# Tic-Tac-Toe against AI using pure Monte Carlo Tree Search
import random


board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))


def draw_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8] + '\n')


def check_status(arr):
    for a, b, c in win:
        if arr[a] == arr[b] == arr[c] == 'X':
            return 'x'
        if arr[a] == arr[b] == arr[c] == 'O':
            return 'o'
    count = 0
    for i in range(len(arr)):
        if arr[i] != ' ':
            count += 1
    if count == 9:
        return 'tie'


def p1_func():
    print('Player place X')
    while True:
        x = input('Pick where to place X (1-9):')
        if x.isdigit():
            x = int(x)
            if x >= 1 and x <= 9 and board[x-1] == ' ':
                board[x-1] = 'X'
                break
            else:
                print('try again\n')
        else:
            print('try again\n')
        draw_board()


def place_temp_board(arr,string):
    temp_available = []
    for k in range(len(arr)):
        if arr[k] == ' ':
            temp_available.append(k)
    x = random.choice(temp_available)
    arr[x] = string


def comp_func():
    legal_moves = []
    win_count_arr = []
    count = 500
    print('Computer place O')
    for i in range(len(board)):
        if board[i] == ' ':
            legal_moves.append(i)
    for i in legal_moves:
        win_count = 0
        for k in range(count):
            temp_board = board.copy()
            temp_board[i] = 'O'
            pre_win = False
            temp_finish = check_status(temp_board)
            if temp_finish == 'o':
                win_count += 3
                pre_win = True
            elif temp_finish == 'tie':
                win_count += 1
                pre_win = True

            while not pre_win:
                place_temp_board(temp_board, 'X')
                temp_finish = check_status(temp_board)
                if temp_finish == 'x':
                    win_count -= 50
                    break
                elif temp_finish == 'tie':
                    win_count += 1
                    break
                place_temp_board(temp_board, 'O')
                temp_finish = check_status(temp_board)
                if temp_finish == 'o':
                    win_count += 3
                    break
                elif temp_finish == 'tie':
                    win_count += 1
                    break
        win_count_arr.append(win_count)
    win_index = win_count_arr.index(max(win_count_arr))
    board[legal_moves[win_index]] = 'O'
    draw_board()


def player_first():
    finish = False
    draw_board()
    while not finish:
        p1_func()
        finish = check_status(board)
        if finish == 'x':
            print('Player wins')
            break
        elif finish == 'tie':
            print('Tie')
            break
        comp_func()
        finish = check_status(board)
        if finish == 'o':
            print('Computer wins')
            break
        elif finish == 'tie':
            print('Tie')
            break


def comp_first():
    finish = False
    draw_board()
    while not finish:
        comp_func()
        finish = check_status(board)
        if finish == 'o':
            print('Computer wins')
            break
        elif finish == 'tie':
            print('Tie')
            break
        p1_func()
        finish = check_status(board)
        if finish == 'x':
            print('Player wins')
            break
        elif finish == 'tie':
            print('Tie')
            break


def play_a_new_game():
    while True:
        first = input('Who goes first? p for Player, c for Computer: ')
        if first == 'p' or first == 'P':
            player_first()
            break
        elif first == 'c' or first == 'C':
            comp_first()
        else:
            print('try again')


if __name__ == '__main__':
    play_a_new_game()
