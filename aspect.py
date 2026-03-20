import spacy

nlp = spacy.load("en_core_web_sm")

ASPECTS = {
    "camera":  ["camera", "photo", "picture", "lens", "selfie", "shot"],
    "battery": ["battery", "charge", "charging", "drain", "power"],
    "price":   ["price", "cost", "expensive", "cheap", "value", "worth"],
    "display": ["screen", "display", "brightness", "resolution"],
    "speed":   ["fast", "slow", "speed", "performance", "lag", "smooth"],
    "design":  ["design", "build", "look", "slim", "heavy", "light"],
}

POSITIVE_WORDS = [
    "good", "great", "amazing", "excellent", "love", "brilliant",
    "stunning", "fantastic", "nice", "best", "perfect", "superb",
    "awesome", "clear", "smooth", "impressive"
]

NEGATIVE_WORDS = [
    "bad", "terrible", "poor", "hate", "slow", "drain", "expensive",
    "heavy", "ugly", "worst", "horrible", "disappointing", "awful",
    "blurry", "laggy", "fast"  
]

def get_sentence_sentiment(sentence):
    sentence = sentence.lower()
    pos = sum(1 for w in POSITIVE_WORDS if w in sentence)
    neg = sum(1 for w in NEGATIVE_WORDS if w in sentence)

    if pos > neg:
        return "Positive", round(min(95, 60 + pos * 10))
    elif neg > pos:
        return "Negative", round(min(95, 60 + neg * 10))
    else:
        return "Neutral", 55

def analyze_aspects(text):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    results = {}

    for aspect, keywords in ASPECTS.items():
        for sentence in sentences:
            sentence_lower = sentence.lower()
            if any(keyword in sentence_lower for keyword in keywords):
                sentiment, score = get_sentence_sentiment(sentence_lower)
                results[aspect] = {
                    "sentiment": sentiment,
                    "score": score,
                    "sentence": sentence.strip()
                }
                break

    return results