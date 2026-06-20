import pandas as pd
import os
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


MODEL_PATH = "models/clause_model.pkl"
VECTORIZER_PATH = "models/vectorizer.pkl"


# =========================
# TRAIN MODEL
# =========================
def train_model():
    # Load dataset
    df = pd.read_csv("data/training_data.csv")

    # Basic cleaning (important!)
    df["text"] = df["text"].astype(str).str.lower()
    df["label"] = df["label"].astype(str)

    # Vectorization
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(df["text"])
    y = df["label"]

    # Model
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    # Save model + vectorizer
    os.makedirs("models", exist_ok=True)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)

    return model, vectorizer


# =========================
# LOAD MODEL (IMPORTANT)
# =========================
def load_model():
    if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)

        with open(VECTORIZER_PATH, "rb") as f:
            vectorizer = pickle.load(f)

        return model, vectorizer
    else:
        # Train if not exists
        return train_model()


# =========================
# CLASSIFY CLAUSE
# =========================
def classify_clause(text, model, vectorizer):
    X = vectorizer.transform([text])

    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]

    confidence = max(probabilities)

    return prediction, confidence