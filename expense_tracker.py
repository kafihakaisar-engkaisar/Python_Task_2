import csv
os_file = "expenses.csv"

def add_expense():
    desc = input("Enter expense description (e.g., Coffee, Snacks): ")
    amount = input("Enter amount: ")
    
    with open(os_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])
    print(" Expense added successfully!\n")

def view_expenses():
    try:
        print("\n--- All Expenses ---")
        with open(os_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    print(f"Item: {row[0]}, Amount: ₹{row[1]}")
        print("-" * 20 + "\n")
    except FileNotFoundError:
        print("No expenses recorded yet.\n")

def total_expenses():
    total = 0
    try:
        with open(os_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    total += int(row[1])
        print(f"\n Total Expenses: ₹{total}\n")
    except FileNotFoundError:
        print("No expenses recorded yet.\n")

# Main menu loop for CLI application
def main():
    while True:
        print("=== Expense Tracker Menu ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()