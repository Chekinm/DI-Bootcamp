###########################################################################################
################   ex9 - ##################################################################
###########################################################################################
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

# I combine the rules of both problem into one.
# You have been asked to enter number of people in the group
# then name and age of each memeber of the group
# then the type of file they want to watch
# programm will print the verdict depending on members age ages

class watcher():
    def __init__(self, name, age, restricted="False", price=15):
        self.name = name
        self.age = age
        self.restricted = (True if age < 21 else False) 
        # I change this from original to be logical -> just less than 21
        if self.age < 3:
            self.price = 0
        elif self.age < 12:
            self.price = 10
        else:
            self.price = 15

def print_group_ticket(list_of_watchers, movie_is_adultonly=False):
    total = 0
    forbiden_list = []
    allowed_list = []
    for person in list_of_watchers:
        if movie_is_adultonly and person.restricted:
            forbiden_list.append(person.name + ' - ' + str(person.age) + ' years')
            continue
        total += person.price
        all_per_str = f'{person.name} \t  --- {person.price} shekels'
        allowed_list.append(all_per_str)
        
    if forbiden_list:
        print('Unfortunatley this person is not allowed to watch the movie:')
        print(*forbiden_list, sep='\n')
        if allowed_list:
            print('This is a check for others:')
    else:
        if allowed_list:
            print("Here is you check:")
                  
    if allowed_list:
        print(*allowed_list, sep='\n')
        print(f'total price is   {total}  shekels')
    
    
####### entry point ################

print('Enter number of persons in the group:')
num_of_person = int(input())
list_of_watcher = []

for i in range(num_of_person):
    print(f'Enter the name of the person number {i+1}:')
    name_i = input()
    print(f'Enter the age of the person number {i+1}:')
    age_i = int(input())
    list_of_watcher.append(watcher(name_i, age_i))

adult_only_in = input('Is this film adults only, type yes or no:')
adult_only = True if adult_only_in == 'yes' else False
print_group_ticket(list_of_watcher, adult_only)