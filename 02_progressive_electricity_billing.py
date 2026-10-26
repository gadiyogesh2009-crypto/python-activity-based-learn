# Assignment 2: Progressive Electricity Billing

def calculate_bill(units):
    if units < 0:
        raise ValueError("Units cannot be negative.")

    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = 100 * 2 + (units - 100) * 3
    else:
        energy_charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed_charge = 50
    subtotal = energy_charge + fixed_charge
    surcharge = subtotal * 0.05
    rebate = 20 if units < 100 else 0
    total = subtotal + surcharge - rebate
    return total


months = int(input("Enter number of months to compare: "))
bills = []

for month in range(1, months + 1):
    units = float(input(f"Enter units used in month {month}: "))
    bill = calculate_bill(units)
    bills.append((month, units, bill))
    print(f"Month {month} bill: Rs. {bill:.2f}")

print("\n--- Bill Comparison ---")
for i in range(1, len(bills)):
    previous_bill = bills[i - 1][2]
    current_bill = bills[i][2]

    if previous_bill > 0:
        increase = ((current_bill - previous_bill) / previous_bill) * 100
        if increase > 30:
            print(
                f"Alert: Month {bills[i][0]} bill increased by "
                f"{increase:.2f}% compared with the previous month."
            )

if bills:
    highest = max(bills, key=lambda item: item[2])
    print(f"Highest bill: Month {highest[0]} (Rs. {highest[2]:.2f})")
