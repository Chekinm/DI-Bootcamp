###########################################################################################
################   ex1   ##################################################################
###########################################################################################

# Create a set called my_fav_numbers with all your favorites numbers.
my_fav_numbers = [7, 23, 55, 421]

# Add two new numbers to the set.
# add one
my_fav_numbers.append(100000)

# or extend with ahother list
my_fav_numbers.extend([444, 555])

# Remove the last number.
my_fav_numbers.pop()

# Create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_fav_numbers = [-1, -2, -100]

# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
our_fav_numbers = my_fav_numbers + friend_fav_numbers

# test results
assert my_fav_numbers == [7, 23, 55, 421, 100000, 444]
assert our_fav_numbers == [7, 23, 55, 421, 100000, 444, -1, -2, -100]

###########################################################################################
################   ex2 - interprise :)  ###################################################
###########################################################################################

# Given a tuple which value is integers, is it possible to add more integers to the tuple?
a = (1,2)
b =  (100,200)

 
try:
    a = a + 1
except Exception as ex:
    print(f'You are trying to do forbidden things. Error - {ex} - arised')
finally:
    print(f'Lets have a look if it was changed. It was (1,2), and now it is {a}')
    print(f'We was not able to change it' if a == (1,2) else 'We change it.')

# thought that we can concatenate two tuples let's try

try:
    a = a + b
except Exception as ex:
    print(f'You are trying to do forbidden things. Error - {ex} - arised')
finally:
    print(f'Lets have a look if it was changed. It was (1,2), and now it is {a}')
    print(f'We was not able to change it' if a == (1,2) else 'We change it.')


###########################################################################################
################   ex3 - ##################################################################
###########################################################################################

# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove “Banana” from the list.
# can do it two different way
basket.remove('Banana')
assert basket == ["Apples", "Oranges", "Blueberries"]

# or remove by index
basket.insert(0,'Banana')
basket.pop(0)
assert basket == ["Apples", "Oranges", "Blueberries"]

# Remove “Blueberries” from the list.
basket.remove('Blueberries')

# Add “Kiwi” to the end of the list.

basket.append('Kiwi')
# Add “Apples” to the beginning of the list.
basket.insert(0, 'Apples')

# should be like that
assert basket == ['Apples', 'Apples', 'Oranges', 'Kiwi']

# Count how many apples are in the basket.

num_apples = basket.count('Apples')
assert num_apples == 2
# Empty the basket.

basket.clear()

assert basket == []

# Print(basket)
print(basket)


###########################################################################################
################   ex4 - ##################################################################
###########################################################################################


# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 
# (don’t hard-code the sequence).


float_seq = [int(i/2) if i//2 == i/2 else i/2 for i in range(3,11)]
# have no idea if you really like us to create mix of int and float but anyway here 
# it is, as asked
assert float_seq == [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5] 

###########################################################################################
################   ex5 - ##################################################################
###########################################################################################

# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element 
# which has an even index.

print(*(num for num in range(1,21)))
print(*(num for num in range(1,21) if num%2 == 0))



###########################################################################################
################   ex6 - ##################################################################
###########################################################################################

# Write a while loop that will continuously ask the user for their name, 
# unless the input is equal to your name.
my_name = 'Mike' 
while True:
    username = input('Please enter your name: ')
    if username != my_name:
        print (f'Hey {username}. We don\'t like {username}s here. If you have friends')
        print (f'who\'s name is {my_name} call him. We allowed him')
    else:
        print (f'Hey {username}. Nice to have you in our Mikes community!MIke')
        break

###########################################################################################
################   ex7 - ##################################################################
###########################################################################################


# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, 
# eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your 
# favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fruits =  input('Please enter all you favorite fruits. \nPLease enter it as one string with space as delimiter: ')
fruits_list = fruits.split()

print('Now, I know all you favorites fruit!')
guess = input('Enter any fruit, and I will say if you like it or not: ')
print('Yemmi. You like it!' if guess in fruits_list else 'No. That is not you favorite one.')


###########################################################################################
################   ex8 - ##################################################################
###########################################################################################




# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ 
# stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is 
# (10 + 2.5 for each topping).

order_list = ['pizza']
pizza_price = 10
toping_price = 2.5

print('You ordered a pizza, with mozarella.')

u_input = input('Type what you want to add, or quit to exit:')
while u_input != 'quit':
    order_list.append(u_input)
    u_input = input('Type what you want to add, or quit to exit:')

total = 0
print('Your order is:')

for component in order_list:
    component_price = (pizza_price if component == 'pizza' else toping_price)
    print(f'\t -- {component} \t ---- \t {component_price}')
    total += component_price

print(f'\n \t The total is \t\t{total}')
