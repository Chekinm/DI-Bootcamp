# Exercise 1 : Cars
# Instructions
# Copy the following string into your code: 


user_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# Convert it into a list using Python (don’t do it by hand!).

user_lst = user_str.split()

# Print out a message saying how many manufacturers/companies are in the list.
print(f'we have {len(user_lst)} car-brand in the string')

# Print the list of manufacturers in reverse/descending order (Z-A).
print(sorted(user_lst, reverse=True))

# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
counter = 0
sp_char = 'o'
for car in user_lst:
    if sp_char in car:
        counter += 1
print(counter)

# Find out how many manufacturers’ names do not have the letter ‘i’ in them.

counter = 0
sp_char = 'i'
for car in user_lst:
    if sp_char not in car:
        counter += 1
print(counter)

# Bonus: There are a few duplicates in this list:
dupl_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

# Remove these programmatically. (Hint: you can use set to help you).
dupl_list = list(set(dupl_list))

# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.
print(*dupl_list,sep=', ')
print(f'we have {len(dupl_list)} car-brand in the list')

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

dupl_list.sort()

def rev_let(str):
    res = ''
    for i in str:
        res = i + res
    return res

print(*(rev_let(str) for str in dupl_list), sep=', ')
