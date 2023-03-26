# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world

print(("\033[91m {}\033[00m".format("Hello") + "\033[93m {}\033[00m" .format('world\n')) * 4 )


# Write code that calculates the result of: (99^3)*8 
# (meaning 99 to the power of 3, times 8).

print((99**3) * 8)

# Create a variable called computer_brand which value is 
# the brand name of your computer.
# Using the computer_brand variable print a sentence 
# that states the following: "I have a <computer_brand> computer".

computer_brand = 'Lenovo'
print(f'I have a {computer_brand} computer')

# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name = 'Mike'
age = 47
shoe_size = 42
info = f'My name is {name}, and my show size, which is - {shoe_size}, is less then my age ({age}).'
print(info)

# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.

a = 100
b = 42

if a > b:
    print ('Hello world')


# Write code that asks the user for a number and determines whether this number is odd or even.

num = int(input("Plese enter integer the number: "))
if num % 2:
    print('Your number is odd!')
else:
    print('Your number is even!') 


# Write code that asks the user for their 
# name and determines whether or not you have 
# the same name, print out a funny message 
# based on the outcome.

my_name = 'Mikhail'

your_name = input('Pleas, enter you name :')
if your_name == my_name:
    print('Ou. We have the same name! Nice to meet you!')
else:
    print('Nice to meet you!')
    
# Write code that will ask the user for their 
# height in inches.
# If they are over 145cm print a message that 
# states they are tall enough to ride.
# If they are not tall enough print a message that says 
# they need to grow some more to ride.

height_in_inch = float(input('Please, enter you hight in inch:'))

height_in_sm = 2.54 * height_in_inch

print('OK! You are tall enought to ride! if' if height_in_sm >=145 else 'Sorry you have to grow a little bit! Come back later!')
 
