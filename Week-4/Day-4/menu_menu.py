from menumanager import MenuItem, DBSQLManager, DBconnect
import psycopg2
from psycopg2 import sql 
from dataclasses import dataclass


db_env = {
    'host': 'localhost',
    'user': 'psyco_user',
    'password': 'psyco_user_password',
    'dbname': 'menu_manager',
}


def main_menu_selection() -> str:
    """read and validate user choice"""
    invalid_inp = True 
    while invalid_inp:
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

def create_new_menu():
    pass

def select_from_list():
    pass

def delete_menu():
    pass

def main():
    # runing until exit from user input
    run = True
    while run:
        sel = main_menu_selection():
        if sel = 'n':
            create_new_menu()
        elif sel = 'l':
            select_from_list()
        elif sel = 'd':
            delete_menu()
        else sel = 'x':
            Print('See you later!')
            run = False


db = DBSQLManager(menu_name, **db_env)
db.display_tables_names()
#print(db.get_by_name('burger'))
#print(*db.get_menu(), sep='\n')
pasta = MenuItem('pasta6',140)

burger = MenuItem('burger7', 100)
try:
    
    db.add_dish(pasta)
    db.add_dish(burger)
    burger = MenuItem('burger7',4000)
    db.update_dish(burger)
        

except ValueError as e:
    print("Already added")








#db.delete_dish(pasta)

print(*db.get_menu(), sep='\n')
db.display_tables_names()
db.self_delete()


#print(*db.get_menu(), sep='\n')