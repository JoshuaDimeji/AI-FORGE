# This is a mini banking system
# A bank account is an object with attributes (balance, account number) and behaviors (deposit, withdraw, check balance)

class BankAccount:  # the class name
    def __init__(self, account_number,
                 balance=0):  # object attributes: account_number and balance which is initially assigned 0
        self.account_number = account_number
        self.balance = balance

    def deposit(self):  # the deposit() method
        amount = int(
            input("How much do you want to deposit?: "))  # request input from user and stores in variable "amount"
        self.balance += amount  # amount is then added to self.balance which is in the constructor
        print(f"You have succesfully deposited ${amount}, Your balance is now ${self.balance}")

    def withdraw(self):  # the withdraw() method
        amount = int(input("How much do you want to withdraw? "))  # requests input from user and store in "amount"
        if amount > self.balance:  # checks if amount is greater than user's balance
            print("Insufficient fund!")
        else:
            self.balance -= amount  # if amount isn't greater, it's deducted from the self.balance
            print(f"You have withdrawn ${amount} successfully")

    def check_balance(self):  # the check_balance() method
        print(f"Your balance is ${self.balance}")


my_bank = BankAccount("220044")  # create the object, my_bank. 220044 is the account_number that was passed
while True:  # the loop in the code body. It first displays the main menu of the bank app
    print("""                                    
Welcome to the mini banking app system
This is the main menu

Enter 1 to check balance
Enter 2 to deposit
Enter 3 to withdraw
Enter 4 to view account number
Enter 0 to quit app
    """)
    user_choice = int(input("Enter your choice: "))  # requests for user's choice
    if user_choice != 1 and user_choice != 2 and user_choice != 3 and user_choice != 4 and user_choice != 0:  # checks if an invalid number is entered
        print("You have entered an invalid command!\nDo you want to try again?")
        user_choice_2 = input("Yes or No: ").lower()  # requests for another user's input of "yes" or "no"
        if user_choice_2 == "yes":  # if yes, it returns to the main page
            continue
        elif user_choice_2 == "no":  # if no, the program terminates
            break
    elif user_choice == 1:
        my_bank.check_balance()  # calls the check_balance() method
        user_choice_2 = input("Do you wish to continue? Yes or No: ").lower()
        if user_choice_2 == "yes":
            continue
        elif user_choice_2 == "no":
            break
    elif user_choice == 2:
        my_bank.deposit()  # calls the deposit() method
        user_choice_2 = input("Do you wish to continue? Yes or No: ").lower()
        if user_choice_2 == "yes":
            continue
        elif user_choice_2 == "no":
            break
    elif user_choice == 3:
        my_bank.withdraw()  # calls the withdraw() method
        user_choice_2 = input("Do you wish to continue? Yes or No: ").lower()
        if user_choice_2 == "yes":
            continue
        elif user_choice_2 == "no":
            break
    elif user_choice == 4:
        print(f"Your account number is: {my_bank.account_number}")
        user_choice_2 = input("Do you wish to continue? Yes or No: ").lower()
        if user_choice_2 == "yes":
            continue
        elif user_choice_2 == "no":
            break
    elif user_choice == 0:
        break
