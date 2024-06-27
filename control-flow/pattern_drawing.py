#Taking user inputs
size = int(input("Enter the size of the pattern: "))

#initializing a row variable to use for the while loop
row = 0

#while loop and nested for loop
while row < size :
    for _ in range(size):
        print("*", end="")
    print() #to print a newline after each window
    #increment
    row += 1
