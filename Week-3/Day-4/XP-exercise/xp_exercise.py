# exersice-1
from random import randrange


def get_words_from_file(url:str) -> list:
    '''read file from url and make a list of words from that file'''
    with open(url) as file:
        word_list = [line.strip() for line in file.readlines()]
    return word_list
    

def get_random_sentence(word_list, length):
    '''create a random sequence o number from 0 to lenth of word_list
    get word by this random indexes '''
    sentence = []
    for i in range(length):
        sentence.append(word_list[randrange(len(word_list))].lower())
    return ' '.join(sentence)
    

def main():
    '''read the user unput of length of the sentence
    read file from url and create a random sentence of length entered 
    user'''
    url = './sowpods.txt'
    print('This programm read the file with dictionary of words and create a random sentence')
    try:
        sent_length = int(input('Enter the length of sentence (should be from 2 to 20): '))
        if 2 <= sent_length <= 20:
            word_list = get_words_from_file(url)
            sentence = get_random_sentence(word_list, sent_length)
            print(sentence)
            return None
        else:
            print('You\'ve entered the wrong number. Sorry. Buy!')
            return None
    except ValueError:
        print('You entered not a number. Sorry. Buy!')
        return None   

main()


# 🌟 Exercise 2: Working With JSON
# Instructions
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# create a dict from json file
dict_from_json = json.loads(sampleJson)

# access desired key value
print(dict_from_json['company']['employee']['payable']['salary'])

# add new key with value
dict_from_json['company']['employee']['birth_date'] = '20 Jan 1995'
print(dict_from_json)

# convert the dict back to json
new_json = json.dumps(dict_from_json)

# check results
print(new_json)
