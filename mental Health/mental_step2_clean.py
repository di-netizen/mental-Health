import pandas as pd

# Load dataset
df = pd.read_csv("mental_health_raw.csv")
print("📊 Original shape:", df.shape)

# Drop duplicates if any
df = df.drop_duplicates()

# Handle missing values (if any appear)
df.fillna(method='ffill', inplace=True)

# One-hot encode categorical columns
df_encoded = pd.get_dummies(df, drop_first=True)

# Show new shape and columns
print("✅ Cleaned shape:", df_encoded.shape)
print("📋 Columns:\n", df_encoded.columns.tolist())

# Save cleaned dataset
df_encoded.to_csv("mental_health_cleaned.csv", index=False)
print("📁 Saved as 'mental_health_cleaned.csv'")
