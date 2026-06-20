from src.pdf_extractor import extract_text_from_pdf
from src.text_cleaner import clean_text
from src.clause_segmenter import split_into_clauses
from src.clause_classifier import train_model, classify_clause
from src.risk_detector import detect_risk

file_path = "data/sample_contract.pdf"

# Step 1: Extract
raw_text = extract_text_from_pdf(file_path)

# Step 2: Clean
cleaned_text = clean_text(raw_text)

# Step 3: Split
clauses = split_into_clauses(cleaned_text)

model, vectorizer = train_model()

# Output
for i, clause in enumerate(clauses):
    label = classify_clause(clause["content"], model, vectorizer)
    risk = detect_risk(clause["content"])

    print(f"\nClause {i+1}:")
    print(f"Heading: {clause['heading']}")
    print(f"Content: {clause['content']}")
    print(f"Predicted Type: {label}")
    print(f"Risk Level: {risk}")