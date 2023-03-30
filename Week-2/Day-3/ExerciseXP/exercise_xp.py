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
################   ex2   ##################################################################
###########################################################################################


# it is in separate fileExercise 2 : Cinema
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

from Cinema import Watchers, Movie, Cinema

family1 = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 28}

family_1_watchers = Watchers(family1)

my_cinema = Cinema({'kid':2,'teen':23, 'adult':100})

my_movie = Movie('Kill Bill', True)

my_cinema.print_ticket(family_1_watchers.watchers_list, my_movie)

family2 = {}

family_2_watchers = Watchers()
family_2_watchers.read_input()
my_movie2 = Movie('Blue moon', True)
my_cinema2 = Cinema()
my_cinema2.print_ticket(family_2_watchers.watchers_list, my_movie2)


###########################################################################################
################   ex3   ##################################################################
###########################################################################################


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

brand_dict = {
                'name':'Zara', 
                'creation_date':1975,
                'creator_name':'Amancio Ortega Gaona',
                'type_of_clothes':['men', 'women', 'children', 'home'],
                'international_competitors':['Gap', 'H&M', 'Benetton'],
                'number_stores':7000,
                'major_color':{
                    'France':'blue',
                    'Spain':'red', 
                    'US':['pink', 'green'],
                    },
            }

# 3. Change the number of stores to 2.
brand_dict['number_stores'] = 2

# 4. Print a sentence that explains who Zaras clients are.
print('The customers of zara are: {}'.format(','.join(brand_dict['type_of_clothes'])))

# 5. Add a key called country_creation with a value of Spain.
brand_dict['country_creation']='Spain'

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

if brand_dict.get('international_competitors') != None:
    brand_dict.get('international_competitors').append('Desigual')
print(brand_dict['international_competitors'])

# 7. Delete the information about the date of creation.
brand_dict.pop('creation_date')
print(brand_dict)

# 8. Print the last international competitor.

print(brand_dict['international_competitor1s'][-1])

# 9. Print the major clothes colors in the US.
print(brand_dict['major_color']['US'])
# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand_dict))

# 11. Print the keys of the dictionary.
print(brand_dict.keys())
# 12. Create another dictionary called more_on_zara with the following details:
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000,
    }

# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand_dict.update(more_on_zara)
print(brand_dict)


# 14. Print the value of the key number_stores. What just happened ?
print(brand_dict['number_stores'])

###########################################################################################
################   ex4   ##################################################################
###########################################################################################
# Exercise 4 : Disney Characters


users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]


#1
disney_users_A={}
disney_users_B={}

for i, value in enumerate(users):
    disney_users_A[value] = i
    disney_users_B[i] = value

print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# 2
print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 
disney_users_C={}
for i, value in enumerate(sorted(users)):
    disney_users_C[value] = i
   
print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.

disney_users_A1={}

for i, value in enumerate(users):
    if 'i' in value:
        disney_users_A1[value] = i    
print(disney_users_A1)

# The characters, which names start with the letter “m” or “p”.

disney_users_A2={}


for i, value in enumerate(users):
    if  value[0].lower() in ['m','p']:
        disney_users_A2[value] = i
    
print(disney_users_A2)


