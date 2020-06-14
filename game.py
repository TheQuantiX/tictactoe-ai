from CONSTS import *
import nnet
import time
import colorama
from termcolor import colored, cprint

def CheckVictoryX(board, x, y): # Where x, y are the coordinates of the last move
    for i in range(A_SIDE):
        if board[0][i] == ('x') and board[1][i] == ('x') and board [2][i] == ('x'):
            return -1
        if board[0][i] == ('o') and board[1][i] == ('o') and board [2][i] == ('o'):
            return 1
        if board[i][0] == ('x') and board[i][1] == ('x') and board [i][2] == ('x'):
            return -1
        if board[i][0] == ('o') and board[i][1] == ('o') and board [i][2] == ('o'):
            return 1
    if board[0][0] == ('x') and board[1][1] == ('x') and board [2][2] == ('x'):
        return -1
    if board[0][0] == ('o') and board[1][1] == ('o') and board [2][2] == ('o'):
        return 1
    if board[0][2] == ('x') and board[1][1] == ('x') and board [2][0] == ('x'):
        return -1
    if board[0][2] == ('o') and board[1][1] == ('o') and board [2][0] == ('o'):
        return 1
    for i in range(A_SIDE):
        for j in range(A_SIDE):
            if (board[i][j] == ' '):
                return None
    return 0

def CheckVictoryO(board, x, y): # Where x, y are the coordinates of the last move
    for i in range(A_SIDE):
        if board[0][i] == ('x') and board[1][i] == ('x') and board [2][i] == ('x'):
            return 1
        if board[0][i] == ('o') and board[1][i] == ('o') and board [2][i] == ('o'):
            return -1
        if board[i][0] == ('x') and board[i][1] == ('x') and board [i][2] == ('x'):
            return 1
        if board[i][0] == ('o') and board[i][1] == ('o') and board [i][2] == ('o'):
            return -1
    if board[0][0] == ('x') and board[1][1] == ('x') and board [2][2] == ('x'):
        return 1
    if board[0][0] == ('o') and board[1][1] == ('o') and board [2][2] == ('o'):
        return -1
    if board[0][2] == ('x') and board[1][1] == ('x') and board [2][0] == ('x'):
        return 1
    if board[0][2] == ('o') and board[1][1] == ('o') and board [2][0] == ('o'):
        return -1
    for i in range(A_SIDE):
        for j in range(A_SIDE):
            if (board[i][j] == ' '):
                return None
    return 0

def getCoords():
    while True:
        aaa = input("Print coordinates of your turn (x and y): ").split()
        if len(aaa) != 2:
            cprint("Error: ", 'red', attrs = ['bold'], end = '')
            print('invalid number of arguments.')
            continue
        if aaa[0] in '123' and aaa[1] in '123':
            return [int(aaa[0]) - 1, int(aaa[1]) - 1]
        else:
            cprint("Invalid input. Format = 'x y'. Try again.", 'red')
            
def printBoard(mode, board):
    for i in range(A_SIDE):
        for j in range(A_SIDE):
            if board[i][j] == ' ':
                print('_', end=' ')
            elif board[i][j] == 'x':
                if mode == 'x':
                    cprint(board[i][j], 'green', end=' ')
                else:
                    cprint(board[i][j], 'red', end=' ')
            else:
                if mode == 'o':
                    cprint(board[i][j], 'green', end=' ')
                else:
                    cprint(board[i][j], 'red', end=' ')
        print()

def play(mode, board, net):
    colorama.init()
    x = y = 0
    if (mode == 'x'):
        mymode = 'x'
        while CheckVictoryX(board, x, y) == None:
            if mymode == 'o':
                print("Getting coordinates from the AI...")
                time.sleep(3.0)
                coords = nnet.getCoords(mode, board, net)
                x, y = coords[0], coords[1]
                if board[x][y] != ' ':
                    return [board, -1]
                else:
                    board[x][y] = 'o'
                mymode = 'x'
            else:
                arr = getCoords()
                x, y = arr[0], arr[1]
                if board[x][y] != ' ':
                    return [board, 1]
                else:
                    board[x][y] = 'x'
                mymode = 'o'
            printBoard('x', board)
        return [board, CheckVictoryX(board, x, y)]
    else:
        mymode = 'x'
        while CheckVictoryO(board, x, y) == None:
            if mymode == 'o':
                arr = getCoords()
                x, y = arr[0], arr[1]
                if board[x][y] != ' ':
                    return [board, 1]
                else:
                    board[x][y] = 'o'
                mymode = 'x'
            else:
                print("Getting coordinates from the AI...")
                time.sleep(3.0)
                coords = nnet.getCoords(mode, board, net)
                x, y = coords[0], coords[1]
                if board[x][y] != ' ':
                    return [board, -1]
                else:
                    board[x][y] = 'x'
                mymode = 'o'
            printBoard('o', board)
        return [board, CheckVictoryO(board, x, y)]
    
def play_netvnet(mode, board, net1, net2):
    x = y = 0
    if (mode == 'x'):
        mymode = 'x'
        while CheckVictoryX(board, x, y) == None:
            if mymode == 'o':
                #print("Getting coordinates from the AI...")
                #time.sleep(3.0)
                coords = nnet.getCoords(mode, board, net1)
                x, y = coords[0], coords[1]
                if board[x][y] != ' ':
                    return [board, -1]
                else:
                    board[x][y] = 'o'
                mymode = 'x'
            else:
                #print("Getting coordinates from the AI...")
                #time.sleep(3.0)
                arr = nnet.getCoords(mode, board, net2)
                x, y = arr[0], arr[1]
                if board[x][y] != ' ':
                    return [board, 1]
                else:
                    board[x][y] = 'x'
                mymode = 'o'
            #printBoard(board)
        return [board, CheckVictoryX(board, x, y)]
    else:
        mymode = 'x'
        while CheckVictoryO(board, x, y) == None:
            if mymode == 'o':
                #print("Getting coordinates from the AI...")
                #time.sleep(3.0)
                arr = nnet.getCoords(mode, board, net2)
                x, y = arr[0], arr[1]
                if board[x][y] != ' ':
                    return [board, 1]
                else:
                    board[x][y] = 'o'
                mymode = 'x'
            else:
                #print("Getting coordinates from the AI...")
                #time.sleep(3.0)
                coords = nnet.getCoords(mode, board, net1)
                x, y = coords[0], coords[1]
                if board[x][y] != ' ':
                    return [board, -1]
                else:
                    board[x][y] = 'x'
                mymode = 'o'
            #printBoard(board)
        return [board, CheckVictoryO(board, x, y)]