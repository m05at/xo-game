import random

def printboard(bo):
    print(' -----------')
    print('  ' + bo[1] + ' | ' + bo[2] + ' | ' + bo[3])
    print(' -----------')
    print('  ' + bo[4] + ' | ' + bo[5] + ' | ' + bo[6])
    print(' -----------')
    print('  ' + bo[7] + ' | ' + bo[8] + ' | ' + bo[9])
    print(' -----------')


def choose():
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        letter = input('Do you want be X or O : ').upper()

    if letter == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def isEmpty(bo,i):
    return bo[i] == ' '
def playermove():
    move = 0
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isEmpty(board, int(move)):
        move = input('What\'s your move? (1-9)')
    return int(move)

def isWinner(bo, le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le)
    or (bo[4] == le and bo[5] == le and bo[6] == le)
    or (bo[7] == le and bo[8] == le and bo[9] == le)
    or (bo[1] == le and bo[4] == le and bo[7] == le)
    or (bo[2] == le and bo[5] == le and bo[8] == le)
    or (bo[3] == le and bo[6] == le and bo[9] == le)
    or (bo[1] == le and bo[5] == le and bo[9] == le)
    or (bo[3] == le and bo[5] == le and bo[7] == le))

def isBoardFilled(bo):
    if bo.count(' ')  == 1:
        return True

def copyboard(bo):
    copy = []
    for i in bo:
        copy.append(i)
    return copy

def chooseRandomMove(bo, moves):
    a = []
    for i in moves:
        if bo[i] == ' ':
            a.append(i)
    if len(a) == 0:
        print('None')
        return None
    else:
        return random.choice(a)

def choosemode():
    mode = ''
    while not (mode.startswith('e') or mode.startswith('h')):
        mode = input('Easy or Hard : ').lower()
    return mode[0]

def hardcompmove(bo, comp, player):
    for i in range(1,10):
        copy = copyboard(bo)
        if copy[i] == ' ':
            copy[i] = comp
            if isWinner(copy, comp):
                return i

    for i in range(1,10):
        copy = copyboard(bo)
        if copy[i] == ' ':
            copy[i] = player
            if isWinner(copy, player):
                return i

    move = chooseRandomMove(bo,[1,3,7,9])
    if move != None:
        return move

    if bo[5] == ' ':
        return 5

    return chooseRandomMove(bo, [2,4,6,8])
while True:
    board = [' ' for i in range(10)]
    player,computer = choose()
    mode = choosemode()
    if player == 'X':
        turn = 'player'
    else:
        turn = 'comp'
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            printboard(board)
            move = playermove()
            board[move] = player
            if isWinner(board, player):
                printboard(board)
                print('You win!')
                gameIsPlaying = False
            elif isBoardFilled(board):
                printboard(board)
                print('The game\'s a tie')
                gameIsPlaying = False
            else:
                turn = 'comp'
        else:
            if mode == 'e':
                move = chooseRandomMove(board,[1,2,3,4,5,6,7,8,9])
            else:
                move = hardcompmove(board, computer, player)
            board[move] = computer
            if isWinner(board, computer):
                printboard(board)
                print('The computer wins! You lose.')
                gameIsPlaying = False
            elif isBoardFilled(board):
                printboard(board)
                print('The game\'s a tie')
                gameIsPlaying = False
            else:
                turn = 'player'
    
    y = input('Do you want to play again? (yes or no)')
    if not y.lower().startswith('y'):
        break