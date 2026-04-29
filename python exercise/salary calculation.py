def calculate_salary(basic_salary):
    hra = basic_salary * 0.20   # 20% HRA
    da = basic_salary * 0.10    # 10% DA
    ta = basic_salary * 0.05    # 5% TA

    gross_salary = basic_salary + hra + da + ta

    pf = basic_salary * 0.12    # 12% PF
    tax = basic_salary * 0.05   # 5% Tax

    total_deduction = pf + tax
    net_salary = gross_salary - total_deduction

    return gross_salary, total_deduction, net_salary


print("Salary Calculation")
basic = float(input("Enter basic salary: "))

gross, deduction, net = calculate_salary(basic)

print("\nSalary Details")
print("Basic Salary:", basic)
print("Gross Salary:", gross)
print("Total Deduction:", deduction)
print("Net Salary:", net)