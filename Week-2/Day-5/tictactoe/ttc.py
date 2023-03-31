# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
import numpy as np
import os


def display_board(game_map):
    """game_map is a 3x3 array with game state
    just print it put in fancy table""" 
    
    print('*' * 13)
    for i in range(3):
        print(f'* {game_map[i][0]} | {game_map[i][1]} | {game_map[i][2]} *')
        if i < 2:
            print('*---|---|---*')
        else:
            print('*' * 13)


def check_win(game_map):
    """return -1 if x win 0  is nobody and  1 if o win
    """
    game_matrix = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            if game_map[i][j] == x:
                game_matrix[i][j] = 1
            elif game_map[i][j] == o:
                game_matrix[i][j] = -1
    for i in range(2):
        for sum_line in np.sum(game_matrix,i):
            if sum_line == 3:
                return 1
            elif sum_line == -3:
                return -1
    if np.trace(game_matrix) == 3:
        return 1
    elif np.trace(game_matrix) == -3:
        return -1
    if np.trace(np.fliplr(game_matrix)) == 3:
        return 1
    elif np.trace(np.fliplr(game_matrix)) == -3:
        return -1
    return 0

def player_input(player, game_map):
    print(f'Now {player} turn.')
    while True:
        x_coor = int(input('Enter row: '))
        y_coor = int(input('Enter column: '))
        if  not (0 < x_coor < 4 and 0 < y_coor < 4):
            print('We play 3x3 variant of the game!')
            continue
        if game_map[x_coor-1][y_coor-1] == ' ':
            game_map[x_coor-1][y_coor-1] = player
            os.system('cls')
            display_board(game_map)
            return True
        print('Sorry this field is occupaed. Enter another field')

def game_clear(game_map):
    for i in range(3):
        for j in range(3):
            game_map[i][j] = ' '

def play():
    game_map = [[' ' for i in range(3)] for j in range(3)]
    game_on = True
    while game_on:
        game_clear(game_map)
        os.system('cls')
        display_board(game_map)
        counter = 0
        while counter < 9 and check_win(game_map) == 0:
            player_input((x if counter%2 else o), game_map)
            counter += 1
        else:
            os.system('cls')
            display_board(game_map)
            print('***********************')
            print('****  Game over!  *****')
                
            check = check_win(game_map)

            if check:
                print(f'****   \"{x if check == 1 else o}\" won!   *****')
                print('***********************')      
            else:
                print('***  Nobody wins!   ***')
        cont = input('Press "n" for a new game or any other char to quit: ')
        game_on = True if cont == 'n' else False


#Fedya's staff
x = "\033[91m{}\033[00m".format("x")
o = "\033[93m{}\033[00m".format('o')

# just play the game

play()


