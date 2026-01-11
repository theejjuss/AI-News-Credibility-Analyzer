# AI News Credibility Analyzer 🧠📰

An AI-powered web application that analyzes the **credibility of news articles** using machine learning and linguistic indicators.  
The system helps users identify **potentially fake, misleading, or trustworthy news** through explainable analysis and visual insights.

🔗 **Live Demo (Render):** https://ai-news-credibility-analyzer.onrender.com  
*(Replace with your actual Render URL)*

---

## 📌 Problem Statement

With the rapid spread of misinformation across digital platforms, users often struggle to verify the authenticity of online news.  
Manual fact-checking is time-consuming and requires expertise.

**This project addresses the problem by providing:**
- Automated credibility assessment
- Explainable indicators instead of black-box decisions
- A simple, user-friendly interface for analysis

---

## 🎯 Objectives

- Detect whether a news article is **likely credible or suspicious**
- Provide a **credibility score** with risk interpretation
- Highlight linguistic and structural patterns linked to fake news
- Maintain **input persistence** and user-friendly UX
- Deploy the system as a live web application

---

## 🧠 System Overview

The system follows a **hybrid approach**:
- **Machine Learning Model** for credibility prediction
- **Rule-based linguistic analysis** for explainability
- **Web interface** for interaction and visualization

### Workflow:
1. User pastes a news article
2. Text preprocessing and feature extraction
3. ML model predicts credibility score
4. Rule-based indicators analyze linguistic signals
5. Results are displayed with charts and explanations

---

## 🏗️ Architecture

User Interface (HTML/CSS/JS)
↓
Flask Backend
↓
Text Preprocessing
↓
ML Credibility Model
↓
Score Fusion & Interpretation
↓
Visual Analytics Output

---

## 🧪 Technologies Used

### Frontend
- HTML5
- CSS3 (Custom styling & animations)
- JavaScript (UI logic, charts, persistence)

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- TF-IDF Vectorization
- Trained classification model

### Deployment
- GitHub (Version Control)
- Render (Cloud Deployment)

---

## 📊 Features

- ✅ Paste-and-analyze news articles
- ✅ Credibility score with confidence labels
- ✅ Animated bar charts and breakdown metrics
- ✅ Explainable analysis (not a black-box)
- ✅ Input text persistence after analysis
- ✅ Clean and professional UI
- ✅ Live deployment with public URL

---

## ⚠️ Limitations

- The system **does not fact-check against live databases**
- It evaluates **credibility indicators**, not absolute truth
- Performance depends on the quality and diversity of training data
- Not intended for legal or journalistic decision-making

---

## 🚀 Deployment (Render)

The application is deployed using **Render (Python Web Service)**.

### Deployment Configuration:
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python app.py`
- **Port:** `5000`

Raw datasets were removed from the repository to:
- Reduce repository size
- Improve deployment reliability
- Follow industry best practices

---

## 📁 Project Structure

AI-News-Credibility-Analyzer/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── templates/
│ └── index.html
├── models/
│ └── model.pkl
├── src/
└── README.md


---

## 🧠 Future Enhancements

- Integration with live fact-check APIs
- Multilingual news analysis
- Deep learning-based credibility modeling
- User authentication and saved analysis history
- Browser extension support

---

## 👨‍🎓 Academic Declaration

This project was developed **for academic purposes** as part of a final-year engineering curriculum.  
All results and evaluations are intended for **educational demonstration only**.

---

## 📜 License

This project is released for **academic and educational use only**.

---

## 🙌 Acknowledgements

- Open-source Python and ML community
- Flask documentation
- Scikit-learn contributors
- Render deployment platform
