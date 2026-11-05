"""SWYNEX - Data Cleaning & Preparation
Dataset: Titanic (public dataset)
Run in Google Colab or any Python setup with pandas installed.
"""
import pandas as pd

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(URL)
df.to_csv("titanic_raw.csv", index=False)

print("=== BEFORE CLEANING ===")
print("Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nData types:\n", df.dtypes)

# 1. Remove duplicate records
df = df.drop_duplicates()

# 2. Fix inconsistent text values (extra spaces, mixed case)
for col in ["Name", "Sex", "Embarked", "Ticket", "Cabin"]:
    df[col] = df[col].astype("string").str.strip()
df["Sex"] = df["Sex"].str.lower()
df["Embarked"] = df["Embarked"].str.upper()

# 3. Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Cabin"] = df["Cabin"].fillna("Unknown")

# 4. Correct data types
df["Survived"] = df["Survived"].astype("int")
df["Pclass"] = df["Pclass"].astype("category")
df["Sex"] = df["Sex"].astype("category")
df["Embarked"] = df["Embarked"].astype("category")
df["Age"] = df["Age"].round(0).astype("int")

# 5. Sanity checks on values
df = df[(df["Age"] > 0) & (df["Fare"] >= 0)]

print("\n=== AFTER CLEANING ===")
print("Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nData types:\n", df.dtypes)

df.to_csv("titanic_cleaned.csv", index=False)
print("\nSaved titanic_cleaned.csv")
