# System packages
import os.path 

# External packages

# Imports of our own fucntiones
from menu_functions import add_results, remove_results, mark_results, view_results

print("Welcome to the Water Testing application")
print("\n")

def create_menu(): # Function #1 
    print("1. Enter 1 to add item to the list")
    print("2. Enter 2 to remove item from the list")
    print("3. Enter 3 to mark any item as complete")
    print("4. Enter 4 to view Water Testing results")
    print("5. Enter 5 to exit application")

    user_choice = input("\n Enter your selection: ")
    return user_choice

file_name = "aquarium_list.csv"

# if the file does not exist
if (not os.path.isfile(file_name)):
    # Display message if file does not exist, gives user more information.
    print("A list file was created as it did not exist, this will store your Aquarium Name and Date Tested")
    # Create the file
    aquarium_name_file = open(file_name, "w")
    # Enter the headings into the file
    aquarium_name_file.write("Aquarium Name,Date Tested")
    # Close the file
    aquarium_name_file.close()

choice = ""

while choice != "5":
    choice = create_menu()

    if (choice == "1"):
        add_results()

    elif (choice == "2"):
        remove_results()

    elif (choice == "3"):
        mark_results()

    elif (choice == "4"):
        view_results()

    elif (choice == "5"):
        print("You entered 5.")
    else:
        print("Please only enter the options shown above.")


print("Thank you for using the Water Testing application")