#exploratory data analysis
"""
import pandas as pd
import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.head())
print(df.info())
print(df.describe())
"""

import pandas as pd

data = {
    "Hours": [2, 4, 6, 8],
    "Attendance": [60, 70, 80, 90],
    "Result": ["Fail", "Fail", "Pass", "Pass"]
}

df = pd.DataFrame(data)

print(df)

print("\n--- Dataset Information ---")
print(df.info())

print("\n--- Statistical Information ---")
print(df.describe())

print(df.head())       # See data
print(df.info())       # Understand data
print(df.describe())   # Statistics
print(df["Hours"])     # Select a column
print(df.isnull())     # Find missing values
print(df.dropna())     # Remove missing values
print(df.mean(numeric_only=True))    # Calculate average

X = df[["Hours", "Attendance"]]
y = df["Result"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)

