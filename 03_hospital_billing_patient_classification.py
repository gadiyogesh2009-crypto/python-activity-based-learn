# Assignment 3: Hospital Billing and Patient Classification

consultation = float(input("Enter consultation charges (Rs.): "))
diagnostics = float(input("Enter diagnostic charges (Rs.): "))
treatment = float(input("Enter treatment charges (Rs.): "))

if min(consultation, diagnostics, treatment) < 0:
    print("Error: Charges cannot be negative.")
else:
    subtotal = consultation + diagnostics + treatment
    discount = subtotal * 0.10 if subtotal >= 5000 else 0
    final_bill = subtotal - discount

    if final_bill < 2000:
        category = "Basic"
    elif final_bill < 10000:
        category = "Standard"
    else:
        category = "High"

    print("\n--- Hospital Bill ---")
    print(f"Subtotal: Rs. {subtotal:.2f}")
    print(f"Discount: Rs. {discount:.2f}")
    print(f"Final bill: Rs. {final_bill:.2f}")
    print(f"Patient classification: {category}")
