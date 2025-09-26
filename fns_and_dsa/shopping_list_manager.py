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
        choice = input("Enter your choice: ") #Promt for picking an item from menu

        if choice == '1':
            item = input("Enter the item to add: ") 
            shopping_list.append(item) # Prompt for and add an item
            pass
        elif choice == '2':
            remove_item = input("Enter name of item you want to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item) # Prompt for and remove an item
            else:
                print("Item not found in list.") # Displays if an item to remove is not in list.
            pass
        elif choice == '3':
            print(shopping_list) # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()