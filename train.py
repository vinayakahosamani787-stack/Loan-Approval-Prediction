
import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("dataset/loan_data.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


# ==========================================
# 2. REMOVE UNNECESSARY COLUMN
# ==========================================

df = df.drop("Loan_ID", axis=1)


# ==========================================
# 3. SEPARATE FEATURES AND TARGET
# ==========================================

X = df.drop("Loan_Status", axis=1)

y = df["Loan_Status"].map({
    "Y": 1,
    "N": 0
})


# ==========================================
# 4. IDENTIFY COLUMN TYPES
# ==========================================

categorical_columns = X.select_dtypes(
    include=["object", "str"]
).columns.tolist()

numerical_columns = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

print("\nCategorical columns:", categorical_columns)
print("Numerical columns:", numerical_columns)


# ==========================================
# 5. CREATE NUMERICAL PIPELINE
# ==========================================

numerical_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])


# ==========================================
# 6. CREATE CATEGORICAL PIPELINE
# ==========================================

categorical_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])


# ==========================================
# 7. COMBINE PREPROCESSING PIPELINES
# ==========================================

preprocessor = ColumnTransformer(transformers=[
    ("numerical", numerical_pipeline, numerical_columns),
    ("categorical", categorical_pipeline, categorical_columns)
])


# ==========================================
# 8. SPLIT DATASET
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\n===== DATA SPLIT =====")
print("Training records:", X_train.shape[0])
print("Testing records:", X_test.shape[0])


# ==========================================
# 9. DEFINE MACHINE LEARNING MODELS
# ==========================================

models = {
    "Logistic Regression": LogisticRegression(
        max_iter=3000
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )
}


# ==========================================
# 10. TRAIN AND EVALUATE MODELS
# ==========================================

results = {}
trained_pipelines = {}

for name, model in models.items():

    print("\n===================================")
    print("Training:", name)
    print("===================================")

    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", model)
    ])

    # Train model
    pipeline.fit(X_train, y_train)

    # Make predictions
    predictions = pipeline.predict(X_test)

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, predictions)

    precision = precision_score(
        y_test,
        predictions,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        zero_division=0
    )

    # Store results
    results[name] = {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    }

    trained_pipelines[name] = pipeline

    # Display results
    print("\nAccuracy:", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall:", round(recall, 4))
    print("F1 Score:", round(f1, 4))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=["Rejected", "Approved"],
            zero_division=0
        )
    )


# ==========================================
# 11. COMPARE MODELS
# ==========================================

results_df = pd.DataFrame(results).T

print("\n===================================")
print("MODEL COMPARISON")
print("===================================")

print(results_df.round(4))


# ==========================================
# 12. SELECT BEST MODEL
# ==========================================

best_model_name = results_df["F1 Score"].idxmax()

best_pipeline = trained_pipelines[best_model_name]

print("\nBest Model:", best_model_name)


# ==========================================
# 13. SAVE BEST MODEL
# ==========================================

os.makedirs("models", exist_ok=True)

joblib.dump(
    best_pipeline,
    "models/best_model.pkl"
)

print("\nModel saved successfully!")
print("Location: models/best_model.pkl")


# ==========================================
# 14. COMPLETION MESSAGE
# ==========================================

print("\n===================================")
print("MODEL TRAINING COMPLETED!")
print("===================================")
