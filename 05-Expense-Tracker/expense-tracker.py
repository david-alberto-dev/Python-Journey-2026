"""
Mini-project #5: Expense Tracker
"""

expenses = []

def show_expenses():
    if not expenses:
        print("\nThere are no expenses.\n")
    else:
        print("\n--- 📋 YOUR EXPENSES ---")
        for index, expense in enumerate(expenses, start=1):
            print(f'{index}. {expense["item_name"]}, {expense["item_category"]}, {expense["item_price"]}')
            print("-" * 20)
        print(f"💰Remaining budget: {current_budget:.2f}\n")

while True:
    try:
        initial_budget = float(input("Please enter the initial budget: \n"))
    except ValueError:
        print("Please enter a number.")
        continue
    current_budget = initial_budget
    break

while True:
    print("""--- Expense Tracker ---
            1. View Expenses
            2. Add Expense
            3. Remove Expense
            4. Quit
                                    """)
    choice = input("Please enter your choice: ").strip()
    match choice:
        case "1":
            show_expenses()
        case "2":
            print("Alright, let's add a new expense.")
            item_name = input("Please enter the name of the item: ")
            item_category = input("Please enter the category of the item: ")
            try:
                item_price = float(input("Please enter the price of the item: "))
            except ValueError:
                print("Please enter a number.")
                continue
            new_expense = {
                "item_name": item_name,
                "item_category": item_category,
                "item_price": item_price
            }
            current_budget -= item_price
            expenses.append(new_expense)
            print("New expense added successfully!")
            continue
        case "3":
            if not expenses:
                print("\nThe expense list is empty, nothing to remove.")
                continue
            else:
                show_expenses()
                try:
                    index_to_remove = int(input("What would you like to remove? Enter the expense index: "))
                    if 1 <= index_to_remove <= len(expenses):
                        removed_item = expenses.pop(index_to_remove - 1)
                        current_budget += removed_item["item_price"]
                        print(f"Removed {removed_item['item_name']} successfully!")
                        print(f"Refunding {removed_item['item_price']} to your budget.")
                    else:
                        print(f"Please enter a number from 1 to {len(expenses)}.")
                except ValueError:
                    print("Please enter a number.")
                    continue
        case "4":
            confirmation = input("Are you sure you want to quit? (y/n): ").strip().lower()
            if confirmation == "y":
                print("Quitting...")
                break
        case _:
            print("Please enter a number from 1 to 4.")
            continue