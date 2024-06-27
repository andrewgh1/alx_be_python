# match_case_calculator.py

# Prompt user for input
num1 =float(input("Enter the first number: "))
num2 =float(input("Enter the second number: "))

# Prompt user for operation choice
operation = input("Choose the operation (+, -, *, /): ")


# Perform calculation using match-case statement
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
    case _:
        print("Invalid operation selected.")

    
# Output the result
if operation == "/" and num2 != 0 :
    print(f"The result is {result:.2f}.")
elif operation in ["+", "-", "*"]:
    print(f"The result is {result}.")