# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assume a simple annual interest rate of 5%
interest_rate = 0.05

# Calculate the projected savings after one year, incorporating the interest
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * interest_rate)

# Output the results
print(f"Your monthly savings are: {monthly_savings:.2f}")
print(f"Your projected annual savings after including interest are: {projected_annual_savings:.2f}")
