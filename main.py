import sqlite3
from datetime import datetime

def add_expense(date, category, amount, description):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
    """, (date, category, amount, description))
    conn.commit()
    conn.close()
    print("Expense added successfully!")


def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print("\nYour Expenses:\n")
        for row in rows:
            print(f"ID: {row[0]}, Date: {row[1]}, Category: {row[2]}, Amount: ${row[3]}, Description: {row[4]}")
    else:
        print("\nNo expenses found.")


if __name__ == "__main__":
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            date = datetime.now().strftime("%Y-%m-%d")
            category = input("Enter expense category (e.g. Food, Rent): ")
            amount = float(input("Enter amount: "))
            description = input("Enter a short description: ")
            add_expense(date, category, amount, description)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
