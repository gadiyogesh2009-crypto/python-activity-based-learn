# Assignment 10: Campus Event Financial Planning
import math

venue_cost = float(input("Enter venue cost (Rs.): "))
equipment_cost = float(input("Enter equipment cost (Rs.): "))
transport_cost = float(input("Enter transport cost (Rs.): "))
catering_per_person = float(input("Enter catering cost per person (Rs.): "))
certificate_per_person = float(input("Enter certificate cost per person (Rs.): "))
sponsorship = float(input("Enter sponsorship amount (Rs.): "))
registration_fee = float(input("Enter registration fee per participant (Rs.): "))
participants = int(input("Enter expected number of participants: "))

values = [
    venue_cost, equipment_cost, transport_cost, catering_per_person,
    certificate_per_person, sponsorship, registration_fee
]

if min(values) < 0 or participants < 0:
    print("Error: Costs, sponsorship, fee, and participants cannot be negative.")
else:
    fixed_cost = venue_cost + equipment_cost + transport_cost
    variable_cost_per_person = catering_per_person + certificate_per_person
    total_cost = fixed_cost + variable_cost_per_person * participants
    registration_income = registration_fee * participants
    total_income = registration_income + sponsorship
    balance = total_income - total_cost

    print("\n--- Event Financial Summary ---")
    print(f"Fixed costs: Rs. {fixed_cost:.2f}")
    print(f"Variable cost per participant: Rs. {variable_cost_per_person:.2f}")
    print(f"Total cost: Rs. {total_cost:.2f}")
    print(f"Total income: Rs. {total_income:.2f}")
    print(f"Surplus/Deficit: Rs. {balance:.2f}")

    contribution_per_person = registration_fee - variable_cost_per_person
    if contribution_per_person > 0:
        break_even = max(0, math.ceil((fixed_cost - sponsorship) / contribution_per_person))
        print(f"Break-even participants: {break_even}")
    else:
        print("Break-even cannot be reached with the current registration fee.")
