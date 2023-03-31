# The computer choose a random word and mark stars for each
#  letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer 
# fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part 
# to the gallows (head, body, left arm, right arm, left leg,
# right leg).
# The player will continue guessing letters until they can 
# either solve the word(s) (or phrase) or all six body parts 
# are on the gallows.
# The player can’t guess the same letter twice.
attemps = 'attemps'
attemp = 'attemp'

a = [0] * 7

a[0] = f"""


 _______
 |     |
 |     o
 |    /|\ 
 |    / \\
 |
/|\\
"""
a[1] = f"""


 _______
 |     |
 |     o
 |    /|\ 
 |    /
 |
/|\\
"""
a[2] = f"""


 _______
 |     |
 |     o
 |    /|\ 
 |     
 |
/|\\
"""
a[3] = f"""


 _______
 |     |
 |     o
 |    /|
 |    
 |
/|\\
"""
a[4]= f"""


 _______
 |     |
 |     o
 |    /
 |     
 |
/|\\
"""
a[5]= f"""


 _______
 |     |
 |     o
 |    
 |     
 |
/|\\
"""

a[6]= f"""


 _______
 |     |
 |     
 |    
 |     
 |
/|\\
"""

import random
from os import system

def print_hidden(wrd: list, hide: list, att_left: int, guessed_list: list) -> None:
    to_print = ''.join(['*' if hide[i] else wrd[i] for i in range(len(wrd))])
    system('cls')
    print(a[game_counter])
    print('')
    print(to_print)
    print('')
    print('Guessed letters!:' + ','.join(guessed_list))
    print('')
    print(f'{att_left} {attemps if game_counter > 1 else attemp} left!')
    

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']


game_on = True
while game_on:
    word = list(random.choice(wordslist))
    hidden_word = [True if i != ' ' else False for i in word]
    game_counter = 6
    guessed_list = []
    guessed_char = ''

    while game_counter > 0 and True in hidden_word:
        print_hidden(word, hidden_word, game_counter, guessed_list)
        guessed_char = input('Guess letter!: ')
        while guessed_char in guessed_list:
            guessed_char = input('Already tried. Choose another letter!: ')
        guessed_list.append(guessed_char)
        if guessed_char in word:
            for i in range(len(word)):
                if (guessed_char == word[i]):
                    hidden_word[i] = False
        else:
            game_counter -= 1
    else:
        print_hidden(word, hidden_word, game_counter, guessed_list)
        if True in hidden_word:
            print('You lost!')
        else:
            print('GG!')
        

    cont = input('Press "n" for a new game or FF if you surrender: ')

    game_on = True if cont == 'n' else False
    