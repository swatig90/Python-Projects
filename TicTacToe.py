from Functions import *

while True:
    print('Welcome to Tic Tac Toe!\n')
    board = [' '] * 10
    turn = choose_first()
    print(f'{turn} will go first \n')
    player1_marker, player2_marker = player_input(turn)
    print('Player1: ' + player1_marker)
    print('Player2: ' + player2_marker)
    play_game = input('Ready to play? y or n: ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player1':
            display_board(board)
            position = user_input(turn, board)
            place_marker(board, player1_marker, position)
            if win_check(board, player1_marker):
                display_board(board)
                print('Player1 won the game!\n')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Its a TIE!')
                    break
                else:
                    turn = 'Player2'
                    #print('Player2 turn \n')
        else:
            display_board(board)
            position = user_input(turn, board)
            place_marker(board, player2_marker, position)
            if win_check(board, player2_marker):
                display_board(board)
                print('Player2 won the game! \n')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Its a TIE!')
                    break
                else:
                    turn = 'Player1'
                    #print('Player1 turn')

    if not replay()=='Y':
        break




