# Assignment 4: Employee Payroll and Deduction Analysis

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary (Rs.): "))
overtime_hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentive amount (Rs.): "))

if min(basic_salary, overtime_hours, incentive) < 0:
    print("Error: Salary, overtime, and incentive cannot be negative.")
else:
    hra = basic_salary * 0.20
    allowance = basic_salary * 0.10
    overtime_pay = overtime_hours * 200
    gross_salary = basic_salary + hra + allowance + overtime_pay + incentive

    deduction_rate = 0.05 if gross_salary <= 30000 else 0.10
    deduction = gross_salary * deduction_rate
    net_salary = gross_salary - deduction

    print("\n--- Payroll Details ---")
    print(f"Employee: {employee_name}")
    print(f"HRA: Rs. {hra:.2f}")
    print(f"Allowance: Rs. {allowance:.2f}")
    print(f"Overtime pay: Rs. {overtime_pay:.2f}")
    print(f"Gross salary: Rs. {gross_salary:.2f}")
    print(f"Deduction ({deduction_rate * 100:.0f}%): Rs. {deduction:.2f}")
    print(f"Net salary: Rs. {net_salary:.2f}")
