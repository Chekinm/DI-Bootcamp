###########################################################################################
################   ex1   ##################################################################
###########################################################################################

# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res_dict = {}
for key, value in zip(keys,values):
    res_dict[key] = value
# Expected output:
assert res_dict == {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


###########################################################################################
################   ex1   ##################################################################
###########################################################################################


# Exercise 2 : Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead 
# of using the provided family variable (Hint: ask the user 
# for names and ages and add them into a family dictionary 
# that is initially empty).

# abusing DRI principle. Lets use class and functions writen yesterday.
# i organize it a separate module cinema.py 

from cinema import watcher, watchers

family1 = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

family_1_watchers = watchers()
family_1_watchers.read_dict(family1)
family_1_watchers.print_ticket()

# family2 = {}

family_2_watchers = watchers()
family_2_watchers.read_input()
family_2_watchers.print_ticket()

