# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning 
# in this course.
# Call the function, and make sure the message displays correctly.

def display_message() -> None:
    print('I\'m learning python!')

display_message()

# 🌟 Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title: str) -> None:
    print(f'My favorite book is {title}.')

favorite_book('Lord of the Ring')

# 🌟 Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(cityname: int, country: int) -> None:
    print(f'{cityname} is in {country}.')

describe_city('Rishon Le Zion', 'Israel')

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
from random import randint


def guess(num: int) -> bool:
    func_num = randint(1,100)
    if num == func_num:
        print(f'Wow. My guess was right. We both mind {num}.')
        return True
    else:
        print(f'Not today. I guess {func_num}, and you was {num}.')
        return False
i = 0
while not guess(24):
    i += 1
print(f'Finnaly  after {i} attemps')

# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

def make_shirt(size: int, message: str) -> None:
    print (f'Creating a shirt. Size - {size}. Slogan on shirt - {message}.')
make_shirt(10, 'Have fun!')

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(size=10, message='I love Python!') -> None:
    print (f'Creating a shirt. Size - {size}. Slogan on shirt - {message}.')

make_shirt()
make_shirt(8)
make_shirt(12, 'Have fun!')

# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

def show_magicians(magician_names) -> None:
    print(*magician_names, sep='\n')

def make_greate(list_of_names: list) -> list:
    return list(map(lambda st: st + ' the Great', list_of_names ))

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

show_magicians(magician_names)

magician_names = make_greate(magician_names)

show_magicians(magician_names)



# 🌟 Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.
from random import uniform

class season():
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi

class month():
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi



def get_random_temp(lo_limit: int, hi_limit: int) -> int:
    return round(uniform(lo_limit, hi_limit), 2)

def get_random_temp_by_season(season: season) -> int:
    temp = get_random_temp(season.lo, season.hi)

    return temp

def get_random_temp_by_month(month: season) -> int:
    temp = get_random_temp(month.lo, month.hi)

    return temp


winter = season(-10,10)
spring = season(0,15)
summer = season(10,30)
autumn = season(15,25)

JANUARY = month(-15,0)
FEBRUARY = month(-10,2)
MARCH = month(-2,6) 
APRIL = month(2,10)
MAY = month(10,20)
JUNE = month(15,30)
JULY = month(15,40)
AUGUST = month(25,40)
SEPTEMBER = month(20,30)
OCTOBER = month(15,28)
NOVEMBER = month(10,20)
DECEMBER = month(1,30)

month_dict = {
    1:JANUARY,
    2:FEBRUARY,
    3:MARCH, 
    4:APRIL,
    5:MAY,
    6:JUNE,
    7:JULY,
    8:AUGUST,
    9:SEPTEMBER,
    10:OCTOBER,
    11:NOVEMBER,
    12: DECEMBER,
}


# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”



def print_message(temp) -> None:
    print(f'Today is {temp} degrees.')
    # Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
    # below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
    if temp < 0:
        print('Brrr, that\'s freezing! Wear some extra layers today')

    # between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
    elif temp < 16:
        print('Quite chilly! Don\'t forget your coat')

    # between 16 and 23
    elif temp < 23:
        print('Not cold not worm.')

    # between 24 and 32
    elif  temp < 32:
        print('Just comfortable. Have a nice day!')

    # between 32 and 40
    else:
        print('It is hot. Suggest swiming!')


def main():
    m_num = int(input('Input month number: '))
    month = month_dict[m_num]
    temp = get_random_temp_by_month(month)
    print_message(temp)


main()

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().




winter = season(-10,10)
spring = season(0,15)
summer = season(10,30)
autumn = season(15,25)



# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
