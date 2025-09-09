income = int(input("Enter your monthly income: "))
expense = int(input("Enter your total monthly expenses: "))
saving = income - expense
rate = 0.05
projected_saving = (saving * 12) + (saving * rate * 12)
print("Your monthly savings are $", saving)
print("Projected savings after one year, with interest, is: $", projected_saving)
