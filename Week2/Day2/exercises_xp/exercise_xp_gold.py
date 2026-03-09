import sys

# Exercise 1: Bank Account
# Instructions
# Part I:

# Create a class called BankAccount that contains the following attributes and methods:
# balance - (an attribute)
# __init__ : initialize the attribute
# deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
# withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive

class BankAccount:
    def __init__(self, balance, username, password):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def deposit(self, num: int):
        if not self.authenticated:
            raise Exception("Authentication required for this account.")
        
        if num <= 0:
            raise ValueError(f"Deposit amount {num} must be positive.")
        
        self.balance += num
        return self.balance
            

    def withdraw(self, num: int):
        if not self.authenticated:
            raise Exception("Authentication required for this account.")

        if num <= 0:
            raise ValueError(f"Withdrawal amount {num} must be positive.")
        
        if num > self.balance:
            raise ValueError("Insufficient funds.")
        
        self.balance -= num
        return self.balance
    
    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
        else:
            self.authenticated = False
        
        return self.authenticated



# Part II : Minimum balance account
# Create a MinimumBalanceAccount that inherits from BankAccount.
# Extend the __init__ method and accept a parameter called minimum_balance with a default value of 0.
# Override the withdraw method so it only allows the user to withdraw money if the balance remains higher than the minimum_balance, raise an Exception if not.

class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, minimum_balance = 0):
        super().__init__(balance, username, password)
        self.min_balance = minimum_balance

    def withdraw(self, num):
        if (self.balance - num) < self.min_balance:
            raise Exception("Balance cannot fall below minimum.")
        
        return super().withdraw(num)
        
    

# Part III: Expand the bank account class
# Add the following attributes to the BankAccount class:
# username
# password
# authenticated (False by default)

# Create a method called authenticate. This method should accept 2 strings : a username and a password. If the username and password match the attributes username and password the method should set the authenticated boolean to True.

# Edit withdraw and deposit to only work if authenticated is set to True, if someone tries an action without being authenticated raise an Exception


account = BankAccount(500,'cher', '123456')
account.authenticate('cher', '123456')
print(account.authenticated)
account.withdraw(300)
print(account.balance)
account.deposit(900)
print(account.balance)


# Part IV: BONUS Create an ATM class

# __init__:
# Accepts the following parameters: account_list and try_limit.

# Validates that account_list contains a list of BankAccount or MinimumBalanceAccount instances.
# Hint: isinstance()

# Validates that try_limit is a positive number, if you get an invalid input raise an Exception, then move along and set try_limit to 2.
# Hint: Check out this tutorial

# Sets attribute current_tries = 0

class ATM:
    def __init__(self, account_list, try_limit):
        if not isinstance(account_list, list):
            raise ValueError("account_list must be a list.")
        
        for account in account_list:
            if not isinstance(account, BankAccount):
                raise ValueError("All items in account_list must be a BankAccount")
            
        try:
            if not isinstance(try_limit, int) or try_limit < 0:
                raise Exception("Try limit must be a positive number")
            self.try_limit = try_limit
        except Exception as e:
            print(f"Error: {e}. Setting try_limit to default (2).")
            self.try_limit = 2
        
        self.account_list = account_list
        self.current_tries = 0

    def show_main_menu(self):
        while True:
            print("\n---ATM Main Menu ---")
            print("1. Log in")
            print("2. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == '2':
                print("Goodbye!")
                break
            else: 
                print("Invalid selection.")

    def log_in(self, usersname, password):
        found_account = None

        for account in self.account_list:
            if account.authenticate(usersname, password):
                found_account = account
                break

        if found_account:
            self.current_tries = 0
            self.show_account_menu(found_account)
        else:
            self.current_tries += 1 
            print(f"Invalid credentials. Attempt {self.current_tries}/{self.try_limit}")

        if self.current_tries >= self.try_limit:
            print("Max tries reached. System shutting down.")
            sys.exit()

    def show_account_menu(self, account):
        while True:
            print(f"\n--- Account Menu ({account.username}) ---")
            print(f"Current Balance: ${account.balance}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Log out")
            choice = input("Select an option: ")

            try:
                if choice == '1':
                    amt = int(input("Amount to deposit: "))
                    account.deposit(amt)
                elif choice == '2':
                    amt = int(input("Amount to withdraw: "))
                    account.withdraw(amt)
                elif choice == '3':
                    account.authentidated = False
                    print("Logged out successfully.")
                    break
                else:
                    print("Invalid choice.")
            except Exception as e:
                print(f"Transaction error: {e}")


# Call the method show_main_menu (see below)

# Methods:
# show_main_menu:
# This method will start a while loop to display a menu letting a user select:
# Log in : Will ask for the users username and password and call the log_in method with the username and password (see below).
# Exit.

# log_in:
# Accepts a username and a password.

# Checks the username and the password against all accounts in account_list.
# If there is a match (ie. use the authenticate method), call the method show_account_menu.
# If there is no match with any existing accounts, increment the current tries by 1. Continue asking the user for a username and a password, until the limit is reached (ie. try_limit attribute). Once reached display a message saying they reached max tries and shutdown the program.

# show_account_menu:
# Accepts an instance of BankAccount or MinimumBalanceAccount.
# The method will start a loop giving the user the option to deposit, withdraw or exit.