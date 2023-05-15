"""reverse enigineered from week4-day4 just exchange DB with json file
a bit stupid but it works and  I need a points in leaderbord:)"""


# import psycopg2
import os
# from psycopg2 import sql 
from dataclasses import dataclass
import json
# from menumanager import MenuItem, DBSQLManager, DBconnect

@dataclass
class MenuItem():
    # this data class represent menu item
    # this will be out type to store menu item if needed
    dish_name: str
    price: int
    def __str__(self):
        return (f'{self.dish_name.capitalize()}\t - {self.price} ils.')


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


def manage_specific_menu(menu_dict:dict, rest_name:str): 
    """read and and perform user choid in specific menu(table) menu from JSON file """
    invalid_input = True 
    while invalid_input:
        # loop until user lik eto exit to the top level menu (press x)
        print(f"\nYou are editing '{rest_name}' menu")
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
                add_dish(menu_dict, rest_name, item)
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


def create_new_menu(menu_dict:dict) -> dict:
    """read menu name from user input and create and return new db instance"""
    invalid_inp = True 
    while invalid_inp:
        # os.system("cls")
        rest_name = input('\nInput a name for new menu: ')
        if rest_name.isalpha():
            if rest_name not in menu_dict['restaurants']:
                menu_dict['restaurants'].update({rest_name:{'items':[]}})
                print(f"Menu '{rest_name}' created.")
                menu_dict = manage_specific_menu(menu_dict, rest_name)
                invalid_inp =  False
            else:
                print('Menu already exist. Try another name')
        else:
            print('PLease enter a valid name!')
        

def select_from_list(menu_dict:dict) -> dict:
    menu_list = list(menu_dict)
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
                return menu_dict[menu_list[int(number)]]
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

def add_dish(menu_dict:dict, rest_name:str, item:MemuItem)->dict:
    """add new dish to specified restorant menu, return updated dict"""

    if item.name in menu_dict["restaurants"].[rest_name]


    return menu_dict


def main():
    #runing until exit from user input

    with open ('restaurant_menu.json') as f:
        menu_dict = json.load(f) 
        print(menu_dict)

    run = True
    while run:
        sel = main_menu_selection()
        if sel =='n':
            db = create_new_menu(menu_dict) # return subdict from main dictinary with new restorant        elif sel == 'l':
            db = select_from_list(db_general, db_env) # return db as DBSQLMAnager
            manage_specific_menu(db)
        elif sel == 'd':
            delete_menu(db_general, db_env)
        elif sel == 'x':
            with open ('restaurant_menu.json', 'w') as f:
                menu_dict = json.dump(f) 
                print('Current state was saved to file!')
            print('See you later!')
            run = False

db_env = {
    #this is our database data to connect, chenge to yours
    'host': 'localhost',
    'user': 'psyco_user',
    'password': 'psyco_user_password',
    'dbname': 'menu_manager',
}

with open ('restaurant_menu.json') as f:
    menu_dict = json.load(f) 
    print(menu_dict)

# just run it
main()
