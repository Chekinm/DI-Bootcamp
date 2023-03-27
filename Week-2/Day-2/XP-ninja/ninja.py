# # Exercise 1: Formula
# # Instructions
# # Write a program that calculates and prints a value according 
# # to this given formula:
# # Q = Square root of [(2 * C * D)/H]
# # Following are the fixed values of C and H:
# # C is 50.
# # H is 30.
# # Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# # For example, if the user inputs: 100,150,180
# # The output should be:

# # 18,22,24
# c = 50
# h = 30

# def q (d, c=50, h=30):
#     return round(((2 * c * d) / h) ** 0.5)
# nums = [int(i) for i in input().split(',')]
# for num in nums:
#     print(q(num), end=',')


#     Exercise 2 : List Of Integers
# Instructions
# Given a list of 10 integers to analyze. For example:
# Store the list of numbers in a variable.
from random import randint

list_of_lists = []

list_of_lists.append([3, 47, 99, -80, 22, 97, 54, -23, 5, 7])
list_of_lists.append([44, 91, 8, 24, -6, 0, 56, 8, 100, 2])
list_of_lists.append([3, 21, 76, 53, 9, -82, -3, 49, 1, 76])
list_of_lists.append([18, 19, 2, 56, 33, 17, 41, -63, -82, 1])


# Print the following information:

def built_in (lst):

    print('---------------------------------')
# a. The list of numbers – printed in a single line
    print(*lst, sep=' ')
# b. The list of numbers – sorted in descending order (largest to smallest)
    print(*sorted(lst, reverse=True), sep=' ')
# c. The sum of all the numbers
    print(sum(lst))
# A list containing the first and the last numbers.
    print([lst[0],lst[-1]])
# A list of all the numbers greater than 50.
    print (*(i for i in lst if i > 50))
# A list of all the numbers smaller than 10.
    print (*(i for i in lst if i < 10))
# A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
    print (*(i ** 2 for i in lst))

# The numbers without any duplicates – also print how many numbers are in the new list.
    print(list(set(lst)))
    print(len(set(lst)))
# The average of all the numbers.
    print(sum(lst)/len(lst))
# The largest number.
    print(max(lst))
# 10.The smallest number.
    print(min(lst))

def my_sum(lst):
    my_sum = 0
    for i in lst:
        my_sum += i
    return my_sum
# 11.Bonus: Find the sum, average, largest and smallest number without using built in functions.
def my_max(lst):
    if lst:
        my_max = lst[0]
        for i in lst:
            if i > my_max:
                my_max = i
        return my_max
    else:
        raise ValueError
    
def my_min(lst):
    if lst:
        my_min = lst[0]
        for i in lst:
            if i < my_min:
                my_min = i
        return my_min
    else:
        raise ValueError

for lst in list_of_lists:
    built_in(lst)
print(my_sum(lst))
print(my_max(lst))
print(my_min(lst))

# 12.Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. 
# Ask the user for an integer between -100 and 100 – repeat this 
# question 10 times. Each number should be added into a variable 
# that you created earlier.

# entered_list = [int(input(f'Enter number {i} form -100 to 100: ')) for i in range(10)]
# list_of_lists.append(entered_list)
# 13.Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.

random_list_of_ten = [randint(-100, 100) for i in range(10)]
list_of_lists.append(random_list_of_ten)

# 14.Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.

random_list_of_random = [randint(-100, 100) for i in range(randint(1,50))]
list_of_lists.append(random_list_of_random)

# 15.Bonus: Will the code work when the number of random numbers is not equal to 10?


built_in(random_list_of_random)
print(my_sum(random_list_of_random))
print(my_max(random_list_of_random))
print(my_min(random_list_of_random))