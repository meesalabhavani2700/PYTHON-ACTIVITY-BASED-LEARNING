basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))

gross = basic + allowances

if gross <= 20000:
    deduction = 0
elif gross <= 40000:
    deduction = (gross - 20000) * 0.05
else:
    deduction = 1000 + (gross - 40000) * 0.10

net = gross - deduction

print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)