# 🧠 Mental Health Prediction

This project simulates a real-world mental health prediction system using machine learning. It uses a synthetic dataset to model whether an individual is likely to have a mental health condition based on personal, workplace, and behavioral factors.

---

## 📌 Project Highlights

- 🔧 Generates synthetic mental health data
- 🧹 Cleans and one-hot encodes categorical features
- 📊 Performs model training with Random Forest
- 📈 Evaluates the model with classification metrics
- 🔮 Predicts outcomes for new user input
- 💾 Saves and reloads the trained model

---

## 🗃️ Dataset Overview

The dataset includes the following fields:

- `Age`  
- `Gender` (Male, Female, Other)  
- `Family History of Mental Illness`  
- `Work Interference` (Never, Rarely, Sometimes, Often)  
- `Remote Work`  
- `Tech Company`  
- `Benefits`  
- `Care Options`  
- `Wellness Program`  
- `Seek Help`  
- `Mental Health Condition` (Target Variable)

---

## 📁 Project Structure

```bash
mental-health-prediction/
├── mental_health_raw.csv          # Generated raw dataset
├── mental_health_cleaned.csv      # Cleaned and encoded data
├── mental_health_model.pkl        # Trained model (Random Forest)
├── mental_X_test.csv              # Features for testing
├── mental_y_test.csv              # Target values for testing
├── generate_data.py               # Synthetic data generation script
├── clean_data.py                  # Data cleaning and encoding
├── train_model.py                 # Model training and saving
