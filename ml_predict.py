import pickle
import re
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))
def clean_text(user_input):
    user_input = re.sub(r'<.*?>', '', user_input)
    user_input = re.sub(r'[^a-zA-Z\s]', '', user_input)
    user_input = user_input.lower()
    words = user_input.split()
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)
def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

def ml_predict(user_input):
    model, vectorizer = load_model()
    cleaned = clean_text(user_input)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    probability = model.predict_proba(vectorized)[0]

    if prediction == 1:
        label = "Positive"
        score = round(probability[1] * 100, 1)
    else:
        label = "Negative"
        score = round(probability[0] * 100, 1)

    return {
        "label": label,
        "score": score
    }
