from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        label = "Positive"
        emoji = "😊"
    elif compound <= -0.05:
        label = "Negative"
        emoji = "😠"
    else:
        label = "Neutral"
        emoji = "😐"

    return {
        "label": label,
        "emoji": emoji,
        "score": round(compound, 3),
        "positive": round(scores['pos'] * 100, 1),
        "negative": round(scores['neg'] * 100, 1),
        "neutral":  round(scores['neu'] * 100, 1)
    }