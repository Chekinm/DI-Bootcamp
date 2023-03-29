# Exercise 1 : What’s Your Name ?
# Instructions
# Write a function called get_full_name() that takes three arguments: 
# 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it’s omitted by the user, 
# the name returned should only contain the first and the last name.
# For example, 
# get_full_name(first_name="john", middle_name="hooker", last_name="lee") 
# will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.

def get_full_name(name1: str, name2 : str, name3='') -> str:
    return f'{name1} {name2} {name3}'


# Exercise 2 : From English To Morse
# Instructions
# Write a function that converts English text to morse code and another 
# one that does the opposite.
# Hint: Check the internet for a translation table, every letter 
# is separated with a space and every word is separated with a slash /.



morse_code_dict = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    ' ':'/'
                    }

morse_decode_dict = {'.-': 'a', '-...': 'b',
                    '-.-.': 'c',
                    '-..': 'd', '.': 'e', '..-.': 'f', 
                    '--.': 'g', '....': 'h', '..': 'i',
                    '.---': 'j', '-.-': 'k', '.-..': 'l', 
                    '--': 'm', '-.': 'n', '---': 'o', 
                    '.--.': 'p', '--.-': 'q', '.-.': 'r',
                    '...': 's', '-': 't', '..-': 'u', 
                    '...-': 'v', '.--': 'w', '-..-': 'x',
                    '-.--': 'y', '--..': 'z',
                    }
   
def morse_code (text, morse_code_dict):
    text_to_convert = text.split()
    converted = []
    for word in text_to_convert:
       converted.append(' '.join(morse_code_dict[char] for char in word))
    return '/'.join(converted)


def morse_decode (text, morse_decode_dict):
    converted = []
    text_to_convert = text.split('/')
    for word in text_to_convert:
        converted.append(''.join(morse_decode_dict[char] for char in word.split()))
    return ' '.join(converted)

coded = morse_code('aaa bbb ccc ddd',morse_code_dict)
print(coded)

decoded = morse_decode(coded,morse_decode_dict)
print(decoded)

# Exercise 3 : Box Of Stars
# Instructions
# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************
def box_printer (*arg):
    text_lst = [*arg]
    max_length = len(max(text_lst, key=len))
    star_st = '*' * (max_length + 4)
    for i in range(len(text_lst)):
        text_lst[i] = '* ' + text_lst[i] + ' ' * (max_length - len(text_lst[i])) + ' *'
    print(star_st)
    print(*text_lst,sep='\n')
    print(star_st)
    
   
box_printer("Hello", "World", "in", "reallylongword", "a", "frame")

# Exercise 4
# Analyse this code before executing it. What is the purpose of this code?

# this is isert sorting algorithm
# i refactor it a litle bit to be more readable
# also fix pep8
#
def insertion_sort(alist):
    for index in range(1, len(alist)):
        #currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > alist[position]:
            alist[position], alist[position-1] = alist[position-1], alist[position]
            position = position - 1
    #alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)
