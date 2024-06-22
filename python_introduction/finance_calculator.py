# Taking users monthly income and expense 
monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total monthly expenses: "))

#Calculate monthly savings 
monthly_savings = monthly_income - monthly_expense

# project annual savings with a fixed interest rate of 5%
annual_interest_rate = 0.05
Projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate))

#print the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${Projected_savings}.")