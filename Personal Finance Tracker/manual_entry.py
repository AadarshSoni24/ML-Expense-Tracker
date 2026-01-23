import sqlite3
from datetime import datetime

def add_expense():
    # Date validation
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD.")

    # Description validation
    while True:
        description = input("Enter description (shop / reason): ").strip()
        if description:
            break
        else:
            print("❌ Description cannot be empty.")

    # Category validation
    while True:
        category = input("Enter category (Food, Travel, etc): ").strip()
        if category:
            break
        else:
            print("❌ Category cannot be empty.")

    # Amount validation
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount > 0:
                break
            else:
                print("❌ Amount must be greater than 0.")
        except ValueError:
            print("❌ Please enter a valid number.")

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (date, description, category, amount, source)
        VALUES (?, ?, ?, ?, ?)
    """, (date, description, category, amount, "manual"))

    conn.commit()
    conn.close()

    print("✅ Expense added successfully.")

if __name__ == "__main__":
    add_expense()
