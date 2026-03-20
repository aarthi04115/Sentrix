# 🔬 Sentrix — Real-Time Sentiment Intelligence

> Analyze public opinion on any topic, instantly. Powered by live Reddit data, NLP, and a trained ML model.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit)
![Accuracy](https://img.shields.io/badge/Model%20Accuracy-89.24%25-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 📌 What is Sentrix?

Sentrix is a real-time NLP dashboard that fetches live Reddit posts on any topic and performs both **overall** and **aspect-level** sentiment analysis — then compares a rule-based approach (VADER) against a custom-trained ML model side by side.

Unlike typical sentiment analysis projects that use static datasets, Sentrix works on **live data** fetched directly from Reddit — making every analysis unique and genuinely useful.

---

## ✨ Features

### 🌐 Tab 1 — Live Reddit Analysis
- Fetches 10–100 live Reddit posts on any topic in real time
- Classifies each post as Positive, Negative, or Neutral
- Interactive pie chart — sentiment distribution
- Trend line — sentiment score across posts
- Top positive and negative posts with direct Reddit links

### 🔍 Tab 2 — Aspect-Based Sentiment Analyzer
- Paste any product review
- Breaks it down by specific aspects — camera, battery, price, display, speed, design
- Each aspect gets its own sentiment score independently
- Example:
  ```
  Input:   "Camera is stunning but battery drains too fast. Price is fair."
  Output:  Camera  → Positive 85%
           Battery → Negative 78%
           Price   → Neutral  55%
  ```

### 🤖 Tab 3 — Model Comparison
- Same review analyzed by two different AI approaches simultaneously
- VADER (rule-based, 7500 word dictionary) vs Your Trained ML Model
- Radar chart comparing accuracy, speed, sarcasm handling, and customizability
- Auto-detects when models disagree — flags ambiguous or sarcastic reviews

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| Streamlit | Web application UI |
| VADER (NLTK) | Rule-based sentiment scoring |
| SpaCy | NLP — sentence splitting & aspect extraction |
| Scikit-learn | Logistic Regression ML model |
| TF-IDF Vectorizer | Text to numerical features |
| Plotly | Interactive charts and visualizations |
| Requests | Live Reddit data fetching |
| Pandas | Data handling and manipulation |
| Pickle | Model serialization |

---

## 📊 ML Model Performance

Trained on the IMDB 50K Movie Reviews dataset using Logistic Regression + TF-IDF.

| Metric | Score |
|---|---|
| Accuracy | **89.24%** |
| F1 Score (Positive) | **0.89** |
| F1 Score (Negative) | **0.89** |
| Precision | **0.89** |
| Recall | **0.89** |
| Training samples | 40,000 |
| Test samples | 10,000 |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or above
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/aarthi04115/Sentrix.git
cd Sentrix

# Install dependencies
pip install -r requirements.txt

# Download SpaCy language model
python -m spacy download en_core_web_sm
```

### Train the ML Model

```bash
python model_train.py
```

This will generate `model.pkl` and `vectorizer.pkl` in the project directory.

> Note: Download the IMDB Dataset from [Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) and place it in the project root before training.

### Run the App

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
Sentrix/
├── app.py              ← Main Streamlit web app (3 tabs)
├── sentiment.py        ← VADER sentiment analyzer
├── aspect.py           ← Aspect-based sentiment extraction
├── reddit_fetch.py     ← Live Reddit data fetcher
├── ml_predict.py       ← Trained ML model predictor
├── model_train.py      ← Model training script
├── requirements.txt    ← Project dependencies
└── README.md           ← You are here
```

---

## 💡 Why Sentrix?

| Typical Student Project | Sentrix |
|---|---|
| Static IMDB CSV dataset | Live Reddit data — different every demo |
| Just positive / negative | Aspect-level breakdown per topic |
| Terminal output only | Full interactive web dashboard |
| Single approach | VADER vs ML model comparison |
| Generic name | Branded, memorable product |

---

## 👤 Author

**Aarthi G D**

Built as part of an AI/ML learning journey — combining NLP, machine learning, and real-time data to solve a genuine problem.

---

## 📄 License

This project is licensed under the MIT License.

---

Built with Python · VADER · SpaCy · Sklearn · Streamlit
