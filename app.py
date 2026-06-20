import streamlit as st
import pdfplumber

# Import your modules
from src.clause_classifier import train_model, classify_clause
from src.risk_detector import detect_risk

# Train model once
model, vectorizer = train_model()

# Streamlit UI
st.title("📄 Contract Guardian AI")
def answer_question(question, clauses, vectorizer):
    # Convert all clause texts
    clause_texts = [c["content"] for c in clauses]

    # Vectorize
    clause_vectors = vectorizer.transform(clause_texts)
    question_vector = vectorizer.transform([question])

    # Compute similarity
    from sklearn.metrics.pairwise import cosine_similarity
    similarities = cosine_similarity(question_vector, clause_vectors)

    # Get best match
    best_index = similarities.argmax()

    return clauses[best_index]


uploaded_file = st.file_uploader("Upload Contract PDF", type="pdf")


# ---------------------------
# Extract text from PDF
# ---------------------------
def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# ---------------------------
# Split into clauses
# ---------------------------
def split_clauses(text):
    import re

    # Pattern to detect numbered clauses like:
    # 1. Title
    # 1.1 Subtitle
    # 2 Something
    pattern = r'(\n?\d+(\.\d+)*\s+[A-Z][^\n]*)'

    matches = list(re.finditer(pattern, text))

    clauses = []

    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)

        heading = matches[i].group().strip()
        content = text[start:end].strip()

        clauses.append({
            "heading": heading,
            "content": content
        })

    return clauses

# ---------------------------
# Main Logic
# ---------------------------

if uploaded_file is not None:
    text = extract_text(uploaded_file)

    if not text.strip():
        st.error("❌ Could not extract text from PDF")
    else:
        clauses = split_clauses(text)

        if not clauses:
            st.warning("⚠️ No clauses detected. Try a better formatted contract.")
        else:
            # ✅ Q&A SECTION (NOW CORRECTLY PLACED)
            st.subheader("🤖 Ask Questions from Contract")

            user_question = st.text_input("Ask something about the contract:")

            if user_question:
                best_clause = answer_question(user_question, clauses, vectorizer)

                st.markdown("### 💡 Answer")

                summary = best_clause["content"].split(".")[0]

                st.write(f"**Relevant Clause:** {best_clause['heading']}")
                st.write(f"**Answer:** {summary}")

                with st.expander("📖 View Full Clause"):
                    st.write(best_clause["content"])

            st.divider()

            # ✅ CLAUSE ANALYSIS
            st.subheader("📑 Analysis Result")

            for i, clause in enumerate(clauses):

                # Classification
                label, confidence = classify_clause(
                    clause["content"],
                    model,
                    vectorizer
                )

                # Risk Detection
                risk, risky_lines = detect_risk(clause["content"])

                # Display
                st.markdown(f"### Clause {i+1}: {clause['heading']}")

                st.write(f"**Type:** {label} ({confidence*100:.2f}% confidence)")
                st.write(f"**Risk Level:** {risk}")

                # Summary
                summary = clause["content"].split(".")[0]
                st.write(f"**Summary:** {summary}")

                # Risky sentences
                if risky_lines:
                    st.error("⚠️ Risky Sentences Found:")
                    for line in risky_lines:
                        st.write(f"- {line}")

                # Full clause
                with st.expander("📖 View Full Clause"):
                    st.write(clause["content"])

                st.write("---")