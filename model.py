import pandas as pd
import re
import pickle
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import nltk
nltk.download('stopwords')
print("Step 1 - Loading dataset...")
df = pd.read_csv('IMDB Dataset.csv')
print(f"Dataset loaded! Total reviews: {len(df)}")
print(df.head(3))
df = pd.read_csv('IMDB Dataset.csv')
print(f"Total reviews: {len(df)}")
print(df.head(3))
print("\nStep 2 - Cleaning text...")
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)

df['cleaned'] = df['review'].apply(clean_text)
print("Cleaning done!")
print(df['cleaned'].head(2))
print("\nStep 3 - Preparing features and labels...")
X = df['cleaned']
y = df['sentiment'].map({'positive': 1, 'negative': 0})
print(f"Positive reviews: {y.sum()}")
print(f"Negative reviews: {len(y) - y.sum()}")
print("\nStep 4 - Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Training samples: {len(X_train)}")
print(f"Testing samples:  {len(X_test)}")

print("\nStep 5 - Converting text to numbers (TF-IDF)...")
vectorizer = TfidfVectorizer(max_features=10000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec  = vectorizer.transform(X_test)
print("Text converted to numbers!")

print("\nStep 6 - Training model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)
print("Model trained!")
print("\nStep 7 - Testing model accuracy...")
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy * 100:.2f}%")
print("\nDetailed Report:")
print(classification_report(y_test, y_pred,
      target_names=['Negative', 'Positive']))

print("\nStep 8 - Saving model...")
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
print("Model saved as model.pkl and vectorizer.pkl!")
print("Training complete!")