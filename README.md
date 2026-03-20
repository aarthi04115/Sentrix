# 🔬 Sentrix — Real-Time Sentiment Intelligence

> Built by [AARTHI GD] | 

Sentrix is a real-time NLP dashboard that fetches live Reddit posts 
on any topic and performs both overall and aspect-level sentiment analysis.

---

## What Makes Sentrix Different?

- Live Reddit data — not a static old dataset
- Aspect-level analysis — breaks reviews into camera, battery, price etc
- Interactive charts — pie chart, trend line, top posts
- Clean web UI — no terminal needed, runs in browser

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web app UI |
| VADER | Sentiment scoring |
| SpaCy | NLP sentence splitting |
| Plotly | Interactive charts |
| Requests | Live Reddit data fetching |
| Pandas | Data handling |

---

## How to Run

**Step 1 — Install libraries:**
pip install -r requirements.txt
python -m spacy download en_core_web_sm

**Step 2 — Run the app:**
streamlit run app.py

**Step 3 — Open browser:**
Go to http://localhost:8501

---

## Features

### Live Reddit Tracker
- Type any topic
- Fetches 50+ real Reddit posts instantly
- Shows sentiment pie chart
- Shows sentiment trend line
- Shows most positive and most negative post

### Aspect Analyzer
- Type any product review
- Breaks it down by camera, battery, price, display, speed, design
- Shows which aspect is positive or negative separately

---

## Sample Output

Input: "The camera is stunning but battery drains too fast. Price is fair."

| Aspect | Sentiment | Score |
|---|---|---|
| Camera | Positive | 85% |
| Battery | Negative | 75% |
| Price | Neutral | 55% |

---

## Author
Built by [Your Name]
[Your College Name] — [Your Branch] — [Your Year]
```

**Step 3** — Press **Ctrl + S** ✅

---

## 📖 Why README Matters So Much

When a recruiter opens your GitHub repo, the **first thing they see** is your README — before even looking at code.

A good README tells them:
- What the project does in 10 seconds
- How to run it without asking you
- That you think like a professional, not a student

> A project with no README = recruiter closes the tab immediately ❌
> A project with a clean README = recruiter keeps reading ✅

---

## 🎉 All 6 Files Done!

Your Sentrix folder should now look like:
```
Sentrix/
├── app.py
├── sentiment.py
├── aspect.py
├── reddit_fetch.py
├── requirements.txt
└── README.md