import csv


def add_aquarium(file_name):
    results_name = input("Enter Aquarium name: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([results_name])



# def add_test_results(file_name):
#     results_name = {
#         "Date:": input("Enter date: "),
#         "PH:": input("Enter PH: "),
#         "Ammonia:": input("Enter Ammonia: "),
#         "Nitrite:": input("Enter Nitrite: "),
#         "Nitrate:": input("Enter Nitrate: ")
#     }
#     with open(file_name, "a") as f:
#         writer = csv.writer(f)
#         writer.writerow([results_name])





def remove_results(file_name):
    results_name = input("Enter the todo name that you want to delete: ")
    # Create a new list
    todo_lists = []
    # Put all the previous items into the list except the one they want to delete
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        is_exist = False
        for row in reader:
            if (results_name != row[0]):
                todo_lists.append(row) 
            else:
                is_exist = True
    if not is_exist:
        print("No item with that name exists.")

    # Write the enter aquarium_list.csv file with this new list
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)


def view_results(file_name):
    try:
        with open(file_name, "r") as f: 
            reader = csv.reader(f)
            reader.__next__() 
    except FileNotFoundError:
        print("The Aquarium results_table file does not exist.")






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
