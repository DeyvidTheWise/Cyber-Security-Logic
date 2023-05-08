import re
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Download NLTK data
nltk.download('punkt')

def preprocess_input(input_string):
    # Remove special characters
    input_string = re.sub(r'\W', ' ', input_string)

    # Convert to lowercase
    input_string = input_string.lower()

    # Tokenize the input string
    words = nltk.word_tokenize(input_string)

    return ' '.join(words)

# Sample dataset with labeled inputs
data = [
    ("SELECT * FROM users WHERE username='admin' OR 1=1;--", 1),
    ("SELECT * FROM users WHERE username='normalUser'", 0),
    ("username='normalUser'; DROP TABLE users;", 1),
    ("SELECT * FROM users WHERE username='testUser'", 0)
]

# Preprocess the input strings
preprocessed_data = [(preprocess_input(input_string), label) for input_string, label in data]

# Vectorize the input strings
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([input_string for input_string, label in preprocessed_data])
y = np.array([label for input_string, label in preprocessed_data])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train a Random Forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Test the classifier
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Confusion Matrix: {confusion_matrix(y_test, y_pred)}")