import random

while True:
    phrase = input('Please enter phrase. It shoudl be 10 char long:')
    if len(phrase) < 10:
        print('Tnis one is too short. Try again!')
        continue
    elif len(phrase) > 10:
        print('This oen is too long. Try again')
        continue
    break

print('Great. Nice and precise.')
print('I see that first and last char')
print('of you phrase is \'' + phrase[0] +'\' and \''+ phrase[-1] +'\'')

print('adding one char at time it will be printer like:')

curr_char = ''
list_of_char = []

for char in phrase:
    list_of_char.append(char)
    curr_char +=char
    print(curr_char)

print('---------------------------------------------------------')
print('And, if  for some reason you like it shuffled, here oyu are:')
random.shuffle(list_of_char)
print(''.join(list_of_char))