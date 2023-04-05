# Exercise 1: Bank Account
# Part I:

import time

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


    def authenticate_api (self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
            return True
        else:
            return False


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

# Part II : Minimum balance account

class MinimumBalanceAccount(BankAccount):

    def __init__(self, username, password, balance=0, minmum_balance=0, authenticated = False):
        
        if balance >= minmum_balance:
            super().__init__(username, password, balance)
            self.minmum_balance = minmum_balance
        else:
            raise ValueError (f'Balance must be grater that {minmum_balance}')

    def withdraw (self, amount):
        if (self.balance - amount) >= self.minmum_balance:
            super().withdraw(amount)   
        else:
            print (f'Balance after opertaion  must be grater that {self.minmum_balance}')

# Part IV: BONUS Create an ATM class
class ATM():

    def __init__(self, account_list, try_limit):
        self.cooldown = 30
        self.current_tries = 0
        self.last_try_time = time.time()
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
            
    def show_main_menu(self):
        running = True
        while running:
            #os.system('cls')
            print('Choose an option:')
            choose = input('Press (l) to login, or (e) to exit:')
            if choose == 'e':
                running = False
            elif choose == 'l':
                if self.current_tries < self.try_limit:
                    username = input('Enter username: ')
                    password = input('Enter password: ')
                    self.login(username, password)
                elif time.time() - self.last_try_time > self.cooldown:
                    self.current_tries -= 1
                else:
                    print(f'You enter wrong password more then {self.try_limit} times.')
                    print(f'Input blocked for {self.cooldown} seconds.')
                    print(f'{self.cooldown - (time.time() - self.last_try_time)} seconds remaining.')
            else:
                print('invalid option')
    
    def login(self, username, password):
        for bank_account in self.account_list:            
            if bank_account.authenticate_api(username, password):
                self.show_account_menu(bank_account)
                self.current_tries = 0
                return None
            else:
                pass
        print ('Wrong username or password')
        self.current_tries += 1   
        print (f'{self.try_limit - self.current_tries} attempt remaining')

        self.last_try_time = time.time()  
            

    def show_account_menu(self, bank_account):
        running = True
        while running:
            print(f'You balance is {bank_account.balance}')
            choice = input('Enter option: \n (w) - withdraw: \n (d) - deposit: \n (e) - exit: ')
            if choice == 'w':
                amount = int(input('Enter amount: '))
                bank_account.withdraw(amount)
            
            elif choice == 'd':
                amount = int(input('Enter amount: '))
                bank_account.deposit(amount)
            elif choice == 'e':
                bank_account.authenticated = False
                running = False
            


a = BankAccount( '1', '1', 100,)
b = BankAccount( '2', '2', 200,)
# print(a.balance)
# a.deposit(200)

# try:
#     a.deposit(-200)
# except ValueError as ve:
#     print(ve)

#a.authenticate()

#a.withdraw(10)
#a.balance
# try:
#     a.withdraw(-100)
# except ValueError as ve:
#     print(ve)

# try:   
#     a.withdraw(1000)
# except ValueError as ve:
#     print(ve)
    
lim = MinimumBalanceAccount('3','3',300,200)

lis_acc = [a,b,lim]

atm = ATM(lis_acc, 2)
atm.show_main_menu()