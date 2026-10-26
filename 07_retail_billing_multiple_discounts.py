# Assignment 7: Retail Billing with Multiple Discount Rules

item_count = int(input("Enter number of items: "))
if item_count <= 0:
    print("Error: Number of items must be positive.")
else:
    subtotal = 0
    for i in range(1, item_count + 1):
        print(f"\nItem {i}")
        item_name = input("Enter item name: ")
        category = input("Enter category (electronics/other): ").strip().lower()
        unit_price = float(input("Enter unit price (Rs.): "))
        quantity = int(input("Enter quantity: "))

        if unit_price < 0 or quantity < 0:
            print("Invalid price or quantity; item skipped.")
            continue

        subtotal += unit_price * quantity

    discount = min(subtotal * 0.10, 1000) if subtotal >= 5000 else 0
    taxable_amount = subtotal - discount
    tax_rate = 0.18  # default tax rate
    tax = taxable_amount * tax_rate
    total = taxable_amount + tax

    print("\n--- Retail Bill ---")
    print(f"Subtotal: Rs. {subtotal:.2f}")
    print(f"Discount: Rs. {discount:.2f}")
    print(f"Tax (18%): Rs. {tax:.2f}")
    print(f"Final amount: Rs. {total:.2f}")
