
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset/loan_data.csv")

# Set plot style
sns.set_theme(style="whitegrid")

# 1. Loan approval distribution
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Loan_Status")
plt.title("Loan Approval Distribution")
plt.xlabel("Loan Status")
plt.ylabel("Number of Applicants")
plt.savefig("notebooks/loan_approval_distribution.png")
plt.show()

# 2. Education distribution
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Education")
plt.title("Education Distribution")
plt.xlabel("Education")
plt.ylabel("Number of Applicants")
plt.savefig("notebooks/education_distribution.png")
plt.show()

# 3. Applicant income distribution
plt.figure(figsize=(7, 5))
sns.histplot(data=df, x="ApplicantIncome", bins=30, kde=True)
plt.title("Applicant Income Distribution")
plt.xlabel("Applicant Income")
plt.ylabel("Frequency")
plt.savefig("notebooks/applicant_income_distribution.png")
plt.show()

# 4. Credit history vs loan approval
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Credit_History", hue="Loan_Status")
plt.title("Credit History vs Loan Approval")
plt.xlabel("Credit History")
plt.ylabel("Number of Applicants")
plt.savefig("notebooks/credit_history_vs_approval.png")
plt.show()

print("EDA completed successfully!")
