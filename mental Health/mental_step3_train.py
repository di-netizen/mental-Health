import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load cleaned data
df = pd.read_csv("mental_health_cleaned.csv")

# Feature-target split
X = df.drop("Mental_Health_Condition_Yes", axis=1)
y = df["Mental_Health_Condition_Yes"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model and test set
import joblib
joblib.dump(model, "mental_health_model.pkl")
X_test.to_csv("mental_X_test.csv", index=False)
y_test.to_csv("mental_y_test.csv", index=False)

print("✅ Model trained and saved as 'mental_health_model.pkl'")
