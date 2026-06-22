🛡️ Contract Guardian AI
AI-Powered Contract Risk Detection & Explanation System

Contract Guardian AI is an intelligent system designed to analyze legal contracts, detect risks, classify clauses, and explain them in simple language using Machine Learning and Large Language Models (LLMs).

It helps users — even non-legal professionals — understand complex legal documents quickly and confidently.

---

## 🌐 Live Demo

🔗 https://contract-guardian-ai.onrender.com/

⚠️ **Note:**
This application currently uses a personal API key with limited AI model quota.
Please use the demo responsibly and avoid excessive repeated requests 🙏🙂

---

## 🎯 Problem Statement

Legal contracts are:

• Complex and difficult to understand
• Time-consuming to review
• Prone to hidden risks
• Expensive to analyze (lawyers, consultants)

👉 This project solves these problems by automating contract analysis using AI.

---

## 💡 Solution Overview

Contract Guardian AI:

• Extracts text from uploaded contracts (PDF)
• Breaks content into clauses
• Classifies each clause using ML models
• Detects potential risks
• Uses LLMs to explain clauses in plain English
• Provides an interactive interface for user queries

---

## 🚀 Key Features

### 📄 Contract Upload & Processing

• Upload PDF contracts easily
• Automatic text extraction and preprocessing
• Clause segmentation for better analysis

### 🧠 Clause Classification

Machine Learning model categorizes clauses into:

• Termination
• Payment
• Liability
• Confidentiality
• Others

---

### ⚠️ Risk Detection

Each clause is analyzed for potential risks

Risk levels assigned:

🟢 Low Risk
🟡 Medium Risk
🔴 High Risk

---

### 💬 AI-Powered Explanation

• LLM explains legal clauses in simple, human-readable language
• Helps non-legal users understand contracts easily

---

### ❓ Ask Questions Feature

• Ask custom questions about the contract
• Get contextual AI-driven answers

---

### 📊 Interactive UI

• Clean dashboard
• Real-time analysis display
• Easy navigation and usage

---

## 🌟 Advantages

⏱️ Saves time in contract review
💸 Reduces dependency on legal experts
🧠 Makes legal language accessible
📉 Helps identify hidden risks early
🤖 Combines ML + LLM for powerful insights
📈 Scalable for enterprise use cases

---

## 🏗️ System Architecture

User Upload → Text Extraction → Clause Segmentation → ML Classification → Risk Detection → LLM Explanation → UI Display

---

## 🧠 Tech Stack

### 🔹 Frontend

• Streamlit

### 🔹 Backend

• Python

### 🔹 Machine Learning

• Scikit-learn
• TF-IDF Vectorizer
• Classification Model

### 🔹 LLM Integration

• Google Gemini API

### 🔹 Libraries Used

• PyPDF2 / pdfplumber
• Pandas / NumPy
• dotenv

---

## 📂 Project Structure

contract_guardian/
│── app.py                      # Main Streamlit app
│── models/
│   └── vectorizer.pkl          # ML vectorizer
│── src/
│   ├── risk_detector.py        # Clause classification & risk logic
│   ├── llm_explainer.py        # LLM explanation module
│── requirements.txt
│── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

git clone https://github.com/Krishna-Vadher1416/Contract-Guardian
cd Contract-Guardian

### 2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

## ▶️ Running the Application

streamlit run app.py

---

## 🔄 Workflow

• User uploads contract PDF
• System extracts text
• Text is split into clauses
• ML model classifies each clause
• Risk level is assigned
• LLM generates explanation
• Results displayed in UI
• User can ask follow-up questions

---

## 📊 Example Output

Clause: "Either party may terminate..."
Type: Termination
Risk Level: Low
Explanation: This clause defines conditions under which the agreement can be ended.

---

## 🚧 Future Enhancements

📄 Export analysis as PDF report
🎯 Highlight clauses directly in document
📊 Confidence score visualization
🌐 Multi-cloud deployment (AWS / Azure / GCP)
🧠 Fine-tuned legal AI model
🔍 Search within contract
🗂️ Multi-document comparison

---

## 🎯 Use Cases

• Startups reviewing agreements
• Freelancers analyzing contracts
• Legal tech applications
• HR contract verification
• Business partnerships

---

## 🤝 Contributing

Contributions are welcome!

Steps:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Krishna Vadher

---

## ⭐ Support

If you found this project helpful, please give it a ⭐ on GitHub!
