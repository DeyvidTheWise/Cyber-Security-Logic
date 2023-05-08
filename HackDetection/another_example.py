import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


# Generate some sample data (features and labels)
def generate_sample_data(num_samples=1000):
    features = np.random.randn(num_samples, 5)  # 5 random features for each sample
    labels = np.random.randint(
        0, 2, num_samples
    )  # Randomly assign "normal" (0) or "malicious" (1) labels
    return features, labels


# Split data into training and testing sets
features, labels = generate_sample_data()
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42
)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Test the classifier on the test set and print the results
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=["normal", "malicious"]))
