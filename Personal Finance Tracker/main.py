from manual_entry import add_expense
from bank_csv_parser import import_bank_csv
import reports
import os

def show_menu():
    print("\n=== Personal Finance Tracker ===")
    print("1. Add expense manually")
    print("2. Import bank CSV")
    print("3. View all expenses")
    print("4. View basic reports")
    print("5. Date-range expense report")
    print("6. Save monthly report to CSV")
    print("7. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            path = input("Enter CSV file path: ")
            import_bank_csv(path)

        elif choice == "3":
            os.system("python view_expenses.py")

        elif choice == "4":
            df = reports.load_expenses()
            reports.category_wise_report(df)
            reports.monthly_total_report(df)
            reports.highest_spending_category(df)

        elif choice == "5":
            df = reports.load_expenses()
            reports.date_range_report(df)

        elif choice == "6":
            df = reports.load_expenses()
            reports.save_monthly_report(df)

        elif choice == "7":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
 