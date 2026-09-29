from typing import cast
income_records = []

expense_records = []


def view_all_records(): # Display all records or income records or expense records
    # Show the available viewing options
    print("\n===== View Records =====")
    print("1. View Income Records")
    print("2. View Expense Records")
    print("3. View All Records")
    # Get the user's choice
    choice = input("Choose an option: ")

    # Display income records if the user chooses 1
    if choice == "1":
        print("\n===== Income Records =====")
        if income_records:
            for index, income in enumerate(income_records, start = 1):

                # Display the income information
                print(f"\nIncome #{index}")
                print(f"Amount: {income['amount']}")
                print(f"Sourse: {income['sourse']}")
                print(f"Date: {income['date']}")
        else:
            print("No income records found.")

    elif choice == "2":
        # Display all expense records
        print("\n===== Expense Records =====")
        if expense_records:
            for index, expense in enumerate(expense_records, start = 1):
                print(f"\nExpense #{index}")
                print(f"Amount: {expense['amount']}")
                print(f"Category: {expense['category']}")
                print(f"Date: {expense['date']}")
        else:
            print("No expense records found.")
    elif choice == "3": # Display both types of records if the user chooses 3
        print("\n===== Income Records =====")
        if income_records:
            for index, income in enumerate(income_records, start=1):
                # Display the income information
                print(f"\nIncome #{index}")
                print(f"Amount: {income['amount']}")
                print(f"Sourse: {income['sourse']}")
                print(f"Date: {income['date']}")
        else:
            print("No income records found.")

         # Display all expense records
        print("\n===== Expense Records =====")
        if expense_records:
            for index, expense in enumerate(expense_records, start=1):
                    print(f"\nExpense #{index}")
                    print(f"Amount: {expense['amount']}")
                    print(f"Category: {expense['category']}")
                    print(f"Date: {expense['date']}")
        else:
                print("No expense records found.")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")















        # check which option the user selected
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":  # run the function to display all records
            view_all_records()
        elif choice == "4":  # Display the financial summary
            view_summary()
        elif choice == "5":
            print("5. Set Budget selected")
        elif choice == "6":
            print("6. Edit Transaction selected")
        elif choice == "7":
            print("7. Delete Transaction selected")
        elif choice == "8":
            print("8. Backup Data selected")
        elif choice == "9":
            print("9. Goodbye!")  # stop the loop and exit the application
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. please enter a number from 1 to 9")






            def load_income_records():  # Load income records from CSV file
                # Check if the income file exists
                if not os.path.exists(INCOME_FILE):
                    return
                # Open the income CSV file in read mode
                with open(INCOME_FILE, "r", newline="") as file:
                    # Create a CSV dictionary reader
                    reader = csv.DictReader(file)
                    # Read each row from the file
                    for row in reader:
                        # Add the row to the income records
                        income_records.append(row)









def load_expense_records(): # Load expense records from the CSV file
    # Check if the expense file exists
    if not os.path.exists(EXPENSE_FILE):
        return
    # Open the expense CSV file in read mode
    with open(EXPENSE_FILE, "r", newline="") as file:
        # Create a CSV dictionary reader
        reader =csv.DictReader(file)
        # Read each row from the file
        for row in reader:
            # Add the row to the expense records
            expense_records.append(row)