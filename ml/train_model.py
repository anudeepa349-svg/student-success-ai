import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from pathlib import Path

# Create training data
df = pd.DataFrame([
    [90, 85, 5, 90, "Low"],
    [85, 80, 4, 85, "Low"],
    [80, 75, 4, 80, "Low"],
    [75, 70, 3, 75, "Low"],
    [70, 60, 3, 70, "Medium"],
    [65, 50, 2, 60, "Medium"],
    [60, 45, 1, 50, "High"],
    [95, 90, 6, 95, "Low"],
    [88, 82, 5, 88, "Low"],
    [72, 55, 2, 55, "Medium"]
], columns=[
    "attendance",
    "internal_marks",
    "study_hours",
    "assignment_completion",
    "risk"
])

print("Training data created successfully.")
print(df)

# Features
X = df[
    [
        "attendance",
        "internal_marks",
        "study_hours",
        "assignment_completion"
    ]
]

# Target
y = df["risk"]

# Create and train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Save model
ml_folder = Path(__file__).resolve().parent
model_path = ml_folder / "risk_model.pkl"

joblib.dump(model, model_path)

print("\nMachine Learning model trained successfully!")
print(f"Model saved at: {model_path}")