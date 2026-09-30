import csv # To work with CSV files.
import os # To check the file.

from decimal import Decimal, InvalidOperation # It is used for precise numbers.
from datetime import datetime # To import date from python modules.
# Saving Incomes, Expenses and Budgets in data file without being erased.
INCOME_FILE = "data/income.csv"
EXPENSE_FILE = "data/expense.csv"
BUDGET_FILE = "data/budgets.csv"

# Store income records in a list.
# Here used list to save records after together one by one.
# Each income record will be saved as a dictionary.
income_records = []

# Each expense record will be saved as a dictionary.
expense_records = []

# Each budgets will be saved as a dictionary.
# Here I put budgets as a dictionary to find budgets with a specific key.
budgets = {}

# Functions and their usage in the program.
def get_valid_amount():
    while True:
        # strip() removes the leading and trailing whitespace from the string.
        amount_input = input("Enter amount: ").strip()

        try: # <-It executes the code; if the program crashes, it proceeds to the `except` block.
            amount = Decimal(amount_input)

            # Reject NaN and Infinity
            if not amount.is_finite(): # is_finite Returns Finite number
                print("Amount must be a finite number.")
                continue

            # Amount must be greater than zero
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            # Amount can have maximum 2 decimal places
            if amount.as_tuple().exponent < -2: # as_tuple() shows the internal structure of the decimal.
                print("Amount can have maximum 2 decimal places.")
                continue

            return amount

        except InvalidOperation:
            print("Please enter a valid number.")

def get_valid_date(): # Get a valid date in YYYY-MM-DD format
    while True:
        # Ask the user to enter a date
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            # Convert the input string into a real date object with strptime()
            datetime.strptime(date, "%Y-%m-%d")
            # Return the valid date string
            return date
        except ValueError:
            # Display an error if the date is invalid
            print("Invalid date. Please use YYYY-MM-DD.")

def get_valid_month():

    while True:
        # Ask the user to enter a year and month.
        month = input("Enter month (YYYY-MM): ")

        try:
            # Check whether the input has exactly 7 characters.
            if len(month) != 7:
                print("Invalid format. Please use YYYY-MM.")
                continue
            # Check whether the year and month contain digits.
            if not (month[:4].isdigit() and month[5:7].isdigit()):
                print("Invalid format. Please use YYYY-MM.")
                continue
            # Check whether the date is a valid year and month.
            datetime.strptime(month, "%Y-%m")
            # Return the valid month.
            return month

        except ValueError:
            print("Invalid month. Please enter a valid month.")

def view_records_by_month():
# Display income and expense records for a specific month.
    #  Ask the user to enter the year and month.
    month = get_valid_month()
    # Display income records for the selected month.
    print("\n===== Income Records =====")

    found_income = False

    for income in income_records:
        # Extract the year and month from the income date.
        income_month = income["date"][:7]

        if income_month == month:
            print(f"\nID: {income['id']}")
            print(f"Amount: {income['amount']}")
            print(f"source: {income["source"]}")
            print(f"Date: {income['date']}")

            found_income = True


    # Display a message if no income was found.
    if not found_income:
        print("\nNo income records found for this month.")

    # Display expense records for the selected month.
    print("\n===== Expense Records =====")

    found_expense = False

    for expense in expense_records:
        # Extract the year and month from the expense date.
        expense_month = expense["date"][:7]

        if expense_month == month:
            print(f"\nID: {expense['id']}")
            print(f"Amount: {expense['amount']}")
            print(f"Category: {expense["category"]}")
            print(f"Date: {expense['date']}")

            found_expense = True

    # Display a message if no expense was found.
    if not found_expense:
        print("\nNo expense records found for this month.")

def monthly_report():


    # Ask the user to enter a valid month.
    month = get_valid_month()

    # Initialize the monthly totals.
    total_income = Decimal("0")
    total_expenses = Decimal("0")

    # Calculate income for the selected month.
    for income in income_records:

        # Extract the year and month from the income date.
        income_month = income["date"][:7]

        # Add the income amount if it belongs to the selected month.
        if income_month == month:
                total_income += Decimal(str(income["amount"]))

    # Calculate expenses for the selected month.
    for expense in expense_records:

        # Extract the year and month from the expense date.
        expense_month = expense["date"][:7]

        # Add the expense amount if it belongs to the selected month.
        if expense_month == month:
            total_expenses += Decimal(str(expense["amount"]))

    # Calculate the monthly balance.
    balance = total_income - total_expenses

    # Display the monthly financial report.
    print(f"\n===== Financial Report: {month} =====")
    print(f"Total Income: {total_income:.2f}")
    print(f"Total Expenses: {total_expenses:.2f}")
    print(f"Balance: {balance:.2f}")

def set_budget():
    # Get a valid month.
    month = get_valid_month()
    # Get the expense category.
    category = get_non_empty_text("Enter category: ")
    # Get the budget amount.
    amount = get_valid_amount()
    # Create a unique key using month and category.
    key = (month, category.lower())
    # Save the budget.
    budgets[key] = amount
    save_budgets()

    print("Budget saved successfully.")

def view_budgets():
    # Display all saved budgets.

    # Check if there are no budgets.
    if not budgets:
        print("No budgets found.")
        return

    print("\n===== Budgets =====")

    # Display each saved budget.
    for (month, category), amount in budgets.items():
        print(f"Month: {month}")
        print(f"Category: {category}")
        print(f"Budget: {amount:.2f}")
        print("-" * 19)

def compare_budget():
    # Compare actual expenses with budgets for a specific month.

    # Get a valid month.
    month = get_valid_month()

    # Store total expenses for each category.
    category_expenses = {}

    # Calculate expenses for the selected month.
    for expense in expense_records:
        if expense["date"][:7] == month:
            category = expense["category"].lower()
            amount = Decimal(str(expense["amount"]))

            # Add the expense to the category total.
            category_expenses[category] = (
                category_expenses.get(category, Decimal("0")) + amount
            )

    print(f"\n===== Budget Comparison: {month} =====")

    # Check whether a budget exists for the selected month.
    found_budget = False

    # Compare each budget with actual expenses.
    for (budget_month, category), budget_amount in budgets.items():
        if budget_month == month:
            found_budget = True

            actual = category_expenses.get(category, Decimal("0"))
            difference = budget_amount - actual

            print(f"Category: {category}")
            print(f"Budget: {budget_amount:.2f}")
            print(f"Actual Expenses: {actual:.2f}")
            print(f"Remaining: {difference:.2f}")
            print("-" * 38)

    # Display a message if no budget exists for this month.
    if not found_budget:
        print(f"   No budget found for this month.")

def edit_transaction():
    # Edit an existing income or expense transaction by ID.

    # Ask for the transaction ID.
    transaction_id = input("Enter transaction ID: ")

    # Search for the transaction in income records.
    for income in income_records:
        if str(income["id"]) == transaction_id:
            amount = get_valid_amount()
            source = get_non_empty_text("Enter source: ")
            date = get_valid_date()

            # Update the income record.
            income["amount"] = amount
            income["source"] = source
            income["date"] = date

            # Save the updated records.
            save_income_records()

            print("Income transaction updated successfully.")
            return

    # Search for the transaction in expense records.
    for expense in expense_records:
        if str(expense["id"]) == transaction_id:
            amount = get_valid_amount()
            category = get_non_empty_text("Enter category: ")
            date = get_valid_date()

            # Update the expense record.
            expense["amount"] = amount
            expense["category"] = category
            expense["date"] = date

            # Save the updated records.
            save_expense_records()

            print("Expense transaction updated successfully.")
            return

    # Show an error if the ID does not exist.
    print("Transaction ID not found.")

def delete_transaction():
    # Delete an income or expense transaction by ID.

    # Ask for the transaction ID.
    transaction_id = input("Enter transaction ID: ")

    # Search for the transaction in income records.
    for income in income_records:
        if str(income["id"]) == transaction_id:
            income_records.remove(income)

            # Save the updated income records.
            save_income_records()

            print("Income transaction deleted successfully.")
            return

    # Search for the transaction in expense records.
    for expense in expense_records:
        if str(expense["id"]) == transaction_id:
            expense_records.remove(expense)

            # Save the updated expense records.
            save_expense_records()

            print("Expense transaction deleted successfully.")
            return

    # Show an error if the ID does not exist.
    print("Transaction ID not found.")

def backup_data():
    # Create a backup of income and expense CSV files.

    # Create the backup folder if it does not exist.
    os.makedirs("backup", exist_ok=True)

    # Copy the income file if it exists.
    if os.path.exists(INCOME_FILE):
        with open(INCOME_FILE, "r", encoding="utf-8") as source:
            data = source.read()

        with open("backup/income_backup.csv", "w", encoding="utf-8") as target:
            target.write(data)

    # Copy the expense file if it exists.
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r", encoding="utf-8") as source:
            data = source.read()

        with open("backup/expenses_backup.csv", "w", encoding="utf-8") as target:
            target.write(data)

    print("Backup created successfully.")

def get_non_empty_text(prompt): # Get non empty text from the user
    while True:
        # Ask the user to enter some text
        text = input(prompt)
        # Remove extra spaces from the beginning and end
        text = text.strip()
        # Check wether the input is empty
        if text:
            return text
        else:
            print("Input cannot be empty. Please try again.")

def get_next_id():
    # Generate the next unique transaction ID.

    # Collect all existing transaction IDs.
    ids = []

    for income in income_records:
        if "id" in income:
            ids.append(int(income["id"]))

    for expense in expense_records:
        if "id" in expense:
            ids.append(int(expense["id"]))

    # Return the next available ID.
    if ids:
        return max(ids) + 1

    return 1

def add_income():
    # Get income details from user.
    amount = get_valid_amount()
    source = get_non_empty_text("Enter income source: ")
    date = get_valid_date()

    # Create a unique transaction ID.
    transaction_id = get_next_id()

    # Create the income record.
    income = {
        "id": transaction_id,
        "amount": amount,
        "source": source,
        "date": date
    }

    # Add the income record to the list.
    income_records.append(income)

    # Save the updated income records.
    save_income_records()

    print("Income added successfully")

def add_expense():
    # Get expense information.
    amount = get_valid_amount()
    category = get_non_empty_text("Enter expense category: ")
    date = get_valid_date()

    # Create a unique transaction ID.
    transaction_id = get_next_id()

    # Create the expense record.
    expense = {
        "id": transaction_id,
        "amount": amount,
        "category": category,
        "date": date
    }

    # Add the expense record to the list.
    expense_records.append(expense)

    # Save the updated expense records.
    save_expense_records()

    print("Expense added successfully")

def show_income():
    print("\n===== Income Records =====")

    if income_records:
        for index, income in enumerate(income_records, start=1):
            print(f"\nIncome #{index}")
            print(f"ID: {income['id']}")
            print(f"Amount: {income['amount']}")
            print(f"source: {income['source']}")
            print(f"Date: {income['date']}")
    else:
        print("No income records found.")

def show_expense():
    print("\n===== Expense Records =====")

    if expense_records:
        for index, expense in enumerate(expense_records, start=1):
            print(f"\nExpense #{index}")
            print(f"ID: {expense['id']}")
            print(f"Amount: {expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"Date: {expense['date']}")
    else:
        print("No expense records found.")

def view_all_records():
    # Display all records or income records or expense records
    # Show the available viewing options
    print("\n===== View Records =====")
    print("1. View Income Records")
    print("2. View Expense Records")
    print("3. View All Records")
    print("4. View Records by Month")
    # Get the user's choice
    choice = input("Choose an option: ")

    # Display income records if the user chooses 1
    if choice == "1":
        # Display all income records
        show_income()

    elif choice == "2":
        # Display all expense records
        show_expense()
    elif choice == "3": # Display both types of records if the user chooses 3
        show_income()
        show_expense()
    elif choice == "4": # Display records for a specific month.
        view_records_by_month()
    else:
        print("Invalid choice. Please choose 1, 2, 3 or 4.")

def view_summary():
    # Calculate total income and total expenses
    total_income = sum(
        (Decimal(str(record["amount"])) for record in income_records),
        Decimal("0")
    )

    total_expense = sum(
        (Decimal(str(record["amount"])) for record in expense_records),
        Decimal("0")
    )

    # Calculate balance
    balance = total_income - total_expense

    print("\n--- Financial Summary ---")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Balance: {balance}")

def save_income_records():
    # Save all income records to the CSV file.

    with open(INCOME_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "amount", "source", "date"]
        )

        writer.writeheader()
        writer.writerows(income_records)

def save_expense_records():
    # Save all expense records to the CSV file.

    with open(EXPENSE_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "amount", "category", "date"]
        )

        writer.writeheader()
        writer.writerows(expense_records)

def save_budgets():
    # Save all budgets to the CSV file.

    with open(BUDGET_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["month", "category", "amount"])

        for (month, category), amount in budgets.items():
            writer.writerow([month, category, amount])

def load_budgets():
    # Load budgets from the CSV file safely.

    if not os.path.exists(BUDGET_FILE):
        return

    try:
        with open(BUDGET_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    month = row["month"]
                    category = row["category"].lower()
                    amount = Decimal(str(row["amount"]))

                    budgets[(month, category)] = amount

                except (KeyError, ValueError, InvalidOperation):
                    print("Warning: A corrupted budget record was skipped.")

    except (OSError, csv.Error):
        print("Warning: Budget file could not be read.")

def load_income_records():
    # Load income records from the CSV file safely.

    if not os.path.exists(INCOME_FILE):
        return

    try:
        with open(INCOME_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    # Support old records without an ID.
                    if "id" not in row or not row["id"]:
                        row["id"] = get_next_id()
                    else:
                        row["id"] = int(row["id"])

                    row["amount"] = Decimal(str(row["amount"]))

                    # Convert old "sourse" key to "source".
                    if "sourse" in row:
                        row["source"] = row["sourse"]
                        del row["sourse"]

                    income_records.append(row)

                except (KeyError, ValueError, InvalidOperation):
                    print("Warning: A corrupted income record was skipped.")

    except (OSError, csv.Error):
        print("Warning: Income file could not be read.")

def load_expense_records():
    # Load expense records from the CSV file safely.

    if not os.path.exists(EXPENSE_FILE):
        return

    try:
        with open(EXPENSE_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    # Support old records without an ID.
                    if "id" not in row or not row["id"]:
                        row["id"] = get_next_id()

                    else:
                        row["id"] = int(row["id"])

                    row["amount"] = Decimal(str(row["amount"]))
                    expense_records.append(row)

                except (KeyError, ValueError, InvalidOperation):
                    print("Warning: A corrupted expense record was skipped.")

    except (OSError, csv.Error):
        print("Warning: Expense file could not be read.")

# Load previously saved records when the program starts
load_income_records()
load_expense_records()
load_budgets()
# Main program loop
def main():
    while True:
        # Display the application title.
        print("\n================================")
        print("    Personal finance tracker    ")
        print("================================")

        # Display the available menu options.
        print("1. Add Income") # Add a new income record.
        print("2. Add Expense") # Add a new expense record.
        print("3. View Records") # View saved income and expense records.
        print("4. Generate Reports") # Display the overall financial summary.
        print("5. Monthly Report") # Display the financial report for a specific month.
        print("6. Set Budget") # Set a budget for a category and month.
        print("7. View Budgets") # Display all saved budgets.
        print("8. Compare Budgets") # Compare budgets with actual expenses.
        print("9. Edit Transaction") # Edit an existing transaction with ID.
        print("10. Delete Transaction") # Delete an existing transaction with ID.
        print("11. Backup Data") # Create a backup of financial data
        print("12. Exit") # Exit the application

        # Get the user's choice
        choice = input("Choose an option (1-12):")

        # Check which option the user selected.
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_all_records()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            monthly_report()
        elif choice == "6":
            set_budget()
        elif choice == "7":
            view_budgets()
        elif choice == "8":
            compare_budget()
        elif choice == "9":
            edit_transaction()
        elif choice == "10":
            delete_transaction()
        elif choice == "11":
            backup_data()
        elif choice == "12":
            print("Goodbye!")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. please enter a number from 1 to 12")


if __name__ == "__main__":
    main()