# Prompt user for current age
current_age = int(input("How Old are you? "))

# Calculate age in 2050
future_year = 2050
current_year = 2023  # Assuming current year is 2023
years_until_future_year = future_year - current_year
age_in_future = current_age + years_until_future_year

# Print the result
print(f"In {future_year}, you will be {age_in_future} years old.")