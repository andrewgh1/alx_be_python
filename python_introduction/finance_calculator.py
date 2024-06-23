# Taking users monthly income and expense 
monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your total monthly expenses: "))

#Calculate monthly savings 
monthly_savings = monthly_income - monthly_expense

# project annual savings with a fixed interest rate of 5%
annual_interest_rate = 0.05
Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#print the results
print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(Projected_savings)}.")