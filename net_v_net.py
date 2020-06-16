''' 
    Neural network for playing Tic-Tac-Toe by Denis Tereshchenko
'''

import nnet # Stands for neural network
from CONSTS import * # All necessary constants
import game
import colorama
import random
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
    n.append(nnet.load("data/data0.txt"))
    n.append(nnet.load("data/data1.txt"))
    printOK()
        
    while True:
        s = random.choice(['x', 'o'])
        board = []
        for i in range(A_SIDE):
            board.append([])
            for j in range(A_SIDE):
                board[i].append(' ')
        if s == 'x' or s == 'X':
            a = game.play_netvnet_vis('x', board, n[0], n[1])
            n_board = a[0]
            is_win = a[1]
        else:
            a = game.play_netvnet_vis('o', board, n[0], n[1])
            n_board = a[0]
            is_win = a[1]
        if is_win == -1:
            cprint('AI #1 won!\n', 'green')
        elif is_win == 0:
            print('Draw!')
        else:
            cprint('AI #2 won!', 'red')
        v = input("Do you want to try again? (y/n) ")
        if v == "n" or v == "N" or v == "no" or v == "No" or v == "nO" or v == "NO":
            print("Goodbye!")
            break
    
if __name__ == "__main__":
    main()