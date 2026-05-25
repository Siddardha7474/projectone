import os

FILE_NAME = "expenses.txt"

def add_record(record_type):
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{record_type},{amount},{description}\n")

    print(f"{record_type} added successfully!\n")

def view_records():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    total_income = 0
    total_expense = 0

    print("\n===== Expense Tracker Records =====")

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

        if not records:
            print("No records available.\n")
            return

        for record in records:
            record_type, amount, description = record.strip().split(",")

            amount = float(amount)

            print(f"Type: {record_type} | Amount: ₹{amount} | Description: {description}")

            if record_type == "Income":
                total_income += amount
            else:
                total_expense += amount

    balance = total_income - total_expense

    print("\n===== Summary =====")
    print(f"Total Income  : ₹{total_income}")
    print(f"Total Expense : ₹{total_expense}")
    print(f"Balance       : ₹{balance}\n")

while True:
    print("===== Expense Tracker =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Records")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_record("Income")

    elif choice == "2":
        add_record("Expense")

    elif choice == "3":
        view_records()

    elif choice == "4":
        print("Exiting Expense Tracker...")
        break

    else:
        print("Invalid choice! Please try again.\n")