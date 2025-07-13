import pandas as pd
import random

# Create synthetic dataset
def generate_data(n=1000):
    genders = ["Male", "Female", "Other"]
    yes_no = ["Yes", "No"]
    work_interfere = ["Never", "Rarely", "Sometimes", "Often"]

    data = {
        "Age": [random.randint(18, 60) for _ in range(n)],
        "Gender": [random.choice(genders) for _ in range(n)],
        "Family_History": [random.choice(yes_no) for _ in range(n)],
        "Work_Interfere": [random.choice(work_interfere) for _ in range(n)],
        "Remote_Work": [random.choice(yes_no) for _ in range(n)],
        "Tech_Company": [random.choice(yes_no) for _ in range(n)],
        "Benefits": [random.choice(yes_no) for _ in range(n)],
        "Care_Options": [random.choice(yes_no) for _ in range(n)],
        "Wellness_Program": [random.choice(yes_no) for _ in range(n)],
        "Seek_Help": [random.choice(yes_no) for _ in range(n)],
        "Mental_Health_Condition": [random.choice(yes_no) for _ in range(n)],
    }

    df = pd.DataFrame(data)
    df.to_csv("mental_health_raw.csv", index=False)
    print("✅ 'mental_health_raw.csv' created with shape:", df.shape)
    print("\nFirst 5 rows:\n", df.head())

generate_data()

