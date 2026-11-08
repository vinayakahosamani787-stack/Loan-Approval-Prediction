
import pandas as pd

# Load dataset
df = pd.read_csv("dataset/loan_data.csv")

print("===== ORIGINAL DATASET =====")
print(df.shape)

# 1. Remove unnecessary Loan_ID column
df = df.drop("Loan_ID", axis=1)

# 2. Replace 3+ with 3 in Dependents
df["Dependents"] = df["Dependents"].replace("3+", "3")

# 3. Handle missing categorical values
categorical_columns = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Property_Area"
]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# 4. Handle missing numerical values
numerical_columns = [
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History"
]

for column in numerical_columns:
    df[column] = df[column].fillna(df[column].median())

# 5. Check missing values after cleaning
print("\n===== MISSING VALUES AFTER CLEANING =====")
print(df.isnull().sum())

# 6. Display cleaned dataset
print("\n===== CLEANED DATASET =====")
print(df.head())

print("\n===== CLEANED DATASET SHAPE =====")
print(df.shape)

print("\nDATA PREPROCESSING COMPLETED!")
