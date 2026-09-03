import pandas as pd

data = {
    "Hours": [2, 4, 6, 8],
    "Attendance": [60, 70, 80, 90],
    "Result": ["Fail", "Fail", "Pass", "Pass"]
}

df = pd.DataFrame(data)

print(df)

X = df[["Hours", "Attendance"]]
y = df["Result"]
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print("\n----- X Train -----")
print(X_train)

print("\n----- X Test -----")
print(X_test)

print("\n----- y Train -----")
print(y_train)

print("\n----- y Test -----")
print(y_test)


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Create the model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

print("\n----- Predictions -----")
print(y_pred)

print("\n----- Actual Values -----")
print(y_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n----- Accuracy -----")
print(accuracy)
