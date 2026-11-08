# 🏦 LoanWise – Loan Approval Prediction System

An AI-powered Loan Approval Prediction System built using Python and Machine Learning. This project predicts whether a loan application is likely to be approved or rejected based on applicant details.

 📌 Project Overview

LoanWise uses machine learning classification algorithms to analyze applicant information and predict loan approval outcomes.

The project includes data preprocessing, exploratory data analysis, model training, model evaluation, and an interactive web application built with Streamlit.

✨ Features

- Predict loan approval using applicant information.
- Interactive web application built with Streamlit.
- Data cleaning and preprocessing.
- Exploratory Data Analysis (EDA) with visualizations.
- Logistic Regression and Random Forest model comparison.
- Model evaluation using accuracy, precision, recall, and F1-score.
- Saved machine learning pipeline for predictions.

🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Git and GitHub
- VS Code

 📂 Project Structure

```text
Loan-Approval-Prediction/
│
├── dataset/
│   └── loan_data.csv
│
├── notebooks/
│   ├── loan_approval_distribution.png
│   ├── education_distribution.png
│   ├── applicant_income_distribution.png
│   └── credit_history_vs_approval.png
│
├── models/
│   └── best_model.pkl
│
├── train.py
├── eda.py
├── preprocessing.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```
 📊 Machine Learning Models

Two classification algorithms were trained and evaluated:

1. Logistic Regression
2. Random Forest Classifier

 Model Performance

| Evaluation Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 86.18% | 82.11% |
| Precision | 84.00% | 84.62% |
| Recall | 98.82% | 90.59% |
| F1-Score | 90.81% | 87.50% |

**Selected Model:** Logistic Regression, based on the F1-score for the approved class.

These results are from a single test split and do not guarantee performance on new applications.

 🚀 Installation and Setup

 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

 2. Open the project folder

```bash
cd Loan-Approval-Prediction
```

 3. Create a virtual environment

```bash
py -m venv venv
```

 4. Activate the virtual environment (Windows PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

 5. Install dependencies

```bash
pip install -r requirements.txt
```

 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

 🧠 Train the Model

To train the machine learning models again, run:

```bash
python train.py
```

The selected trained model will be saved in:

```text
models/best_model.pkl
```

 📈 Exploratory Data Analysis

The project includes visualizations for:

- Loan approval distribution.
- Education distribution.
- Applicant income distribution.
- Credit history versus loan approval.

 📚 Dataset

Dataset: Loan Prediction Problem Dataset.

The dataset contains applicant details such as income, education, marital status, credit history, loan amount, and loan status.

The target variable is `Loan_Status`:
- `Y` – Loan approved.
- `N` – Loan rejected.

 ⚠️ Disclaimer

This project is developed for educational and demonstration purposes only. Predictions are not actual financial decisions or guarantees of loan approval. The model may reflect limitations and biases present in its training data.

 👨‍💻 Author

Developed as a Machine Learning project using Python, Scikit-learn, and Streamlit.

---

⭐ If you find this project useful, consider giving the repository a star!
