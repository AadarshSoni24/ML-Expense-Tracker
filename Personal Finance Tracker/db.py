import sqlite3

def create_database():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            category TEXT,
            amount REAL,
            source TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("Database and table created successfully.")

if __name__ == "__main__":
    create_database()
