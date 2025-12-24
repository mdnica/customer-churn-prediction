import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"

df = pd.read_csv(url)

# Preview dataset
print(df.head())

# Dataset info (types, non-null counts)
print(df.info())

# Target column distribution (Churn = Yes/No)
print(df["Churn"].value_counts())
