import psycopg2
import os
from psycopg2 import sql 
from dataclasses import dataclass
from menumanager import MenuItem, DBSQLManager, DBconnect


def main_menu_selection() -> str:
    """read and validate user choice in main menu"""
    invalid_inp = True 
    while invalid_inp:
        #os.system("cls")
        print('Welcom the the menu manager')
        print('Please enter what you wanna do')
        print('(n) Create new menu')
        print('(l) Select existing menu form list')
        print('(d) Delete menu from db')
        print('(x) Exit')
        selection = input('Type you coice: ')
        if selection in ('n','l','d','x'):
            return selection
        else:
            print('PLease enter a valid option!')


def manage_specific_menu(db: DBSQLManager):
    """read and and perform user choid in specific menu(table) menu"""
    invalid_input = True 
    while invalid_input:
        # loop until user lik eto exit to the top level menu (press x)
        print(f"\nYou are editing '{db.table_name}' menu")
        print('Please enter what you wanna do')
        print('(a) Add new dish')
        print('(u) Update existing dish')
        print('(d) Delete dish from menu')
        print('(p) Print all dishes from menu')
        print('(x) return to the top level menu')
        selection = input('Type you coice: ')

        if selection == 'a':
            #append a dish into a menu
            try:
                item = MenuItem(input('Enter dish name: '), int(input('Enter dish price: ')))
                db.add_dish(item)
            except ValueError as e:
                print('\n'+str(e)+'\n'+'Try again')
            
        elif selection == 'u':
            # update one of the menu dish  with new price
            try:
                item = MenuItem(input('Enter dish name: '), int(input('Enter new dish price: ')))
                db.update_dish(item)
            except ValueError as e:
                print('\n'+str(e)+'\n'+'Try again')

        elif selection == 'd':
            # delete specific dish from menu
            try:
                item = MenuItem(input('Enter dish name to delete: '),0)
                db.delete_dish(item)
                print(f'\n{item.dish_name.capitalize} has been deleted from menu.\n')
            except ValueError as e:
                print('\n'+str(e)+'\n'+'Try again')

        elif selection == 'p':
            # print all item in table
            try:
                menu = db.get_menu()
                print(f"Here is a dishes from  '{db.table_name}': ")
                print(*menu, sep='\n')
            except ValueError as e:
                print('\n'+str(e)+'\n'+'Try again')

        elif selection == 'x':
            # just exit
            invalid_input = False
        else:
            # wrond input return to top
            print('Please enter a valid option!')


def create_new_menu() -> DBSQLManager:
    """read menu name from user input and create and return new db instance"""
    invalid_inp = True 
    while invalid_inp:
        # os.system("cls")
        table_name = input('\nInput a name for new menu: ')
        if table_name.isalpha():
            try:
                db = DBSQLManager(table_name, **db_env)
                print(f"Menu '{table_name}' created.")
                manage_specific_menu(db)
                invalid_inp =  False
            except psycopg2.OperationalError:
                print('Something wrong  with postgre. Try another name')
        else:
            print('PLease enter a valid name!')
        

def select_from_list(db_general: DBconnect, db_env) -> DBSQLManager:
    menu_list = db_general.display_tables_names()
    invalid_input = True
    while invalid_input:
        if menu_list:
            choices = {}
            for index, menu in enumerate(menu_list):
                choices[index] = [f'({index}) - {menu[0]}', menu[0]]
            print('Select manu to manage')                
            print(*[menu[0] for menu in choices.values()], sep='\n')
            number = input('Enter a number: ')
            if number.isnumeric() and int(number) in choices:
                return DBSQLManager(choices[int(number)][1], **db_env)
            else:
                print('Enter existing number')
        else:
            print('Currently there is no menu in the database. Create one')
            input ('Press any key to return to main menu: ')
            invalid_input = True
        

def delete_menu(db_general, db_env):
    menu_list = db_general.display_tables_names()
    invalid_input = True
    while invalid_input:
        if menu_list:
            choices = {}
            for index, menu in enumerate(menu_list):
                choices[index] = [f'({index}) - {menu[0]}', menu[0]]
            print('Select menu to delete')                
            print(*[menu[0] for menu in choices.values()], sep='\n')
            number = int(input('Enter a number: '))
            if number in choices:
                db = DBSQLManager(choices[number][1], **db_env)
                db.self_delete()
                input (f"\nMenu '{db.table_name}' deleted, press any key to return to main: \n")
                invalid_input = False
            else:
                print('Enter existing number')
        else:
            print('\nCurrently there is no menu in the database. Create one')
            input ('Press any key to return to main menu: \n')
            invalid_input = False


def main():
    # runing until exit from user input
    db_general = DBconnect(**db_env) # just connection to database 
                           # we need it to get table list
    run = True
    while run:
        sel = main_menu_selection()
        if sel =='n':
            db = create_new_menu() # return db as DBSQLMAnager
        elif sel == 'l':
            db = select_from_list(db_general, db_env) # return db as DBSQLMAnager
            manage_specific_menu(db)
        elif sel == 'd':
            delete_menu(db_general, db_env)
        elif sel == 'x':
            print('See you later!')
            run = False

db_env = {
    #this is our database data to connect, chenge to yours
    'host': 'localhost',
    'user': 'psyco_user',
    'password': 'psyco_user_password',
    'dbname': 'menu_manager',
}


# just run it
main()
