
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