# Assignment 8: Manufacturing Cost and Profitability Analysis

quantity = int(input("Enter number of units produced: "))
material_per_unit = float(input("Enter material cost per unit (Rs.): "))
labour_per_unit = float(input("Enter labour cost per unit (Rs.): "))
machine_per_unit = float(input("Enter machine cost per unit (Rs.): "))
wastage_percent = float(input("Enter material wastage percentage: "))
selling_price = float(input("Enter selling price per unit (Rs.): "))

if (
    quantity <= 0
    or min(material_per_unit, labour_per_unit, machine_per_unit, selling_price) < 0
    or not 0 <= wastage_percent <= 100
):
    print("Error: Check quantity, costs, selling price, and wastage percentage.")
else:
    wastage_cost = material_per_unit * wastage_percent / 100
    cost_per_unit = material_per_unit + wastage_cost + labour_per_unit + machine_per_unit
    total_cost = cost_per_unit * quantity
    revenue = selling_price * quantity
    profit = revenue - total_cost
    margin = (profit / total_cost * 100) if total_cost > 0 else 0

    print("\n--- Manufacturing Analysis ---")
    print(f"Cost per unit: Rs. {cost_per_unit:.2f}")
    print(f"Total production cost: Rs. {total_cost:.2f}")
    print(f"Total revenue: Rs. {revenue:.2f}")
    print(f"Profit/Loss: Rs. {profit:.2f}")
    print(f"Profit margin on cost: {margin:.2f}%")

    if margin >= 20:
        print("Target achieved: Profit margin is at least 20%.")
    else:
        print("Target not achieved: Profit margin is below 20%.")
