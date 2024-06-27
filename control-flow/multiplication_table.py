#taking user inputs
number = int(input(f'Enter a number to see its multiplication table: '))

# Generate and Print the Multiplication Table
for i in range(1 ,10+1):
    product = number * i
    print(f'{number} * {i} = {product}')