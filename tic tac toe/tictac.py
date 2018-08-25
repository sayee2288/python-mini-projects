'''This is a tic tac toe game with a procedural model, it is basic and works'''

def win_conditions(player_lst):
    #print(player_lst)
    for x in player_lst:
        if len(x) == 0:
            return True

def explain_game():
    print('Welcome to Tic Tac Toe,this table shows the numbers to \
            place your token on each position on the grid:')
    for x in full_board:
        for y in x:
            print(y, end='')
        print()
    print('Now please choose player tokens:')

def choose_players():
    tokens = ['X', 'O']
    global player_1, player_2
    player_1 = input("Player 1 choose your token from X or O: ")
    if player_1 not in tokens:
        print("Please choose only X or O")
        player_1 = input("Player 1 choose your token again from X or O: X")
    tokens.remove(player_1)
    player_2 = tokens[0]
    print("Player 2 you are left with", player_2)

def play_the_game(move,token):
    if move in [1,2,3]:
        ind = full_board[0].index(move)
        board[0][ind] = token
    elif move in [4,5,6]:
        ind = full_board[1].index(move)
        board[1][ind] = token
    elif move in [7,8,9]:
        ind = full_board[2].index(move)
        board[2][ind] = token

    for i in win_list[token]:
        if move in i:
            i.remove(move)



board = [[' ', '|', ' ', '|', ' '],[' ', '|', ' ', '|', ' '],[' ', '|', ' ', '|', ' ' ]]
full_board = [[1, '|', 2, '|', 3],[4, '|', 5, '|', 6 ],[7, '|', 8, '|', 9 ]]
possible_moves = [1,2,3,4,5,6,7,8,9]
mv_count = 0
token = ''
win_list = {'X': [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], \
            [3, 6, 9], [1, 5, 9], [3, 5, 7]],
            'O': [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], \
                [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]}

explain_game()
choose_players()


while len(possible_moves) > 0:
    if mv_count%2 == 0:
        print("Player1, ", end='')
        token = player_1
    else:
        print("Player2, ", end='')
        token = player_2

    move = input("Choose your move from 1 to 9: ")

    if move.isdigit():
        play_the_game(int(move), token)
        possible_moves.remove(int(move))
    else:
        print('Invalid input detected, try again')
        continue

    for x in board:
        for y in x:
            print(y, end='')
        print()

    if len(possible_moves) < 6 and len(possible_moves) > 0:
        if win_conditions(win_list[token]):
            print(token, 'has won the game!!! congrats!!!')
            break

    mv_count += 1
else:
    print("Game over, no one won")
