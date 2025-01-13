#  Personal Finance Calculator

income =  int(input('Enter your Income '))
expenses = int(input("Enter your total monthly Expenses"))

monthly_savings = expenses - income

annual_interest = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest)

print(projected_savings)