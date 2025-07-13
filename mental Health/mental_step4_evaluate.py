import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix

# Load model and test data
model = joblib.load("mental_health_model.pkl")
X_test = pd.read_csv("mental_X_test.csv")
y_test = pd.read_csv("mental_y_test.csv")

# Predict and evaluate
y_pred = model.predict(X_test)

print("✅ Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))
