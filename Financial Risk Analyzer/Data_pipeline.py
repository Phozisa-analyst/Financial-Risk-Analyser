import sqlite3
import numpy as np
import pandas as pd

# Set random seed for consistent results
np.random.seed(42)
num_customers = 100

print("⏳ Step 1: Generating core banking datasets...")
data = {
    "CustomerID": range(1001, 1001 + num_customers),
    "Monthly_Income": np.random.randint(15000, 85000, size=num_customers),
    "Existing_Debt": np.random.randint(2000, 35000, size=num_customers),
    "Credit_Score": np.random.randint(500, 850, size=num_customers),
    "Requested_Loan": np.random.randint(50000, 500000, size=num_customers),
}
df = pd.DataFrame(data)

# Clean anomalies as established in Day 1
df["Monthly_Income"] = df["Monthly_Income"].fillna(df["Monthly_Income"].mean())
df["Existing_Debt"] = df["Existing_Debt"].abs()

print("📊 Step 2: Generating historical transaction ledger (3 months per customer)...")
# Create a transaction history to simulate historical bank statements
tx_records = []
for customer_id in df["CustomerID"]:
    # Generate 3 months of historical data
   for month in [1, 2, 3]:


        # Typical salary deposit
        base_income = float(df_row := df[df["CustomerID"] == customer_id]["Monthly_Income"].values[0])
        tx_records.append([customer_id, f"2026-0{month}-25", "Deposit", "Salary", base_income])
        
        # 3 to 5 random monthly expenses/withdrawals
        num_expenses = np.random.randint(3, 6)
        for _ in range(num_expenses):
            expense_amt = np.random.randint(500, 8000)
            tx_records.append([customer_id, f"2026-0{month}-{np.random.randint(1,24)}", "Withdrawal", "Retail/Debit", float(expense_amt)])

df_transactions = pd.DataFrame(tx_records, columns=["CustomerID", "Transaction_Date", "Tx_Type", "Category", "Amount"])

print("🗄️ Step 3: Pushing expanded relational schema to SQLite...")
conn = sqlite3.connect("banking.db")
cursor = conn.cursor()

# Enable Foreign Key support in SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# Recreate fundamental structures
cursor.execute("DROP TABLE IF EXISTS Loan_Requests;")
cursor.execute("DROP TABLE IF EXISTS Account_Transactions;")
cursor.execute("DROP TABLE IF EXISTS Customers;")

cursor.execute("""
    CREATE TABLE Customers (
        CustomerID INTEGER PRIMARY KEY,
        Monthly_Income REAL,
        Existing_Debt REAL
    );
""")

cursor.execute("""
    CREATE TABLE Loan_Requests (
        CustomerID INTEGER,
        Credit_Score INTEGER,
        Requested_Loan REAL,
        FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID)
    );
""")

# Our brand new relational transaction history table
cursor.execute("""
    CREATE TABLE Account_Transactions (
        TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustomerID INTEGER,
        Transaction_Date TEXT,
        Tx_Type TEXT,
        Category TEXT,
        Amount REAL,
        FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID)
    );
""")

# Split and write to database
df[["CustomerID", "Monthly_Income", "Existing_Debt"]].to_sql("Customers", conn, if_exists="append", index=False)
df[["CustomerID", "Credit_Score", "Requested_Loan"]].to_sql("Loan_Requests", conn, if_exists="append", index=False)
df_transactions.to_sql("Account_Transactions", conn, if_exists="append", index=False)

conn.commit()
conn.close()
print("✅ Success! 'banking.db' updated with a 3-Table Relational Schema.")
