# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# For example, with a left shift of 3 –> D would be replaced by A,
# –> E would become B, and so on.

# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

# Check out this tutorial

# Hint:

# for letter in text:
#     cypher_text += chr(ord(letter) + 3)


# some declaration:
#   for more protection we convert text into lowercase and remove any
#   commas or dots wthich can help to crack the code.

from string import ascii_lowercase, ascii_letters

def encrypt(txt, offset):
    out_txt = []
    for char in txt:
        if char in ascii_letters:
            out_txt.append(chr((ord(char.lower()) - ord('a') + offset)%26 + ord('a')))
        elif char == ' ':
            out_txt.append(' ')
    return ''.join(out_txt)

def decrypt(txt, offset):
    out_txt = []
    for char in txt:
        if char in ascii_letters:
            out_txt.append(chr((ord(char.lower()) - ord('a') - offset)%26 + ord('a')))
        elif char == ' ':
            out_txt.append(' ')
    return ''.join(out_txt)

print('Hello, I can crypt you text with Cesar cipher!')
while True:
    direction = input('Type what you like to do (e) encrypt, (d) for decrypt: ')
    if direction in ['e','d']:
        break

text = input('Now enter you text: ')
offset = int(input('ANd now, the offset: '))

if direction == 'e':
    out_txt = encrypt(text, offset)
    print('You encryopted text is below:')
    print(out_txt)
else:
    out_txt = decrypt(text, offset)
    print('You decrypted text is below:')
    print(out_txt)

