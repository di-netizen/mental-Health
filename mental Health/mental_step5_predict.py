import pandas as pd
import joblib

# Load model
model = joblib.load("mental_health_model.pkl")

# Create a sample person input (same columns as training)
new_person = pd.DataFrame([{
    'Age': 28,
    'Gender_Male': 1,
    'Gender_Other': 0,
    'Family_History_Yes': 1,
    'Work_Interfere_Often': 0,
    'Work_Interfere_Rarely': 1,
    'Work_Interfere_Sometimes': 0,
    'Remote_Work_Yes': 1,
    'Tech_Company_Yes': 1,
    'Benefits_Yes': 1,
    'Care_Options_Yes': 1,
    'Wellness_Program_Yes': 0,
    'Seek_Help_Yes': 1
}])

# Predict
pred = model.predict(new_person)[0]
print("🧠 Prediction:", "Likely to have mental health condition 🛑" if pred == 1 else "Not likely ✅")
