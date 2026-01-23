def load_expenses():
    conn = sqlite3.connect("finance.db")
    df = pd.read_sql_query(
        "SELECT date, category, amount FROM expenses",
        conn
    )
    conn.close()
    return df
