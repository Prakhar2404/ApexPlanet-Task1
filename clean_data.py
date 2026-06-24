import pandas as pd

df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

print("Missing Values:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())

df["City"] = df["City"].fillna("Unknown")

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df["Customer_Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 25, 40, 60, 100],
    labels=["Young", "Adult", "Middle Age", "Senior"]
)

df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("Cleaning Completed")