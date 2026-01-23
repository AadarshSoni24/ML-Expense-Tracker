import sqlite3
from tabulate import tabulate

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM expenses")
rows = cursor.fetchall()

conn.close()

print(tabulate(rows, headers=["ID", "Date", "Description", "Category", "Amount", "Source"]))
