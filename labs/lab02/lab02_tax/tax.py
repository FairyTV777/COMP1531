

income = int(input("Enter your income: "))
tax = None

if income >= 0 and income <= 18200:
    tax = 0
elif income <= 37000:
    tax = 0.19 * (income - 18200)
elif income <= 87000:
    tax = 3572 + 0.325 * (income - 37000)
elif income <= 180000:
    tax = 19822 + 0.37 * (income - 87000)
else:
    tax = 54232 + 0.45 * (income - 180000)

tax = "{:,.2f}".format(tax)

print("The estimated tax on your income is $" + tax)
