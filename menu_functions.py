import csv

from colored import Fore, Back, Style

def add_aquarium(file_name):
    results_name = input("Enter Aquarium name: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([results_name])

def add_test_results(file_name):
    print("For example Date:, Ph:, Ammonia: , Nitrite: or Nitrate: ")
    results_name = input("Enter test results: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([results_name])


def remove_results(file_name):
    results_name = input("Enter the results name that you want to delete: ")
    # Create a new list
    results_lists = []
    # Put all the previous items into the list except the one they want to delete
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        is_exist = False
        for row in reader:
            if (results_name != row[0]):
                results_lists.append(row) 
            else:
                is_exist = True
    if not is_exist:
        print("No item with that name exists.")

    # Write the enter aquarium_list.csv file with this new list
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(results_lists)


def view_results(file_name):
    try:
        with open(file_name, "r") as f: 
            reader = csv.reader(f)
            reader.__next__()
            for row in reader:
                # Concatenate the elements of each row into a single string
                row_string = "".join(row)
                # Print the formatted row
                print(row_string)
    except FileNotFoundError:
        print("The results table doesn't exist")


def ideal_parameters(file_name):
    print("\nAustralian Native fish ideal parameters")
    ideal_parameters = {
        "pH": "6.5 - 7.5 ",
        "Ammonia": "0 - 0.25ppm ",
        "Nitrite": "0ppm ",
        "Nitrate": "0-40ppm ",
        "Temperature": "24 - 26deg ",
        "GH": "50-150ppm "
    }

    for key, value in ideal_parameters.items():
        if key == "pH":
            print(f"{Fore.BLACK}{Back.rgb(112,182,162)}{key}: {value}{Style.reset}")
        elif key == "Ammonia":
            print(f"{Fore.BLACK}{Back.rgb(255,255,173)}{key}: {value}{Style.reset}")
        elif key == "Nitrite":
            print(f"{Fore.BLACK}{Back.rgb(130,210,222)}{key}: {value}{Style.reset}")
        elif key == "Nitrate":
            print(f"{Fore.BLACK}{Back.rgb(231,109,43)}{key}: {value}{Style.reset}")
        else:
            print(f"{key}: {value}")

    print("Colours above relate to water chemical test results as per 'Freshwater Master Test Kit' guidelines")
    print("\nPlease note above is general information only as all fish can differ.")
    print()


# def mark_results(file_name):
#     results_name = input("Enter the todo name that you want to mark as complete: ")
#     todo_lists = []
#     with open(file_name, "r") as f:
#         reader = csv.reader(f)
#         for row in reader:
#             if (results_name != row[0]):
#                 todo_lists.append(row)
#             else:
#                 todo_lists.append(row[0], "True")
#     with open(file_name, "w") as f:
#         writer = csv.writer(f)
#         writer.writerows(todo_lists)
