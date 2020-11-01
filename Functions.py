import random
from os import system
import pyautogui


def user_input(player, board):
    choice = 'WRONG'
    within_range = False
    while choice.isdigit() == False or within_range == False:

        choice = input(f'{player}, please enter your move between [1-9]: ')
        if not choice.isdigit():
            print('You have entered incorrect input')
        if choice.isdigit():
            if int(choice) in [1, 2, 3, 4, 5, 6, 7, 8, 9] and board[int(choice)] == ' ':
                within_range = True
            else:
                print('Input out of range!')
                within_range = False
    return int(choice)


def player_input(player):
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input(f'{player} choose X or O: ').upper()
        if marker != 'X' and marker != 'O':
            print('Sorry, invalid choice! Choose again.')
    if player == 'Player1':
        if marker == 'X':
            player1 = 'X'
            print(f'{player} chose {marker}')
            #print('Player2 chose O')
            player2 = 'O'
        else:
            player1 = 'O'
            player2= 'X'
            print(f'{player} chose {marker}')
    else:
        if marker == 'X':
            player2 = 'X'
            print(f'{player} chose {marker}')
            # print('Player2 chose O')
            player1 = 'O'
        else:
            player2 = 'O'
            player1 = 'X'
            print(f'{player} chose {marker}')
    return player1, player2


def display_board(board):
    pyautogui.hotkey('ctrl', ',')
    print(board[7] + '  | ' + board[8] + '  | ' + board[9])
    #print('  ' + ' | ' + '  ' + ' | ' + '  ')
    print('------------')
    print(board[4] + '  | ' + board[5] + '  | ' + board[6])
    #print('  ' + ' | ' + '  ' + ' | ' + '  ')
    print('------------')
    print(board[1] + '  | ' + board[2] + '  | ' + board[3])
    #print('  ' + ' | ' + '  ' + ' | ' + '  ')
    print('\n')


test_board = ['#', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'O', 'X']
board = ['  ']*10
#display_board(board)

def place_marker(board, marker, position):
    if board[position] == ' ':
        board[position] = marker



def win_check(board, marker):
    return((board[1]==board[2]==board[3]==marker) or
    (board[4]==board[5]==board[6]==marker) or
           (board[7]==board[8]==board[9]==marker) or (board[7]==board[4]==board[1]==marker) or
           (board[8] == board[5] == board[2] == marker) or
           (board[3] == board[6] == board[9] == marker) or
           (board[1] == board[5] == board[9] == marker) or
           (board[7] == board[5] == board[3] == marker) )


def replay():
    choice = input('Do you want to play again? Y or N').upper()
    return choice


def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'


def full_board_check(board):
    for i in range(1,10):
        if board[i] == ' ':
            return False
    return True



