# Exercise 1: Birthday Look-Up
# Instructions
# Create a variable called birthdays. Its value should be a dictionary.

birthday = {}

# Initialize this variable with birthdays of 5 people of your choice. 
# For each entry in the dictionary, the key should be the person’s name, 
# and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.

birthday = {'Mike': '2002/10/05',
            'Dan': '1998/12/31',
            'Jenifer': '2000/01/01',
            'Sara': '1960/05/23',
            }


# Print a welcome message for the user. 
# Then tell them: “You can look up the birthdays of the people in the list!”“
print('Hello!')
print('You can look up the birthdays of the people in the list!')

# Ask the user to give you a person’s name and store the answer in a variable.

name = input('Give me a name: ')

# Get the birthday of the name provided by the user.
# Print out the birthday with a nicely-formatted message.

if name in birthday:
    print(f'Person birthday is {birthday[name]}')

# Exercise 2: Birthdays Advanced
# Instructions
# Before asking the user to input a person’s name print out all of the names in the dictionary.
print('There are another persons in the list')
print('Here is the full list: {}.'.format(', '.join(birthday.keys())))
name2 = input('Try another person: ')

# If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)

if name2 in birthday:
    print(f'Person birthday is {birthday[name2]}')
else:
    print(f'Sorry, we don’t have the birthday information for {name2}.')

# Exercise 3: Add Your Own Birthday

# Instructions
# Add this new code: before asking the user to input a person’s name to look up,
#  ask the user to add a new birthday:
# Ask the user for a person’s name – store it in a variable.
print('Now lets add yours birthday')
name3 = input('Enter your name: ')



# Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
bd = input('Enter your birthday (in the format “YYYY/MM/DD”):')

#  Now add this new data into your dictionary.
#  Make sure that if the user types any name that exists in the dictionary – 
#  including the name that he entered himself –
#  the corresponding birthday is found and displayed.

while True:
    if name3 in birthday:
        name3 = input (f'We already have one {name3}. Do you have another name?: ') 
        bd = input('And birthday (in the format “YYYY/MM/DD”):')
    else:
        birthday[name3] = bd
        print('Succseseffuly added')
        break


# Exercise 4: Fruit Shop
# Instructions
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# Using the dictionary above, each key-value pair represents an item and its price - 
# print all the items and their prices in a sentence.
text = []
for key, value in items.items():
    text.append (f'{key} - {value}$ per kg')

print('WE have in the shop:' + ', '.join(text) + '.') 
# Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
# write some code to calculate how much it would cost to buy everything in stock.
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}
total = 0
for key, dct in items.items():
    total += dct['price'] * dct['stock']

print(f'Total cost is: {total}')
