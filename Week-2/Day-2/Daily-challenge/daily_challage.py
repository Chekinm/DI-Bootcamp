# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of 
# the number until the list length reaches length.

num = int(input('Please, enter a number: '))
length = int(input('Please, enter a lenght: '))
result_list = []
for i in range(length):
    result_list.append((i + 1)*num)
print(result_list)

# Challenge 2
# Write a program that asks a string to the user, and display 
# a new string with any duplicate consecutive letters removed.

def remove_duplicate(word):
    l = r = len(word) - 1
    while l >= 0 and r > 0:
        l -= 1
        if word[l] == word[r]:
            word = word.replace(word[l] * 2, word[l], 1)
        r = l
    return word

assert remove_duplicate('ppoeemm') =='poem'
assert remove_duplicate('wiiiinnnnd') =='wind'
assert remove_duplicate('ttiiitllleeee') =='title'
assert remove_duplicate('cccccaaarrrbbonnnnn') =='carbon'
assert remove_duplicate('aabbbbbaabbbbbbaaaaa') =='ababa'
assert remove_duplicate('') ==''
assert remove_duplicate('a') =='a'
assert remove_duplicate('aa') =='a'

word = input('Enter a word, I will remove duplicate letters :')
print(remove_duplicate(word))



