from datetime import datetime, timedelta
def display_current_datetime():
    """
    Function to display the current date and time
    """
    # Obtain the current date and time 
    current_datetime = datetime.now()

    # Save the current date in a variable
    current_date = current_datetime.date()

    # Print the current date and time in a readable format
    print("Current date and time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    
    return current_date

def calculate_future_date(days_to_add):
    """
    Function to calculate the future date after adding a specified number of days
    """
    # Obtain the current date
    current_date = datetime.now().date()

    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)

    # Print the future date in a readable format
    print("Future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))

    return future_date

def main():
    # Part 1: Display the Current Date and Time
    display_current_datetime()

    # Calculating a Future Date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)

    except ValueError:
        print("Please enter a valid integer for the number of days.")
        


