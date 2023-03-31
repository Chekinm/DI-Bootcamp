list_words = input('Enter your words to sort').split(',')
list_words.sort()
print(*list_words, sep=',')

