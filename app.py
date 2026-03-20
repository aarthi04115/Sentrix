import streamlit as st
import plotly.express as px
import pandas as pd
from sentiment import analyze_sentiment
from aspect import analyze_aspects
from reddit_fetch import fetch_reddit_posts
from ml_predict import ml_predict

st.set_page_config(
    page_title="Sentrix",
    page_icon="🔬",
    layout="wide"
)

st.markdown("""
    <h1 style='text-align:center; color:#7F77DD;'>🔬 Sentrix</h1>
    <p style='text-align:center; color:gray;'>Real-time sentiment intelligence — powered by Reddit & NLP</p>
    <hr>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs([
    "🌐 Live Reddit Analysis",
    "🔍 Aspect Analyzer",
    "🤖 Model Comparison"
])

# ══════════════════════════════════════════════════════════
# TAB 1 — Live Reddit Analysis
# ══════════════════════════════════════════════════════════
with tab1:
    st.subheader("Live Reddit Sentiment Tracker")
    topic = st.text_input("Enter any topic:", placeholder="e.g. iPhone 16, ChatGPT, IPL 2026")
    limit = st.slider("Number of posts to analyze:", 10, 100, 50)

    if st.button("Analyze Reddit 🚀"):
        if topic.strip() == "":
            st.warning("Please enter a topic first!")
        else:
            with st.spinner(f"Fetching Reddit posts about '{topic}'..."):
                df = fetch_reddit_posts(topic, limit)

            if df.empty:
                st.error("No posts found. Try a different topic!")
            else:
                st.success(f"Found {len(df)} posts about '{topic}'!")

                sentiments = []
                for text in df["text"]:
                    result = analyze_sentiment(text)
                    sentiments.append(result["label"])

                df["sentiment"] = sentiments

                col1, col2, col3 = st.columns(3)
                pos_count = sentiments.count("Positive")
                neg_count = sentiments.count("Negative")
                neu_count = sentiments.count("Neutral")

                col1.metric("Positive", f"{pos_count} posts")
                col2.metric("Negative", f"{neg_count} posts")
                col3.metric("Neutral",  f"{neu_count} posts")

                st.markdown("### Sentiment Distribution")
                pie_data = pd.DataFrame({
                    "Sentiment": ["Positive", "Negative", "Neutral"],
                    "Count":     [pos_count, neg_count, neu_count]
                })
                fig_pie = px.pie(
                    pie_data,
                    names="Sentiment",
                    values="Count",
                    color="Sentiment",
                    color_discrete_map={
                        "Positive": "#1D9E75",
                        "Negative": "#E24B4A",
                        "Neutral":  "#888780"
                    }
                )
                st.plotly_chart(fig_pie, use_container_width=True)

                st.markdown("### Sentiment Trend Across Posts")
                score_list = []
                for text in df["text"]:
                    result = analyze_sentiment(text)
                    score_list.append(result["score"])

                df["score"] = score_list
                fig_line = px.line(
                    df,
                    y="score",
                    title="Sentiment Score Per Post",
                    labels={"score": "Sentiment Score", "index": "Post Number"},
                    color_discrete_sequence=["#7F77DD"]
                )
                fig_line.add_hline(y=0, line_dash="dash", line_color="gray")
                st.plotly_chart(fig_line, use_container_width=True)

                st.markdown("### Top Positive Post")
                pos_df = df[df["sentiment"] == "Positive"]
                if not pos_df.empty:
                    best = pos_df.loc[pos_df["score"].idxmax()]
                    st.success(best["title"])
                    st.caption(f"Reddit link: {best['url']}")

                st.markdown("### Top Negative Post")
                neg_df = df[df["sentiment"] == "Negative"]
                if not neg_df.empty:
                    worst = neg_df.loc[neg_df["score"].idxmin()]
                    st.error(worst["title"])
                    st.caption(f"Reddit link: {worst['url']}")

# ══════════════════════════════════════════════════════════
# TAB 2 — Aspect Analyzer
# ══════════════════════════════════════════════════════════
with tab2:
    st.subheader("Aspect-Based Sentiment Analyzer")
    st.caption("Type any product review — Sentrix breaks it down by specific aspects")

    user_review = st.text_area(
        "Enter your review:",
        height=150,
        placeholder="e.g. The camera is absolutely stunning but battery drains super fast. Price is fair though."
    )

    if st.button("Analyze Aspects 🔍"):
        if user_review.strip() == "":
            st.warning("Please enter a review first!")
        else:
            overall = analyze_sentiment(user_review)
            aspects = analyze_aspects(user_review)

            st.markdown("### Overall Sentiment")
            col1, col2 = st.columns(2)
            col1.metric("Verdict", f"{overall['emoji']} {overall['label']}")
            col2.metric("Confidence Score", overall["score"])

            if aspects:
                st.markdown("### Aspect Breakdown")
                for aspect, data in aspects.items():
                    col1, col2, col3 = st.columns([2, 1, 3])
                    col1.write(f"**{aspect.capitalize()}**")
                    if data["sentiment"] == "Positive":
                        col2.success(data["sentiment"])
                    elif data["sentiment"] == "Negative":
                        col2.error(data["sentiment"])
                    else:
                        col2.info(data["sentiment"])
                    col3.caption(f'"{data["sentence"]}"')
            else:
                st.info("No specific aspects detected. Try mentioning camera, battery, price, screen, speed or design!")

# ══════════════════════════════════════════════════════════
# TAB 3 — Model Comparison
# ══════════════════════════════════════════════════════════
with tab3:
    st.subheader("VADER vs Your Trained ML Model")
    st.caption("Same review — two completely different AI approaches. See which one wins!")

    compare_input = st.text_area(
        "Enter any review:",
        height=150,
        placeholder="e.g. The camera is absolutely brilliant but the battery life is honestly terrible!",
        key="compare_input"
    )

    if st.button("Compare Both Models 🤖"):
        if compare_input.strip() == "":
            st.warning("Please enter a review first!")
        else:
            with st.spinner("Running both models..."):
                vader_result = analyze_sentiment(compare_input)
                ml_result    = ml_predict(compare_input)

            st.markdown("### Side by Side Results")
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### 📖 VADER — Rule Based")
                st.caption("Uses a fixed dictionary of 7,500 emotion words")
                if vader_result["label"] == "Positive":
                    st.success(f"😊 Positive")
                elif vader_result["label"] == "Negative":
                    st.error(f"😠 Negative")
                else:
                    st.info(f"😐 Neutral")
                st.metric("Confidence Score", vader_result["score"])
                st.caption("Checks each word against pre-scored list. Fast but cannot learn new patterns.")

            with col2:
                st.markdown("#### 🧠 ML Model — Trained by You!")
                st.caption("Learned patterns from 50,000 real IMDB reviews")
                if ml_result["label"] == "Positive":
                    st.success(f"😊 Positive")
                else:
                    st.error(f"😠 Negative")
                st.metric("Confidence Score", f"{ml_result['score']}%")
                st.caption("TF-IDF + Logistic Regression. Trained on real data. 89.24% accuracy!")

            st.markdown("---")

            st.markdown("### 🏆 Verdict")
            if vader_result["label"] == ml_result["label"]:
                st.success(f"Both models agree — **{ml_result['label']}**! High confidence result ✅")
            else:
                st.warning(f"Models disagree! VADER says **{vader_result['label']}**, ML says **{ml_result['label']}**. Review may be sarcastic or mixed 🤔")

            st.markdown("### 📊 How They Compare")
            diff_data = {
                "Feature":       ["Training needed?", "Handles sarcasm?", "Speed",      "Accuracy",  "Can retrain?"],
                "VADER":         ["No — ready to use", "Partially",       "Very fast",  "~70-75%",   "No"],
                "Your ML Model": ["Yes — 50K reviews", "Better",          "Fast",       "89.24%",    "Yes!"]
            }
            st.dataframe(diff_data, use_container_width=True)

            st.markdown("### 💡 When to use which?")
            tip1, tip2 = st.columns(2)
            with tip1:
                st.info("**Use VADER when:** You need quick results, no training data available, or analyzing social media slang")
            with tip2:
                st.success("**Use ML Model when:** You need high accuracy, have domain-specific data, or want to retrain for your use case")