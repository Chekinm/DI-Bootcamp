import requests
import json
import datetime
import time

curr_date = datetime.date.today()
locale = input('Enter where do you live (two letter code like US, IL or GB): ')
    
flag = True
while flag:
    time.sleep(1)
    api_key = '9ccc70db8adf4f9ea765357505eef11d'
    try:
        response = requests.get(f'https://holidays.abstractapi.com/v1/?api_key={api_key}&country={locale}&year={curr_date.year}&month={curr_date.month}&day={curr_date.day}')
        status_code = response.status_code
        response_cnt = response.content
        # olidays.abstractapi.com returns empty responce like b'[]' is there is no holiday
        # we will iterate day by day until there will be not emty repsonce
    except:
        print('Something wrong with internet')
    if status_code == 200 and response_cnt != b'[]':
        flag = False
    else:
        curr_date += datetime.timedelta(1)

resp_dict = json.loads(response_cnt)[0]
hd_name = resp_dict['name']
# get the name of the holiday from repsonce using json.loads()

# and just get the time from now to the holiday date
time_today = datetime.datetime.now()

holiday_date = datetime.datetime(curr_date.year,curr_date.month,curr_date.day,0,0,0)
print(f'Time to  the next holiday, which is {hd_name}, is {holiday_date-time_today} hours.')

# bum!!
