import sqlite3
import pandas as pd
from tabulate import tabulate

# Load data from database
def load_expenses():
    conn = sqlite3.connect("finance.db")
    df = pd.read_sql_query(
        "SELECT date, category, amount FROM expenses",
        conn
    )
    conn.close()
    return df


# Category-wise spending report
def category_wise_report(df):
    summary = (
        df.groupby("category")["amount"]
        .sum()
        .reset_index()
    )

    print("\nCategory-wise Spending:")
    print(tabulate(summary, headers="keys", tablefmt="grid"))


# Monthly total spending report (print)
def monthly_total_report(df):
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    monthly = (
        df.groupby("month")["amount"]
        .sum()
        .reset_index()
    )

    print("\nMonthly Spending:")
    print(tabulate(monthly, headers="keys", tablefmt="grid"))


# Highest spending category
def highest_spending_category(df):
    summary = df.groupby("category")["amount"].sum()
    highest = summary.idxmax()

    print(f"\nHighest Spending Category: {highest}")


# Date-range expense report
def date_range_report(df):
    start_date = input("\nEnter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    df["date"] = pd.to_datetime(df["date"])

    filtered = df[
        (df["date"] >= start_date) &
        (df["date"] <= end_date)
    ]

    if filtered.empty:
        print("\nNo expenses found in this date range.")
        return

    total = filtered["amount"].sum()

    print(f"\nTotal expense from {start_date} to {end_date}: {total}")

    category_summary = (
        filtered.groupby("category")["amount"]
        .sum()
        .reset_index()
    )

    print("\nCategory-wise breakdown:")
    print(tabulate(category_summary, headers="keys", tablefmt="grid"))


# Save monthly report to CSV
def save_monthly_report(df):
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    monthly = (
        df.groupby("month")["amount"]
        .sum()
        .reset_index()
    )

    monthly.to_csv("monthly_report.csv", index=False)

    print("\nMonthly report saved as 'monthly_report.csv'")


# Main execution
if __name__ == "__main__":
    df = load_expenses()

    category_wise_report(df)
    monthly_total_report(df)
    highest_spending_category(df)

    date_range_report(df)
    save_monthly_report(df)
