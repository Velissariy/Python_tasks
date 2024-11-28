import random

def create_board():
    return [' ' for _ in range(9)]

def display_board(board):
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Игрок 1, выберите X или O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[6] == mark and board[7] == mark and board[8] == mark) or
            (board[0] == mark and board[3] == mark and board[6] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[0] == mark and board[4] == mark and board[8] == mark) or
            (board[2] == mark and board[4] == mark and board[6] == mark))

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Игрок 2'
    else:
        return 'Игрок 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(len(board)):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or not space_check(board, position):
        try:
            position = int(input('Выберите позицию (0-8): '))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
    return position

def replay():
    return input('Хотите сыграть ещё раз? (да/нет): ').lower().startswith('д')

print('Добро пожаловать в Крестики-нолики!')

while True:
    theBoard = create_board()
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' ходит первым.')

    play_game = input('Готовы начать игру? (да/нет): ').lower().startswith('д')

    if play_game:
        game_on = True
    else:
        game_on = False


    while game_on:
        if turn == 'Игрок 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Игрок 1 выиграл!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок 2'

        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Игрок 2 выиграл!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок 1'

    if not replay():
        break
