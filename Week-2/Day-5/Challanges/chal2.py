# Exercise 1
# Instructions
# Draw the following pattern using for loops:
#   *
#  ***
# *****

for i in range(3):
    print(' ' * (2 - i) + '*' * i + '*' + '*' * i + ' ' * (2 - i))



# Draw the following pattern using for loops:
#     *
#    **
#   ***
#  ****
# *****

for i in range(6):
    print(' ' * (5 - i) + '*' * i)

print('-------------------------')
# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *
for i in range(10):
    print((' ' * 4  +  '*' * 6 + ' ' * 4)[9-i:14 - i])


# Exercise 2
# Instructions
# Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
my_list = [2, 24, 12, 354, 233]
# decalare a vaiable my_list with some values
for i in range(len(my_list) - 1):
# range for loop for lenght_of_the_list-1 times 
# i will be 0,1,2,3
    minimum = i
# set value of minimu to current index i
    for j in range( i + 1, len(my_list)):

# ran a secodn loop from (for of the loop (i =0) will be j = 1,2,3,4)

        if(my_list[j] < my_list[minimum]):
        # check if current element less them first element
            minimum = j
            # if True set minium to index of minimum
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
                # if found element less then my_list[i] put this element on plae number i
                
print(my_list)

# got sorted list 
# sort does in place (means memeory complexity is O(1))
#  with time complexity O(n^2)