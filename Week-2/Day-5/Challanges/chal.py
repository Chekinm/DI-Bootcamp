# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index
# in a list.

a = [1,2,3]
a.insert(1,100)
print(a)

# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.
string = 'aaa  bbb  ccc'
num = string.count(' ')
print(num)

# Exercise 3
# Instructions
# Write a script that calculates the number of upper case 
#  and lower case letters in a string.

from string import ascii_lowercase ,ascii_uppercase
string =  ascii_uppercase + ascii_lowercase + '12,./@#$%^&**()34'
count_upper = 0
count_lower = 0
for char in string:
    if 65 <= ord(char) <= 90:
        count_upper +=1
    if 97 <= ord(char) <= 122:
        count_lower +=1
print(count_upper, count_lower)

# Exercise 4
# Instructions
# Write a function to find the sum of an array without using 
# the built in function:

#     >>>my_sum([1,5,4,2])
#     >>>12
def my_sum(ls: list) -> int:
    """repicate sum method"""
    my_sum = 0
    for num in ls:
        my_sum += num
    return my_sum


assert my_sum([1,5,4,2]) == 12


# Exercise 5
# Instructions
# Write a function to find the max number in a list

#     >>>find_max([0,1,3,50])
#     >>>50
def my_max(ls: list) -> int:
    """repicate original max() method"""
    if ls:
        my_max = ls[0]
    else:
        raise ValueError('my_max() arg is an empty sequence')
    for num in ls:
        if num > my_max:
            my_max = num
    return my_max

assert my_max([1,5,4,2]) == 5
try: 
    my_max([])
except ValueError as value_error:
    print (value_error)

# Exercise 6
# Instructions
# Write a function that returns factorial of a number

#     >>>factorial(4)
#     >>>24

from functools import reduce
from operator import mul
def fact(n):
    """calcualte facotrial of n"""
    return reduce(mul, iter(range(1,n+1)))

assert fact(5) == 120

# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):

def list_count(ls, elem_to_find):
    """replicate count method"""
    counter = 0
    for elem in ls:
        if elem == elem_to_find:
            counter += 1
    return counter
   
assert list_count([1,2],1) == 1
assert list_count(['a','a','t','o'],'a') == 2

# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

#     >>>norm([1,2,2])
#     >>>3
from functools import reduce

def l2norm (lst):
    """return sqrt(sum((lst[i]**2)) for i=1 to n"""
    return reduce(lambda x, y: x + y ** 2, lst) ** 0.5   

assert l2norm([1,2,2,4]) == 5


# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)

def is_mono (lst):
    """return True is list of number is sorted, and false if not"""
    derivative_sign = 0
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            continue
        elif (lst[i] - lst[i-1]) * derivative_sign < 0:
            return False
        else:
            derivative_sign = lst[i] - lst[i-1]
    return True

assert is_mono([7, 6, 5, 5, 2, 0]) == True
assert is_mono([2, 3, 3, 3]) == True
assert is_mono([1, 2, 0, 4]) == False
assert is_mono([-100, -99, 100, -5, 1000]) == False
assert is_mono([0, 0, 0, 0, 0]) == True

# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.

def longest_word(lst: list[str]) -> str:
    """return longest word from list of words"""
    max_lenght = 0
    longest_word = ''
    for word in lst:
        if len(word) > max_lenght:
            max_lenght = len(word)
            longest_word = word
    return(longest_word)

assert longest_word(['a','aa','aaa','aaaa','b','','ababa']) == 'ababa'



# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

def separate_int_and_str (lst):
    list_int=[]
    list_str=[]
    for elem in lst:
        if type(elem) == int:
            list_int.append(elem)
        elif type(elem) == str:
            list_str.append(elem)
        else:
            raise ValueError('Unsupported elem type in the list')
    return list_int,list_str

assert separate_int_and_str([1,2,'a','bcd',100]) == ([1, 2, 100], ['a', 'bcd'])

# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:

def is_palindrome (word: str):
    word = word.lower().replace(' ','')
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            return False
    return True

assert is_palindrome('a bba') == True
assert is_palindrome('aba') == True
assert is_palindrome('abcba') == True
assert is_palindrome('а роза упала на лапу Азора') == True
assert is_palindrome('absscba') == False

# Exercise 13
# Instructions
# Write a function that returns the amount of words in a
# sentence with length > k:

def sum_over_k (txt: str, k: int) -> int:
    return len(list(filter(lambda x: len(x) > k, txt.split())))

assert sum_over_k('Do or do not there is no try',2) == 3
      
#     >>>k=2
#     >>>sum_over_k(sentence,k)
#     >>>3


# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):

def average_dict_value (dct):
    if len(dct):
        return sum(dct.values())/len(dct.values())
    else:
        return 0

assert average_dict_value({'a': 1,'b':2,'c':8,'d': 1}) == 3
assert average_dict_value({}) == 0

# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:

def common_div(n1, n2):
    common_div = []
    for m in range(1, round(min(n1, n2) ** 0.5)):
        if min(n1,n2) % m == 0:
            common_div.append(m)
            common_div.append(int(min(n1,n2)/m))
    common_div.sort()
    return list(filter(lambda x: max(n1,n2) % x == 0, common_div))

assert common_div(10,20) == [1,2,5,10]
assert common_div(833910, 171171) == [1, 3, 7, 11, 19, 21, 33, 57, 77, 133, 209, 231, 399, 627, 1463, 4389]

# Exercise 16
# Instructions
# Write a function that test if a number is prime:

#     >>>is_prime(11)
def is_prime(num):
    for i in range(2, round(num ** 0.5)):
        if not (num % i):
            return False
    return True

#assert is_prime(995402030195497) == True
assert is_prime(2204647) == True
assert is_prime(1961833*2204647) == False

# Exercise 17
# Instructions
# Write a function that prints elements of a list if the 
# index and the value are even:

def weird_print(lst):
    res = []
    for i,list_value in enumerate(lst):
        if i % 2 == 0 and list_value % 2 ==0:
            res.append(list_value)
    return res
       
assert weird_print([1,2,2,3,4,5]) ==  [2,4]

# Exercise 18
# Instructions
# Write a function that accepts an undefined number 
# of keyworded arguments and return the count of different types:

def type_count(**kwargs):
    
    type_dict={}
    for value in kwargs.values():
        arg_type = type(value).__name__
        if arg_type in type_dict:
            type_dict[arg_type] += 1
        else:
            type_dict[arg_type] = 1
    return type_dict

assert type_count(a=1,b='string',c=1.0,d=True,e=False) == {'int': 1, 'str':1 , 'float':1, 'bool':2}



# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method 
# for strings.
# By default the function uses whitespace but it should be
# able to take an argument for any character and split 
# with that argument.

def my_split(string: str, split_char=' ') -> list:
    """replicate split method"""
    res = []
    curr_word = []
    for char in string:
        if char != split_char:
            curr_word.append(char)
        else:
            if curr_word:
                res.append(''.join(curr_word))
            curr_word.clear()
    # don't forget last protion
    if curr_word:
        res.append(''.join(curr_word))
    return res

assert my_split('a ab cde fg,ff') == ('a ab cde fg,ff').split()
assert my_split('aa ') ==  ('aa ').split()
assert my_split(' ') ==  (' ').split()
assert my_split('') ==  ('').split()
assert my_split(' a ','a') ==  (' a ').split('a')
assert my_split('abc','b') ==  ('abc').split('b')

# Exercise 20
# Instructions
# Convert a string into password format.
# Example:
# input : "mypassword"
# output: "***********"
def dimmed_pass(str):
    return '*' * len(str)

assert dimmed_pass('password') == '********'

my_split()


# One Last Thing: Good luck!
