# Assignment 5: Multi-Plan Telecommunications Cost Optimization

plans = {
    "A": {"price": 199, "daily_data_gb": 2, "validity_days": 28},
    "B": {"price": 299, "daily_data_gb": 3, "validity_days": 28},
    "C": {"price": 399, "daily_data_gb": 2, "validity_days": 56},
}

required_days = int(input("Enter required validity in days: "))
daily_data_needed = float(input("Enter required data per day (GB): "))
budget = float(input("Enter maximum budget (Rs.): "))

if required_days <= 0 or daily_data_needed < 0 or budget < 0:
    print("Error: Enter positive validity and non-negative data/budget.")
else:
    suitable_plans = []

    for name, plan in plans.items():
        extra_data_gb = max(0, daily_data_needed - plan["daily_data_gb"])
        extra_cost = extra_data_gb * 20 * required_days
        total_cost = plan["price"] + extra_cost

        if plan["validity_days"] >= required_days and total_cost <= budget:
            suitable_plans.append((total_cost, name, plan, extra_data_gb))

    if suitable_plans:
        suitable_plans.sort(key=lambda item: item[0])
        cost, name, plan, extra_data = suitable_plans[0]
        print("\n--- Recommended Plan ---")
        print(f"Plan: {name}")
        print(f"Base price: Rs. {plan['price']:.2f}")
        print(f"Validity: {plan['validity_days']} days")
        print(f"Daily data: {plan['daily_data_gb']} GB")
        print(f"Estimated extra data per day: {extra_data:.2f} GB")
        print(f"Estimated total cost: Rs. {cost:.2f}")
    else:
        print("No plan matches all your requirements and budget.")
