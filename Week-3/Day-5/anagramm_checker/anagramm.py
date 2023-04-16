from anagram_checker import AnagrammCheker


def show_main_menu(main_dict):
    running = True
    while running:
        
        print('Choose an option:')
        choose = input('Press (w) to check a word, or (e) to exit: ')
        if choose == 'e':
            running = False
        elif choose == 'w':
            
            word = input('Enter word: ').strip()
            if len(word.split()) > 1:
                print('Enter only one word')
            elif main_dict.is_valid_word(word):
                print('This is a valid word')
                choice = input ('Would you like to check if there are any anagramms (c) or any key to enter another word? :')
                if choice == 'c':
                    check_anagram(word, main_dict)
            else:
                print('This word is not a valid word, try another one.')
            
            
            
        else:
            print('invalid option')

def check_anagram(word, main_dict):
    anagram_list = main_dict.get_anagramm(word)
    print(f'Ok. You entered word: {word}')
    print('This is a valid word')
    print('We check our database and found')
    
    if anagram_list:
        print(f'that word {word} has {len(anagram_list)} anagramm(s).')
        anagram_str = ', '.join(anagram_list)
        print(f'It is: {anagram_str}.')
    else:
        print(f' that word {word} has no anagramms')
    

main_dict = AnagrammCheker('./sowpods.txt')
show_main_menu(main_dict)
 