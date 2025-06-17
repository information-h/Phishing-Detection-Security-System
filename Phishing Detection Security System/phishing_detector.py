import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("dataset.csv")

# Split data
X = df["url"]
y = df["label"]

# Convert URLs to numerical format
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Test function
def check_url(url):
    vector = vectorizer.transform([url])
    prediction = model.predict(vector)[0]
    return "Phishing URL" if prediction == 1 else "Legitimate URL"

# Test the system
test_url = input("Enter a URL to check: ")
print("Result:", check_url(test_url))
