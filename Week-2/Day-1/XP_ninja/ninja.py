# Use python to find out how many characters are in 
#the following text, use a single line of code 
#(beyond the establishment of your my_text variable).

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(f'My_Text var has {len(my_text)} character including spaces, dots and commas.')

num_of_alphnum = len(my_text.replace(',','').replace('.','').replace(' ',''))

print(f'If counting only alphanumeric char it has {num_of_alphnum} chars')

num_of_words = len(my_text.replace(',','').replace('.','').split())

print(f'And it has {num_of_words} words!')
print('--------------------------------------------------')

# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

print('Now we will play a game!')
print('Each time you enter a sentences, I check if it has an \'a\' simbol inside')
      
print('if know, i check the lenth of the phrase, and if it is longer then previuse one')
print('you have one more step! if shorter, your game is over!')
print('Let\'s go!')

max_len = 0

while True:
    phrase = input('Enter a phrase whithout \'a\':')
    if 'a' in phrase:
        print('I told you not to use \'a\'. You failed. Your game is over!')
        break
    elif len(phrase) <= max_len:
        print('Nice try, but it\'s not longer then previouse. Game over!')
        break
    print('This is good one. Keep going!')
    max_len = len(phrase)
    