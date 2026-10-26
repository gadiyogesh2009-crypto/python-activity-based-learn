# Assignment 9: Multi-Currency Travel Budget Analysis

budget_inr = float(input("Enter total travel budget in INR: "))
expense_count = int(input("Enter number of expenses: "))
expenses = {}

if budget_inr < 0 or expense_count < 0:
    print("Error: Budget and expense count cannot be negative.")
else:
    for i in range(1, expense_count + 1):
        category = input(f"\nExpense {i} category (food/hotel/transport/other): ").strip().lower()
        amount_foreign = float(input("Enter expense amount in foreign currency: "))
        exchange_rate = float(input("Enter INR value for 1 unit of that currency: "))

        if amount_foreign < 0 or exchange_rate <= 0:
            print("Invalid amount or exchange rate; expense skipped.")
            continue

        amount_inr = amount_foreign * exchange_rate
        fee = amount_inr * 0.02
        total_inr = amount_inr + fee
        expenses[category] = expenses.get(category, 0) + total_inr
        print(f"Expense including 2% fee: Rs. {total_inr:.2f}")

    total_spent = sum(expenses.values())
    print("\n--- Travel Budget Summary ---")
    print(f"Total spent: Rs. {total_spent:.2f}")
    print(f"Remaining budget: Rs. {budget_inr - total_spent:.2f}")

    if total_spent > budget_inr:
        print("Warning: Travel budget exceeded.")
    else:
        print("Travel budget is within the limit.")

    if expenses:
        largest_category = max(expenses, key=expenses.get)
        print(f"Largest expense category: {largest_category} (Rs. {expenses[largest_category]:.2f})")
