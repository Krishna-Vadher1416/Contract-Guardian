import re

def split_into_clauses(text):
    clauses = []

    # Split using headings (like Payment, Termination, etc.)
    pattern = r'(CONTRACT AGREEMENT|Payment Terms|Termination|Liability|Confidentiality|Agreement)'
    
    parts = re.split(pattern, text)

    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        content = parts[i+1].strip() if i+1 < len(parts) else ""

        # Fix spacing issue (like 15day → 15 day)
        content = re.sub(r'(\d+)([a-zA-Z]+)', r'\1 \2', content)

        clause = {
            "heading": heading,
            "content": content
        }

        clauses.append(clause)

    return clauses