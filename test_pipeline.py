from src.pdf_extractor import extract_text_from_pdf
from src.text_cleaner import clean_text
from src.clause_segmenter import split_into_clauses

file_path = "data/sample_contract.pdf"

# Step 1: Extract
raw_text = extract_text_from_pdf(file_path)

# Step 2: Clean
cleaned_text = clean_text(raw_text)

# Step 3: Split
clauses = split_into_clauses(cleaned_text)

# Output
for i, clause in enumerate(clauses):
    print(f"\nClause {i+1}:")
    print(f"Heading: {clause['heading']}")
    print(f"Content: {clause['content']}")
    