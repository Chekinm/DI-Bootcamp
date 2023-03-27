# Exercise 1: Concatenate Lists
# Instructions
# Write code that concatenates two lists together 
# without using the + sign.

a = [1,2,3]
b = [2,3,4]
a.extend(b)
print(a)

# Exercise 2: Range Of Numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints 
# all multiples of 5 and 7.
for i in range(1500,2501):
    if i % 5 == 0 or i % 7 == 0:
        print (i)

    
# Exercise 3: Check The Index
# Instructions
# Using this variable
# Ask a user for their name, if their name is in the names
#  list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing 
# the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name = input('Enter you name: ')
if name in names:
    print(f'The index of {name} is - {names.index(name)}')
else:
    print(f'Name - {name} - is not found')


# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
nums = []
num_of_nums = 3
for i in range(num_of_nums):
    nums.append(int(input(f'Input num{i+1} value:')))
print(f'Max value is {max(nums)}')


# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains
#  the letter and whether its a vowel or a consonant.

from string import ascii_lowercase as alphbt

vovels = 'aeiou'

for char in alphbt:
    print(f'- {char} - is vovel' if char in vovels else f'-{char}- is consonant')



# Exercise 6: Words And Letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable 
# called letter.
# Loop through the words list and print the index of the 
# first appearence of the letter variable in each word of the 
# list. # If the letter doesn’t exist in one of the words, 
# print a friendly message with the word and the letter.
words = []
for i in range(7):
    words.append(input(f'Enter word #{i}: '))
letter = input('Now imput any letter: ')

for word in words:
    if letter in word:
        print(f' - {letter}  - is letter number {word.index(letter)} in word {word}')
    else:
        print(f' there is no - {letter} - in word {word}')


Exercise 7:
Instructions
Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.

nums = [i for i in range(1,1000001)]
print(min(nums))
print(max(nums))
print(sum(nums))





Exercise 8 : List And Tuple
Instructions
Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
Suppose the following input is supplied to the program: 34,67,55,33,12,98

res_list = input('Enter six number separated by comma: ').split(',')
res_tpl = tuple(res_list)
print(res_list)
print(res_tpl)


# Exercise 9 : Random Number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

from random import randint
counter_w=0
counter_l=0
num = int(input('please enter number form 1 to 9, or 0 to quit: '))
while num:
    guess_num = randint(1,9)
    flag = (guess_num == num)
    
    if flag:
        print('bingo')
        counter_w +=1
    else: 
        print(f'bad luck, my number is {guess_num}. Try again')
        counter_l +=1
    num = int(input('please enter number form 1 to 9, or 0 to quit: '))

print(f'you played {counter_w + counter_l} games, {counter_l} lost, {counter_w} win')






# Submit Your Exercises :
    






    
