''' 
    Neural network for playing Tic-Tac-Toe by Denis Tereshchenko
'''

import nnet # Stands for neural network
from CONSTS import * # All necessary constants
import game
import colorama
from termcolor import colored, cprint


def getXO():
    while True:
        s = input("Choose X or O: ")
        if (s == "x" or s == "o" or s == "X" or s == "O"):
            return s
        else:
            cprint('Invalid input. Try again.', 'red')

def printOK():
    cprint('OK', 'green')
    
def main():
    colorama.init()
    
    n = []
    
    print("Loading networks... ", end="\t")
    n = nnet.load("data/data0.txt")
    printOK()
        
    while True:
        s = getXO()
        board = []
        for i in range(A_SIDE):
            board.append([])
            for j in range(A_SIDE):
                board[i].append(' ')
        if s == 'x' or s == 'X':
            a = game.play('x', board, n)
            n_board = a[0]
            is_win = a[1]
        else:
            a = game.play('o', board, n)
            n_board = a[0]
            is_win = a[1]
        if is_win == -1:
            cprint('You won!\n', 'green')
        elif is_win == 0:
            print('Draw!')
        else:
            cprint('AI won!', 'red')
        v = input("Do you want to try again? (y/n) ")
        if v == "n" or v == "N" or v == "no" or v == "No" or v == "nO" or v == "NO":
            print("Goodbye!")
            break
    
if __name__ == "__main__":
    main()