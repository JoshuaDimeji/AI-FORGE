"""
Build a calculator that presents a menu and performs operations based on user choice.
Requirements:
● Display a menu with at least 5 operations (add, subtract, multiply, divide, power)
● Ask the user to choose an operation
● Ask for the necessary numbers
● Perform the calculation using a function for each operation
● Display the result
● Ask if the user wants to perform another calculation (loop until they say no)
● Handle division by zero gracefully
"""

# Now, to the solution
# First, my user_defined functions
def addition(num_1, num_2):
    return num_1 + num_2

def subtraction(num_1, num_2):
    return num_1 - num_2

def multiplication(num_1, num_2):
    return num_1 * num_2

def division(num_1, num_2):
    return num_1 / num_2

def power(num_1, num_2):
    return num_1 ** num_2


while True:  # This will always loop through, bringing up the Calculator Menu
    print("Welcome to the Calculator App")    # Here is the Calculator welcome page and menu page
    print("Here's the menu")
    print("""
            These are the commands you need:
            Enter 1 for Addition
            Enter 2 for Subtraction
            Enter 3 for Multiplication
            Enter 4 for Division
            Enter 5 for Power
            Enter 0 to exit
    """)
    user_input = int(input("Enter command:"))   # Input for the command
    if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4 and user_input != 5 and user_input != 0:  # Check for a valid input number
        print("Invalid command!")
    elif user_input == 1:
        num_1 = int(input("Enter first number:"))
        num_2 = int(input("Enter second number:"))
        result = addition(num_1, num_2)
        print(f"The result is: {result}")
    elif user_input == 2:
        num_1 = int(input("Enter first number:"))
        num_2 = int(input("Enter second number:"))
        result = subtraction(num_1, num_2)
        print(f"The result is: {result}")
    elif user_input == 3:
        num_1 = int(input("Enter first number:"))
        num_2 = int(input("Enter second number:"))
        result = multiplication(num_1, num_2)
        print(f"The result is: {result}")
    elif user_input == 4:
        num_1 = int(input("Enter first number:"))
        num_2 = int(input("Enter second number:"))
        if num_2 == 0:
            print("Cannot divide by zero")
        else:
            result = division(num_1, num_2)
            print(f"The result is: {result}")
    elif user_input == 5:
        num_1 = int(input("Enter number to raise:"))
        num_2 = int(input("Enter the power:"))
        result = power(num_1, num_2)
        print(f"The result is: {result}")
    elif user_input == 0:
        print("Thanks for using the calculator program. Bye!!!")
        exit()

    print("Do you want to perform another operation? Yes or No")
    user_input_2 = input("Yes or No:")
    if user_input_2.lower() == "yes":
        continue
    else:
        break