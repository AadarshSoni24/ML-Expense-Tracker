import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from manual_entry import add_expense
from bank_csv_parser import import_bank_csv
import reports
import os
import sqlite3
from datetime import datetime
from ocr_receipt import extract_total_from_receipt
from ml_categorizer import predict_category


# ---------- Button Functions ----------

def open_add_expense():
    add_expense()


def add_expense_via_ocr():
    file_path = filedialog.askopenfilename(
        title="Select Receipt Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if not file_path:
        return

    amount = extract_total_from_receipt(file_path)

    if not amount:
        messagebox.showerror(
            "OCR Failed",
            "Could not extract total amount from receipt."
        )
        return

    date = datetime.today().strftime("%Y-%m-%d")
    description = "OCR Receipt Expense"
    category = predict_category(description)

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (date, description, category, amount, source)
        VALUES (?, ?, ?, ?, ?)
    """, (date, description, category, float(amount), "ocr"))

    conn.commit()
    conn.close()

    messagebox.showinfo(
        "OCR Saved",
        f"Expense saved successfully!\nAmount: {amount}"
    )


def import_csv():
    try:
        import_bank_csv("data/bank_statement.csv")
        messagebox.showinfo("Success", "Bank CSV imported successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def view_all_expenses():
    os.system("python view_expenses.py")


def view_basic_reports():
    df = reports.load_expenses()
    reports.category_wise_report(df)
    reports.monthly_total_report(df)
    reports.highest_spending_category(df)


def date_range_report():
    df = reports.load_expenses()
    reports.date_range_report(df)


def save_monthly_report():
    df = reports.load_expenses()
    reports.save_monthly_report(df)
    messagebox.showinfo("Saved", "Monthly report saved as monthly_report.csv")


def filter_by_category():
    category = simpledialog.askstring(
        "Filter by Category",
        "Enter category name (e.g. Food, Travel, Shopping):"
    )

    if not category:
        return

    df = reports.load_expenses()
    filtered_df = df[df["category"].str.lower() == category.lower()]

    if filtered_df.empty:
        messagebox.showinfo(
            "No Data",
            f"No expenses found for category: {category}"
        )
        return

    reports.category_wise_report(filtered_df)


# ---------- Main Window ----------

root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("420x520")


tk.Label(
    root,
    text="Personal Finance Tracker",
    font=("Arial", 16, "bold")
).pack(pady=15)


# ---------- Expense Actions ----------

tk.Button(
    root,
    text="Add Expense Manually",
    width=35,
    command=open_add_expense
).pack(pady=5)

tk.Button(
    root,
    text="Add Expense via Receipt (OCR)",
    width=35,
    command=add_expense_via_ocr
).pack(pady=5)

tk.Button(
    root,
    text="Import Bank CSV",
    width=35,
    command=import_csv
).pack(pady=5)


# ---------- Filters & Reports ----------

tk.Button(
    root,
    text="Filter by Category",
    width=35,
    command=filter_by_category
).pack(pady=5)

tk.Button(
    root,
    text="Date Range Expense Report",
    width=35,
    command=date_range_report
).pack(pady=5)


# ---------- Viewing & Saving ----------

tk.Button(
    root,
    text="View All Expenses",
    width=35,
    command=view_all_expenses
).pack(pady=5)

tk.Button(
    root,
    text="View Basic Reports",
    width=35,
    command=view_basic_reports
).pack(pady=5)

tk.Button(
    root,
    text="Save Monthly Report (CSV)",
    width=35,
    command=save_monthly_report
).pack(pady=5)


tk.Button(
    root,
    text="Exit",
    width=35,
    command=root.quit
).pack(pady=15)


root.mainloop()
