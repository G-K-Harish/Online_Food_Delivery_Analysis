
import pandas as pd

# Load the validated cleaned dataset
df = pd.read_csv(r"C:\TRAINING_CODES\Online_Food_Delivery_Analysis\Data\CLEANED_ORDERS.csv")

# Convert Order_Date into a proper date
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    format="%Y-%m-%d",
    errors="coerce"
)

# Validate date conversion
print("Invalid dates:", df["Order_Date"].isna().sum())

# Convert date back to MySQL-friendly YYYY-MM-DD format
df["Order_Date"] = df["Order_Date"].dt.strftime("%Y-%m-%d")

# Export a separate SQL-ready file
df.to_csv(
    r"C:\TRAINING_CODES\Online_Food_Delivery_Analysis\Data\SQL_READY.csv",
    index=False
)

print("\nSQL export completed!")
print("Export shape:", df.shape)
print("Export file: SQL_READY.csv")
