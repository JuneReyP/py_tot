hrsRender = int(input("Enter number of hours rendered: "))
perHr = float(input("Enter rate per hour: "))
gsis = float(input("GSIS Premium: "))
philH = float(input("PhilHealth: "))
housing = float(input("Housing Loan: "))
tax = float(input("Tax rate: "))

gross = hrsRender * perHr
deduction = gsis + philH + housing
net = tax/100
total = gross - (gross*net) - deduction

print(f"Gross Salary: {gross}")
print(f"Total deductions: {deduction}")
print(f"Net Salary: {total}")