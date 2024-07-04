def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list")
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to add: ")
            #check if provided item already exits in the shopping list before action
            if item in shopping_list:
                 shopping_list.remove(item)
                 print(f"{item} has been removed from the shopping list")
            else:
                 print(f"{item} not found in the list")
                 pass
        elif choice == '3':
            # Display the shopping list
            # Check if item is not empty 
            print("Shopping list: ")
            if not shopping_list:
                print(f"The list is currently empty.")
            else:
                for i, item in enumerate(shopping_list, start= 1):
                    print(f"{i}. {item}")
                    pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()