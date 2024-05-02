# System packages
import os.path 

# External packages
# Lesson video at 2:34:00 watch from here if needing help
from colored import Fore, Back, Style
from rich import print # this overides the 'print' and gives colours to numbers and strings
from rich.text import Text


# Imports of our own fucntiones
from menu_functions import add_aquarium, add_test_results, remove_results, view_results, ideal_parameters

# Title and terminal brief
print("\n[bold]Welcome to the Aquarium Water Testing results application[/bold] \U0001F9EA \U0001F41F ")
print("[bold]Here you can name your Aquarium, store, view and remove test results.[/]")
print("\n")

# Function overview and user guide
def create_menu():  
    print("1. Enter 1 to [bold][dodger_blue2]name[/][/] your Aquarium")
    print("2. Enter 2 to [bold][bright_green]add[/][/] test results to your Aquarium")
    print("2. Enter 3 to [bold][red1]remove[/][/] item from the list")
    print("4. Enter 4 to [bold][bright_cyan]view[/][/] Water Testing results")
    print("5. Enter 5 to [bold][yellow]check[/][/] ideal Aquariuam parameters")
    print("5. Enter 6 to [bold][bright_white]exit[/] application")

    user_choice = input("\nEnter your selection: ")
    return user_choice

# Variable to link the .csv file
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

while choice != "6":
    choice = create_menu()

    if (choice == "1"):
        add_aquarium(file_name)
        
    elif (choice == "2"):
        add_test_results(file_name)

    elif (choice == "3"):
        remove_results(file_name)

    elif (choice == "4"):
        view_results(file_name)
    
    elif(choice == "5"):
        ideal_parameters(file_name)

    elif (choice == "6"):
        print("You entered 6.")
    else:
        print("Please only enter the options shown above.")


print("Thank you for using the Water Testing application")

