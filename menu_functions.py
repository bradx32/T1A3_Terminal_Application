import csv


def add_results(file_name):
    results_name = input("Enter tank name") # Do grocery
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([results_name]) # Do grocery

# create a dictionary for the "Aquarium name" added when using option 1 


def remove_results(file_name):
    results_name = input("Enter the todo name that you want to delete: ")
    # Create a new list
    todo_lists = []
    # Put all the previous items into the list except the one they want to delete
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        is_exist = False
        for row in reader: # [do grocery,False]
            if (results_name != row[0]): # do laundry != do grocery -> True
                todo_lists.append(row) # [ [do grocery,False], [complete assignment,False] ]
            else:
                is_exist = True
    if not is_exist:
        print("No item with that name exists.")

    # Write the enter aquarium_list.csv file with this new list
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)





def mark_results(file_name):
    results_name = input("Enter the todo name that you want to mark as complete: ")
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (results_name != row[0]):
                todo_lists.append(row)
            else:
                todo_lists.append(row[0], "True")
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)




def view_results(file_name):
    try:
        with open(file_name, "r") as f: #open in read mode ("r")
            reader = csv.reader(f)
            reader.__next__() # this will skip the first lane/title of csv file.
            for row in reader:
                if (row[1 == "True"]):
                    print(f"{row[0]} is complete")
                else:
                    print(f"{row[0]} is not complete")
    except FileNotFoundError:
        print("The Aquarium List file does not exist.")