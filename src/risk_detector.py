def detect_risk(text):
    text_lower = text.lower()

    high_risk_keywords = [
        "penalty",
        "termination without notice",
        "unlimited liability",
        "indemnify",
        "breach",
        "liquidated damages",
        "without prior notice",
        "at sole discretion"
    ]

    risky_sentences = []
    sentences = text.split(".")

    for sentence in sentences:
        for word in high_risk_keywords:
            if word in sentence.lower():
                risky_sentences.append(sentence.strip())
                break

    if risky_sentences:
        return "🔴 High Risk", risky_sentences
    else:
        return "🟢 Low Risk", []