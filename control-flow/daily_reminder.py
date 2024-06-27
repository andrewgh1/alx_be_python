#Taking inputs from user
task = input("Enter your task: ")
#Setting Priority levels
priority = input("Priority (high/medium/low): ").lower()
#Asking if its time bound or not
time_bound = input("Is it time-bound? (yes/no): ").lower()

#match case based on priority levels and if conditions for time_bound
match priority:
    case "high":
        reminder = f" '{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority level"


# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += f" that requires immediate attention today!"
else:
    reminder += f'. Consider completing it when you have free time.'

#provide the customized reminder    
print("Reminder: ", reminder)


    


