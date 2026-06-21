import streamlit as st
import pdfplumber

# Import your modules
from src.clause_classifier import train_model, classify_clause
from src.risk_detector import detect_risk

from src.llm_explainer import explain_clause

# Train model once
model, vectorizer = train_model()

# Streamlit UI
st.set_page_config(page_title="Contract Guardian", layout="wide")

st.title("📜 Contract Guardian AI")
st.markdown("AI-powered contract risk detection & explanation system")


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

st.sidebar.title("⚙️ Settings")
st.sidebar.markdown("Upload your contract and analyze risks")



with st.sidebar:
    st.header("⚙️ Settings")
    uploaded_file = st.file_uploader("📄 Upload Contract", type="pdf")
    if uploaded_file:
        st.sidebar.success("✅ File uploaded successfully")


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

    # 🔥 NEW: Full Contract Analysis Function
    def analyze_full_contract(contract_text):
        prompt = f"""
        You are a legal AI assistant.

        Analyze this contract and provide:
        1. Summary
        2. Key Risks
        3. Important obligations
        4. Any unfair clauses

        Contract:
        {contract_text}
        """

        response = explain_clause(contract_text)  # reuse your LLM function
        return response

    text = extract_text(uploaded_file)

    if not text.strip():
        st.error("❌ Could not extract text from PDF")
    else:
        clauses = split_clauses(text)

        # 🔥 BUTTON: Full Analysis
        if st.button("🔍 Analyze Full Contract"):
    
            with st.spinner("Analyzing with AI..."):
                result = analyze_full_contract(text)

            st.subheader("📊 Full Contract Analysis")
            st.write(result)

            st.download_button(
                label="📥 Download Analysis",
                data=result,
                file_name="contract_analysis.txt"
        )

        if not clauses:
            st.warning("⚠️ No clauses detected. Try a better formatted contract.")
        else:
            # ✅ Q&A SECTION (NOW CORRECTLY PLACED)
            st.subheader("🤖 Ask Questions from Contract")

            # 🔥 Chat memory
            if "chat_history" not in st.session_state:
                st.session_state.chat_history = []

            user_question = st.text_input("Ask something about the contract:")

            if user_question:
                best_clause = answer_question(user_question, clauses, vectorizer)
                llm_answer = explain_clause(best_clause["content"])

                st.session_state.chat_history.append(("You", user_question))
                st.session_state.chat_history.append(("AI", llm_answer))

            # Display chat history
            for sender, msg in st.session_state.chat_history:
                st.write(f"**{sender}:** {msg}")

            if user_question:
                best_clause = answer_question(user_question, clauses, vectorizer)

                st.markdown("### 💡 Answer")

                llm_answer = explain_clause(best_clause["content"])

                st.write(f"**Relevant Clause:** {best_clause['heading']}")
                st.write(f"**Answer:** {llm_answer}")

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

                # LLM Explanation (only for medium/high risk to save API usage)
                llm_output = ""

                if risk in ["Medium", "High"]:
                    try:
                        llm_output = explain_clause(clause["content"])
                    except Exception as e:
                        llm_output = "⚠️ LLM failed: " + str(e)

                # Display
                st.markdown(f"### Clause {i+1}: {clause['heading']}")

                st.write(f"**Type:** {label} ({confidence*100:.2f}% confidence)")
                if risk == "High":
                    st.error(f"⚠️ Risk Level: {risk}")
                elif risk == "Medium":
                    st.warning(f"⚠️ Risk Level: {risk}")
                else:
                    st.success(f"✅ Risk Level: {risk}")

                # Summary
                summary = clause["content"].split(".")[0]
                st.write(f"**Summary:** {summary}")

                # LLM Insight
                if llm_output:
                    st.info("🤖 AI Insight")
                    st.write(llm_output)

                # Risky sentences
                if risky_lines:
                    st.error("⚠️ Risky Sentences Found:")
                    for line in risky_lines:
                        st.write(f"- {line}")

                # Full clause
                with st.expander("📖 View Full Clause"):
                    st.write(clause["content"])

                # 🔥 NEW: Rewrite Button
                if st.button(f"Rewrite Clause {i+1}"):
                    try:
                        rewritten = explain_clause(
                            f"Rewrite this clause in a safer way:\n{clause['content']}"
                        )
                        st.success("✍️ Safer Version:")
                        st.write(rewritten)
                    except Exception as e:
                        st.error(f"Error: {e}")

                st.write("---")

