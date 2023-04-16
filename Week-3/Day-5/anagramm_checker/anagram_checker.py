class AnagrammCheker():

    @staticmethod
    def create_key(word):
        word = word.lower()
        return ''.join(sorted([char for char in word]))
    
    def __init__(self, url):
        self.anagram_dict = {}
        with open (url) as file:
            for line in file:
                word = line.strip().lower()
                chars_key = AnagrammCheker.create_key(word)
                if chars_key in self.anagram_dict:
                    self.anagram_dict[chars_key].update({word:1})
                else:
                    self.anagram_dict[chars_key] = {word:1}

    def is_valid_word(self, word):
        word = word.lower()
        chars_key = AnagrammCheker.create_key(word)
        if chars_key in self.anagram_dict and word in self.anagram_dict[chars_key]:
            return True
        return False

    def get_anagramm(self, word):
        chars_key = AnagrammCheker.create_key(word)
        anagramms = self.anagram_dict[chars_key]
        if len(anagramms) == 1:
            return []
        else:
            return list(anagramms)


   





# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:


# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.
