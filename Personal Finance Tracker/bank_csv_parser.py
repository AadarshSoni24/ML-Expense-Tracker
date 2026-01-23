import pandas as pd
import sqlite3
from categorizer import categorize

def import_bank_csv(file_path):
    df = pd.read_csv(file_path)

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    for _, row in df.iterrows():
        amount = float(row["Amount"])

        # Skip income for now
        if amount > 0:
            continue

        date = row["Date"]
        description = row["Description"]
        category = categorize(description)

        cursor.execute("""
            INSERT INTO expenses (date, description, category, amount, source)
            VALUES (?, ?, ?, ?, ?)
        """, (date, description, category, abs(amount), "bank"))

    conn.commit()
    conn.close()

    print("Bank statement imported successfully.")

if __name__ == "__main__":
    import_bank_csv("data/bank_statement.csv")
