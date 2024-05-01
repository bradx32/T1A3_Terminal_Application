# System packages
import os.path 

# External packages
from rich import print # Lesson video at 2:34:00 watch from here if needing help


# Imports of our own fucntiones
from menu_functions import add_aquarium, add_test_results, remove_results, view_results

print("Welcome to the Aquarium Water Testing results application \U0001F9EA \U0001F41F ")
print("Here you can name your Aquarium, store, view and remove test results.")
print("\n")

def create_menu(): # Function #1 
    print("1. Enter 1 to name your Aquarium")
    print("2. Enter 2 to add test results to your Aquarium")
    print("2. Enter 3 to remove item from the list")
    print("4. Enter 4 to view Water Testing results")
    print("5. Enter 5 to exit application")

    user_choice = input("\n Enter your selection: ")
    return user_choice

file_name = "results_table.csv"

# if the file does not exist
if (not os.path.isfile(file_name)):
    # Display message if file does not exist, gives user more information.
    print("A list file was created as it did not exist, this will store your Aquarium name and results")
    # Create the file
    aquarium_name_file = open(file_name, "w")
    # Enter the headings into the file
    aquarium_name_file.write("Aquarium Name\n")
    # Close the file
    aquarium_name_file.close()

choice = ""

while choice != "5":
    choice = create_menu()

    if (choice == "1"):
        add_aquarium(file_name)
        
    elif (choice == "2"):
        add_test_results(file_name)

    elif (choice == "3"):
        remove_results(file_name)

    elif (choice == "4"):
        view_results(file_name)

    elif (choice == "5"):
        print("You entered 5.")
    else:
        print("Please only enter the options shown above.")


print("Thank you for using the Water Testing application")

