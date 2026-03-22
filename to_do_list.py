"""
Build a program that manages a to-do list with add, view, and remove functionality.
Requirements:
● Display a menu with options: Add task, View tasks, Remove task, Exit
● Add task: ask for task description and add it to a list
● View tasks: display all tasks with numbers
● Remove task: ask for task number and remove it from the list
● Loop until the user chooses Exit
● Use functions for each menu option
● Handle invalid input (e.g., removing a task that doesn't exist)
"""

to_do_list = []   # empty list to save the tasks

def add_tasks():    # function to add task
    while True:
        task = input("Enter the task to add: ")     # Requests task to add
        to_do_list.append(task)             # adds the task to the list
        print("Task added successfully!")
        user_input = input("Do you want to add more tasks? Yes or No: ")
        if user_input.lower() == "yes":
            continue
        elif user_input.lower() == "no":
            break


def view_tasks():                # function to view tasks
    if len(to_do_list) == 0:        # checks the length of the list. If it's zero, then it's an empty list
        print("No tasks added!")
    else:
        print("\nYour task:")       # else, the list has an item(s)
        i = 1                       # sets a counter that will serve as the task numbering or index
        for task in to_do_list:
            print(i, "-", task)     # for loop to iterate and show the items in the list
            i += 1

def delete_tasks():                # function to delete tasks
    if len(to_do_list) == 0:        # checks if the list is empty
        print("No task to remove!")
    else:
        print("\nYour task:")       # show all tasks in the list
        i = 1
        for task in to_do_list:
            print(i, "-", task)
            i += 1
        remove_num = int(input("Enter the task number to remove: "))        # request for the task number to remove from the list

        if remove_num > 0 and remove_num <= len(to_do_list):        # checks if a valid number was entered
            removed_task = to_do_list.pop(remove_num - 1)       # use the .pop() method to remove a particular item from the list
            print("\nTask removed successfully!")
            print("Removed task:", removed_task)        # display the removed item
        else:
            print("Invalid task number!")

while True:                             # Always display the to-do menu
    print("""                           
        Here is the To-do list menu:
        Enter 1 to add task
        Enter 2 to view tasks
        Enter 3 to delete task
        Enter 0 to quit
    """)
    user_choice = input("Enter your choice: ")   # Request user input for coice
    if user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "0":   # checks if a valid input is entered
        print("Invalid choice! Try again.")
        continue  # continue to loop menu till a valid choice is inputted
    elif user_choice == "1":
        add_tasks()
    elif user_choice == "2":
        view_tasks()
    elif user_choice == "3":
        delete_tasks()
    elif user_choice == "0":        # Quits or exits the program
        print("Existing program ...")
        break
