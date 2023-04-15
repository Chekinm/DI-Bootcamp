from string import ascii_lowercase, punctuation
from collections import Counter

sample_text = 'A good book would sometimes cost as much as a good house.'


class Text():
    
    @classmethod
    def add_text_from_file(cls, url):
        with open (url) as file:
            text = file.read()
        return cls(text)
    
    def __init__(self, text) -> None:
        self.text = text
        self.word_counter = Counter(text.lower().split())
        
    def frequency(self, some_word):
        if some_word in self.word_counter:
            print(f'There are {self.word_counter[some_word]} occurnace of {some_word} in text')
        else:
            print(f'There is no occurance of {some_word} in text.')

    def most_common(self):
        # more interesting most common ten with frequency
        # if you like just one change 10 to 1 and uncomment[0][0]
        return self.word_counter.most_common(10)#[0][0]
            
    def all_unique(self):
        return list(self.word_counter)


class TextModification(Text):
    
    @classmethod
    def add_text_from_file(cls, url):
        with open (url) as file:
            text = file.read()
        return cls(text)

    def text_with_no_punctuation(self):
        new_text = []
        for char in self.text:
            if char not in punctuation:
                new_text.append(char.lower())
        self.text = ''.join(new_text)
        self.word_counter = Counter(self.text.split())

    def text_no_stop_words(self):
        stop_words = Text.add_text_from_file('./stop_words_english.txt')
        new_text = []
        for word in self.text.split():
            if word.lower() not in stop_words.word_counter:
                new_text.append(word.lower())
        self.text = ' '.join(new_text)
        self.word_counter = Counter(new_text)

    def text_no_special_char(self):
        new_text = []
        for char in self.text:
            if char.lower() in ascii_lowercase or char.lower() == ' ':
                new_text.append(char.lower())
        self.text = ''.join(new_text)
        self.word_counter = Counter(self.text.split())
  

    
my_text = Text(sample_text)

my_long_text = TextModification.add_text_from_file('./the_stranger.txt')

print(my_text.most_common())
my_text.frequency('good')
my_text.frequency('bad')
print(my_text.all_unique())


print(my_long_text.most_common())
my_long_text.frequency('friend')

my_long_text.text_with_no_punctuation()
print(my_long_text.most_common())

my_long_text = TextModification.add_text_from_file('./the_stranger.txt')
my_long_text.text_no_stop_words()
print(my_long_text.most_common())

my_long_text.text_no_special_char()
print(my_long_text.most_common())

my_long_text = TextModification.add_text_from_file('./the_stranger.txt')
my_long_text.text_with_no_punctuation
print(my_long_text.most_common())





