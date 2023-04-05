# Exercise 1: Bank Account
# Part I:

class BankAccount():
    

    def __init__(self, username, password, balance = 0, authenticated = False) -> None:
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated  = authenticated 

    def authenticate (self):
        username = input('Enter user name: ')
        password = input('Enter password: ')
        if username == self.username and password == self.password:
            self.authenticated = True
        else:
            print('User name does not exist or password is incorrect')


    def deposit (self, amount):
        if amount >= 0:
            self.balance += amount
        else:
            raise ValueError (f'Deposit amount must be positive')

    def withdraw (self, amount):
        if self.authenticated:
            if amount >= 0 and amount <= self.balance:
                self.balance -= amount
            elif amount < 0: 
                raise ValueError (f'Withdrawl amount could not be negative')
            else:
                raise ValueError (f'Not enough money. You request {amount}, while you have only {self.balance}')
        else:
            raise ConnectionError ('You are not logged it. PLease login first')


a = BankAccount( '1', '1', 100,)
print(a.balance)
a.deposit(200)

try:
    a.deposit(-200)
except ValueError as ve:
    print(ve)

a.authenticate()

a.withdraw(10)
a.balance
try:
    a.withdraw(-100)
except ValueError as ve:
    print(ve)

try:   
    a.withdraw(1000)
except ValueError as ve:
    print(ve)
    
# Part II : Minimum balance account

class MinimumBalanceAccount(BankAccount):

    def __init__(self, username, password, balance=0, minmum_balance=0, authenticated = False):
        
        if balance >= minmum_balance:
            super().__init__(username, password, balance)
            self.minmum_balance = minmum_balance
        else:
            raise ValueError (f'Balance must be grater that {minmum_balance}')

a = MinimumBalanceAccount('1','1',300,200)

# Part IV: BONUS Create an ATM class
class ATM():

    def __init__(self, account_list, try_limit):
        for acc in account_list:
            if isinstance(acc, BankAccount) or isinstance(acc, MinimumBalanceAccount):
                self.account_list = account_list
            else:
                raise TypeError ('account list must conatin only BankAccount or MinimumBalanceAccount instances')
            try:
                if try_limit <= 0:
                    raise ValueError ('try limit must be positive')
                else:
                    self.try_limit = try_limit
            except ValueError as ve:
                print (ve)
            finally:
                self.try_limit = 2

# Validates that try_limit is a positive number, if you get an invalid input raise an Exception, then move along and set try_limit to 2.
# Hint: Check out this tutorial

# Sets attribute current_tries = 0

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


