import sqlite3
import pandas as pd

def export_all_expenses():
    conn = sqlite3.connect("finance.db")

    query = """
    SELECT id, date, description, category, amount, source
    FROM expenses
    ORDER BY date
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    df.to_csv("all_expenses.csv", index=False)
    print("✅ All expenses exported to all_expenses.csv")

if __name__ == "__main__":
    export_all_expenses()
