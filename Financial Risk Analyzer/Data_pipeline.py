import sqlite3
import numpy as np
import pandas as pd

# Set random seed for consistent results
np.random.seed(42)
num_customers = 100

print("⏳ Step 1: Generating realistic banking dataset...")

# 1. Create a dictionary of customer banking traits
data = {
    "CustomerID": range(1001, 1001 + num_customers),
    "Monthly_Income": np.random.randint(15000, 85000, size=num_customers),
    "Existing_Debt": np.random.randint(2000, 35000, size=num_customers),
    "Credit_Score": np.random.randint(500, 850, size=num_customers),
    "Requested_Loan": np.random.randint(50000, 500000, size=num_customers),
}

df = pd.DataFrame(data)

# 2. Inject intentional anomalies for data-cleansing proof
# Let's make 5 customer incomes missing (NaN) and 3 existing debts negative
df.loc[df.sample(5).index, "Monthly_Income"] = np.nan
df.loc[df.sample(3).index, "Existing_Debt"] = -5000

print("🧹 Step 2: Cleansing data pipeline anomalies...")
# Fix anomalies: Fill missing income with the average, turn negative debt into positive
df["Monthly_Income"] = df["Monthly_Income"].fillna(df["Monthly_Income"].mean())
df["Existing_Debt"] = df["Existing_Debt"].abs()

print("🗄️ Step 3: Creating local relational SQLite database...")
# Connect to SQLite (creates banking.db file automatically if it doesn't exist)
conn = sqlite3.connect("banking.db")
cursor = conn.cursor()

# Create Tables using raw SQL to show structural knowledge
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INTEGER PRIMARY KEY,
        Monthly_Income REAL,
        Existing_Debt REAL
    )
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Loan_Requests (
        CustomerID INTEGER,
        Credit_Score INTEGER,
        Requested_Loan REAL,
        FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID)
    )
"""
)

# Split our pandas dataframe into our database tables
df_customers = df[["CustomerID", "Monthly_Income", "Existing_Debt"]]
df_loans = df[["CustomerID", "Credit_Score", "Requested_Loan"]]

# Write tables into SQLite
df_customers.to_sql("Customers", conn, if_exists="replace", index=False)
df_loans.to_sql("Loan_Requests", conn, if_exists="replace", index=False)

conn.commit()
conn.close()
print("✅ Success! 'banking.db' initialized with structured data tables.")
