# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python


print(("\033[91m {}\033[00m".format("Hello") + "\033[93m {}\033[00m" .format('world\n')) * 4 + ("\033[91m {}\033[00m".format("I") + "\033[93m {}\033[00m" .format('love python\n')) * 4 )

# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

current_month = int(input('Please enter current mount (1-12):'))
if current_month < 3 or current_month == 12:
    print ('It\'s winter now. Cloth warm!')
elif current_month < 6 or current_month <=3:
    print ('It\'s spring now. Let\'s go to watch some flowers!')
elif current_month < 9 or current_month <=6:
    print ('It\'s summer now. Don\'t forget to drink a lot of water!')
else:
    print ('It\'s autumn now. Just relax')
