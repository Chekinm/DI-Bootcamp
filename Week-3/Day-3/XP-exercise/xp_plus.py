#🌟 Exercise 1: Import

from func import my_sum

a = 5
b = 7
my_sum(a,b)
print('-------------------Ex2-------------------------------')
# 🌟 Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, 
# then rolls a random number between 1 and 100,
# if it’s the same number, display a success message 
# to the user, else don’t.
from random import randint

my_num = int(input('Enter a number between 1 and 100: '))
guesed_num = randint(1, 100)
if my_num == guesed_num:
    print(f'success, my geuss is right you mind number {my_num}.')
else:
    print(f'bad luck, i gueesed - {guesed_num}, while oyu mind {my_num}.') 

print('-------------------Ex3-------------------------------')
# 🌟 Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER 
# case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

from string import ascii_letters
from random import choice

def rnd_str (length=5):
    return ''.join(choice(list(ascii_letters)) for i in range(length))

print(rnd_str(5))
print('-------------------Ex4-------------------------------')
# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

import datetime

a = datetime.date

print(a.today())
print('-------------------Ex5-------------------------------')

# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).
def time_to_first_junurary():
    
    time_today = datetime.datetime.now()
    first_jun = datetime.datetime(time_today.year+1,1,1,0,0,0)
    print(f'Time to 1 January is {first_jun - time_today} hours')
          
time_to_first_junurary()
print('-------------------Ex6-------------------------------')
# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

def minutes(birth_date, birth_month, birth_year):
    time_today = datetime.datetime.now()
    delta = time_today - datetime.datetime(birth_year,birth_month,birth_date,0,0,0)
    print(f'some sad number is - {int(delta.seconds/60 + delta.days*24*60)} minutes.')

minutes(25,6,1976)
print('-------------------Ex7-------------------------------')

# Exercise 7 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

import requests
import datetime
import time
import json
  
curr_date = datetime.date.today()

flag = True
while flag:
    time.sleep(0.2)
    api_key = '9ccc70db8adf4f9ea765357505eef11d'
    try:
        response = requests.get(f'https://holidays.abstractapi.com/v1/?api_key={api_key}&country=GB&year={curr_date.year}&month={curr_date.month}&day={curr_date.day}')
        status_code = response.status_code
        response_cnt = response.content
        # holidays.abstractapi.com returns empty responce like b'[]' if there is no holiday on date
        # we will iterate day by day until there will be not empty repsonce
    except:
        print('Something wrong with internet')
    if status_code == 200 and response_cnt != b'[]':
        flag = False
    else:
        curr_date += datetime.timedelta(1)

resp_dict = json.loads(response_cnt)[0]
hd_name = resp_dict['name']
# get the name of the holiday from repsonce using json.loads()

# and just get the time from now to the holiday
time_today = datetime.datetime.now()

holiday_date = datetime.datetime(curr_date.year,curr_date.month,curr_date.day,0,0,0)
print(f'Time to  the next holiday, which is {hd_name}, is {holiday_date-time_today} hours.')

# bum!!

print('-------------------Ex8-------------------------------')
# Exercise 8 : How Old Are You On Jupiter?
# Instructions
earth_p_s = 31557600
periods = {'earth':31557600, 
            'Mercury': 0.2408467 * earth_p_s, 
            'Venus': 0.61519726 * earth_p_s, 
            'Mars': 1.8808158 * earth_p_s,
            'Jupiter': 11.862615 *earth_p_s,
            'Saturn': 29.447498 *earth_p_s,
            'Uranus': 84.016846 *earth_p_s,
            'Neptune': 164.79132 *earth_p_s,
            }

print(periods)
age = int(input('enter age in seconds: '))
for planet, year in periods.items():
    print(f'Your age on {planet} is {round(age/year,2)} {planet}\'s years.')


# Exercise 9 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation
#  and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list 
# of dictionaries.
# Create a function that adds new dictionaries to the users 
# list. Each user has the following keys: name, adress,
#  langage_code. Use faker to populate them with fake data.

from faker import Faker

fake = Faker('he_IL')


def add_fake_user (users=None):
    if users == None:
        users = []
    else:
        users = users
    users.append({'name':fake.name(),'address':fake.address(), 'language_code': fake.items()[0][0]})
    return users
users = []
for _  in range(100):
    users = add_fake_user(users) 

print(users)


