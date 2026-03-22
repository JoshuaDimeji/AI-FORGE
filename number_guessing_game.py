"""
Build a game where the computer picks a random number and the user tries to guess it.
Requirements:
● Generate a random number between 1 and 100
● Ask the user to guess the number
● Tell them if their guess is too high, too low, or correct
● Keep track of the number of guesses
● When they guess correctly, display the number of attempts
● Ask if they want to play again
● Use at least 3 functions (e.g., generate_number, get_guess, check_guess)
"""

# Now to the solution
# First, my user_defined functions

import random

def generate_number():
    random_number = random.randint(1, 100)   # generate an integer from 1 to 100
    return random_number

def get_guess():     # function that gets guess input from user
    user_guess = int(input("Enter a random number from 1 to 100: "))
    return user_guess

def check_guess(user_guess, random_guess):   # function that checks if the random number and user guess are the same
    if user_guess > random_guess:
        print("Your guess is too high")
    elif user_guess < random_guess:
        print("Your guess is too low")
    elif user_guess == random_guess:
        print("Your guess is correct")
        return "Your guess is correct"

count = 1

while True:                        # loops until the condition is met
    user_input = get_guess()     # retrieves user input here
    random_number = generate_number()  # assigns the randomly generated number to random_number
    guessing_check = check_guess(user_input, random_number)  # calls the check_guess() function here
    if guessing_check == "Your guess is correct":
        break
    count += 1
print(f"It took {count} guesses to get to the right number")