import csv
import os

FILENAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel, Shopping): ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Please enter a valid number.")
        return
        
    description = input("Enter description (optional): ")
    
    with open(FILENAME, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])
        
    print("Expense added successfully!")

def view_expenses():
    print("\n--- All Expenses ---")
    if not os.path.exists(FILENAME):
        print("No expense records found.")
        return
        
    with open(FILENAME, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
        
        if len(data) <= 1:
            print("Expense file is empty.")
            return
            
        for row in data:
            print(f"{row[0]} | {row[1]} | Rs.{row[2]} | {row[3]}")

def category_summary():
    print("\n--- Category Summary Statistics ---")
    if not os.path.exists(FILENAME):
        print("No data available.")
        return
        
    summary = {}
    total_spent = 0.0
    
    with open(FILENAME, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        
        for row in reader:
            if len(row) < 3:
                continue
            category = row[1]
            try:
                amount = float(row[2])
            except ValueError:
                continue
                
            summary[category] = summary.get(category, 0.0) + amount
            total_spent += amount
            
    if not summary:
        print("No summary data available.")
        return
        
    print(f"Total Expenditure: Rs. {total_spent:.2f}\n")
    print("Category-wise Breakdown:")
    for cat, amt in summary.items():
        print(f"- {cat}: Rs. {amt:.2f}")

def main():
    initialize_file()
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category Summary Statistics")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()