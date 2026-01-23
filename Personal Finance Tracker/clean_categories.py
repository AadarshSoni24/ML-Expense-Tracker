import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

# Step 1: Normalize casing (Food, Transport, etc.)
cursor.execute("""
UPDATE expenses
SET category = UPPER(SUBSTR(category, 1, 1)) || LOWER(SUBSTR(category, 2))
""")

# Step 2: Consolidate overlapping / junk categories
cleanup_rules = [
    ("Food", "Food"),
    ("Groceries", "Groceries"),

    # Sports consolidation
    ("Sports", "Sports equipment"),
    ("Sports", "Sports Equipment"),

    # Junk / test categories
    ("Other", "Anything"),
    ("Other", "Anything "),
    ("Other", "anything")
]

for new, old in cleanup_rules:
    cursor.execute(
        "UPDATE expenses SET category = ? WHERE category = ?",
        (new, old)
    )

conn.commit()
conn.close()

print("✅ Categories normalized and consolidated successfully.")
