import re

def extract_clauses(text):
    pattern = r'(\d+\.\d+\s+[A-Za-z ].*?)(?=\n\d+\.\d+|\n\d+\.|\Z)'
    
    matches = re.findall(pattern, text, re.DOTALL)

    clauses = []
    
    for i, match in enumerate(matches):
        lines = match.strip().split("\n")
        heading = lines[0]
        content = " ".join(lines[1:])
        
        clauses.append({
            "clause_id": i+1,
            "heading": heading,
            "content": content
        })
    
    return clauses

