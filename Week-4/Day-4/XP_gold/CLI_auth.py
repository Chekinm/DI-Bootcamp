# Create a dictionary that contains users: each key 
# will represent a username, and each value will 
# represent that user’s password. 
# Initialize this dictionary with 3 users & passwords.
import getpass
import bcrypt
from passlib.hash import bcrypt


def login_menu(user_dict:dict, is_logged_in):
    user = input('Enter user_name: ')
    password = getpass.getpass()
    hasher = bcrypt.using(rounds=13)  # Make it slower
    hashed_password = hasher.hash(password)

    if user in is_logged_in:
        print('User already logged in')
        return True
    elif user in user_dict:
        if hasher.verify(password, user_dict[user]):
            is_logged_in.append(user)
            print('You are loogin in\n')
            return True
        else:
            print('Wrong password\n')
            return False
    else:
        print('User name is not in the user list')
        inp = input('Enter (c) to cretate new user or any key to continue:')
        if inp == 'c':
            user = input('Enter new user_name: ')
            hashed_password = hasher.hash(getpass.getpass())
            user_dict[user] = hashed_password
            print(f"User '{user}' has been created")  
            return False   
        
        
user_dict = {}
is_logged_in = []

run = True

while run:
    print('Enter what you want to do:')
    print('(l) to login')
    inp = input('(e) to exit:  ')
    if inp == 'l':
        logged_in = login_menu(user_dict, is_logged_in)
    elif inp == 'e':
        run = False
    else:
        print('Wrong input. Try again')

