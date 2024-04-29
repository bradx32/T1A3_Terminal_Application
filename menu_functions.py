import csv

def add_results(file_name):
    todo_name = input("Enter a todo item: ") # Do grocery
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"]) # Do grocery,False


def remove_results():
    print("Remove results")

def mark_results():
    print("Mark results")

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