# Exercise 1 : When Will I Retire ?
# Instructions
# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).

# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# After calculating the age of a person, the function should return the age (the age is an integer).
# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.
# Some Hints

# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message informing the user whether they can retire or not.
# As always, test your code to ensure it works.

from datetime import date


def get_age(birthdate: date) -> int:
    """return the age of the person with specified birthdate"""
    today = date.today()
    bd_this_year = date(today.year, birthdate.month, birthdate.day)
    if (bd_this_year - today).days >= 0:
        age = today.year - birthdate.year - 1
    else:
        age = today.year - birthdate.year
    return age

def can_retire(gender: str, date_of_birth: date):
    """return true if person rich retiremtn age of false if not"""
    age = get_age(date_of_birth)
    if gender == 'm' and age > 62:
        return True
    if gender == 'f' and age > 67:
        return True
    return False

gender = input('Hello! PLease enter you gener (m) for male or (f) for female: ')

date_of_birth_str = input('Ok! What is you birthday in (yyyy/mm/dd) format?: ')

date_of_birth = date(*(int(i) for i in date_of_birth_str.split('/')))

print(f'Your are {get_age(date_of_birth)}')
can_ret = can_retire(gender, date_of_birth)
print('You can ' + ('not' if can_ret else '') + 'retire!') 
print('Keep working hard!' if can_ret else 'Relax now!')



# Exercise 2 : Sum
# Instructions
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:
# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)

# Hint: treating our number as a int or a str at different points in our code may be helpful

def funny_repeater(x: int, repeats=4) -> int:
    res = 0
    res_str = []
    for i in range(1, repeats + 1):
        res_str.append(str(x) * i)
        res += int(str(x) * i)
    return ' + '.join(res_str), res 


res = funny_repeater(3,5)
print(res[0] + ' = ' + str(res[1]))