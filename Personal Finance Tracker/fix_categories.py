import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

# Normalize all category values to Title Case
cursor.execute("""
UPDATE expenses
SET category = UPPER(SUBSTR(category, 1, 1)) || LOWER(SUBSTR(category, 2))
""")

conn.commit()
conn.close()

print("✅ All existing categories normalized successfully.")
