# Training data for ML categorization
training_data = [
    ("zomato order", "Food"),
    ("swiggy food", "Food"),
    ("restaurant bill", "Food"),

    ("uber ride", "Transport"),
    ("ola cab", "Transport"),
    ("bus ticket", "Transport"),

    ("netflix subscription", "Subscriptions"),
    ("spotify premium", "Subscriptions"),
    ("amazon prime", "Subscriptions"),

    ("salary credit", "Income"),
    ("bank interest", "Income"),
    # Sports
    ("cricket bat purchase", "Sports"),
    ("gym membership", "Sports"),
    ("football", "Sports"),

    # Shopping
    ("amazon shopping", "Shopping"),
    ("flipkart order", "Shopping"),
    ("clothes purchase", "Shopping"),

# Health
    ("medical bill", "Health"),
    ("pharmacy medicine", "Health"),
    ("doctor consultation", "Health"),

# Entertainment
    ("movie tickets", "Entertainment"),
    ("cinema hall", "Entertainment"),
    ("concert pass", "Entertainment"),

]
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Separate text and labels
texts = [item[0] for item in training_data]
labels = [item[1] for item in training_data]

# Convert text data to numerical form
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train ML model
model = MultinomialNB()
model.fit(X, labels)

print("ML model trained successfully")


def predict_category(description):
    desc_vector = vectorizer.transform([description])
    prediction = model.predict(desc_vector)
    return prediction[0]


# Test the ML prediction
if __name__ == "__main__":
    test_desc = "zomato food order"
    predicted = predict_category(test_desc)
    print("Description:", test_desc)
    print("Predicted Category:", predicted)
