''' 
    Neural network for playing Tic-Tac-Toe by Denis Tereshchenko
'''

import nnet # Stands for neural network
from CONSTS import * # All necessary constants
import game
import time
import genetic
import random
import colorama
from termcolor import colored, cprint
import sys

def to_int(v):
    try:
        i = int(v)
        return i
    except:  
        return None

def getXO():
    while True:
        s = input("Choose X or O: ")
        if (s == "x" or s == "o" or s == "X" or s == "O"):
            return s
        else:
            print("Invalid input. Try again.")

def printOK(end = '\n'):
    cprint('OK', 'green', end = end)
    
def training():
    if len(sys.argv) < 2:
        my_arg = 0
    else:
        my_arg = to_int(sys.argv[1])
    
    colorama.init()
    
    if my_arg == None:
        cprint('Error: ', 'red', attrs = ['bold'], end = '')
        print('expected int argument. Usage: python training <generation>.')
    
    n = []
    fitness = []
    if not WAS_FILE:
        print("Generating networks... ", end="\t")
        for i in range(50):
            n.append(nnet.generate())
            fitness.append(0)
        printOK()
    else:
        print("Loading networks... ", end="\t")
        for i in range(50):
            n.append(nnet.load("data/data{}.txt".format(i)))
            fitness.append(0)
        printOK()
    
    with open("gen.txt") as f0:
            gen_num = float(f0.readlines()[0])
        
    while True:
        for i in range(50):
            fitness[i] = 0
        print("Comparing networks... ", end="\t")
        tim = time.time()
        for i in range(49):
            for j in range(i + 1, 50):
                s = random.randint(0, 1)
                board = []
                for i1 in range(A_SIDE):
                    board.append([])
                    for j1 in range(A_SIDE):
                        board[i1].append(' ')
                if s == 0:
                    a = game.play_netvnet('x', board, n[i], n[j])
                    n_board = a[0]
                    fitness[i] += a[1]
                    fitness[j] -= a[1]
                else:
                    a = game.play_netvnet('o', board, n[i], n[j])
                    n_board = a[0]
                    fitness[i] += a[1]
                    fitness[j] -= a[1]
        printOK(end = ' ')
        print('(done in {} seconds)'.format(round(time.time() - tim, 5)))
        print("Creating generation {}... ".format(int(gen_num)), end="\t")
        gen_num += 1
        agent = []
        for i in range(50):
            agent.append([fitness[i], n[i]])
        agent.sort(key = lambda x: x[0])
        agent = agent[::-1]
        agent = agent[:random.randint(5, 8)]
        n = []
        for i in range(len(agent)):
            n.append(agent[i][1])
        siz = len(agent)
        for i in range(50 - len(agent)):
            aaa = random.random()
            if aaa < 0.2:
                n.append(genetic.mutate(n[random.randint(0, siz - 1)]))
            else:
                n.append(genetic.crossover(n[random.randint(0, siz - 1)], n[random.randint(0, siz - 1)]))
        printOK()
        
        print("Saving networks... ", end="\t")
        with open("wasfile.txt", "w") as f:
            f.write("True")
            
        for i in range(50):
            nnet.save("data/data{}.txt".format(i), n[i])
            
        fit = open("topfitness.txt", "a")
        fit.write('{},{}\n'.format(str(gen_num), str(agent[0][0])))
        fit.close()
        
        printOK()
        
        with open("gen.txt", "w") as fgen:
            fgen.write(str(gen_num - 1))
        if gen_num > my_arg:
            v = input("Do you want to train them further? (y/n) ")
            if v == "n" or v == "N" or v == "no" or v == "No" or v == "nO" or v == "NO":
                print("Goodbye!")
                break


if __name__ == "__main__":
    training()