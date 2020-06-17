from CONSTS import *
import random
import math

def load(file_str):
    n = [[], [], [], [], []]
    f = open(file_str)
    s_s = f.readlines()
    for i in range(SIZE):
        n[0].append(0)
    n[1] = list(map(float, s_s[1].split()))[:]
    n[2] = list(map(float, s_s[2].split()))[:]
    n[3] = list(map(float, s_s[3].split()))[:]
    n[4] = list(map(float, s_s[4].split()))[:]
    f.close()
    return n
    
def generate():
    n = [[], [], [], [], []]
    for i in range(SIZE):
        n[0].append(0)
    for i in range(SIZE):
        n[4].append(random.randint(10, 60) / 10 * random.choice([1, -1]))
    for i in range(HIDDEN):
        n[2].append(random.randint(10, 60) / 10 * random.choice([1, -1]))
    for i in range(SIZE * HIDDEN):
        n[1].append(random.random() * random.choice([1, -1]))
    for i in range(SIZE * HIDDEN):
        n[3].append(random.random() * random.choice([1, -1]))
    return n

def save(file_str, n):
    f = open(file_str, "w")
    for i in range(5):
        f.write(' '.join(list(map(str, n[i]))) + '\n')
    f.close()
    return n 

def sigmoid_derivative(x):
    return 1 - math.tanh(x) ** 2

def getCoords(mode, board, net):
    nn = []
    if mode == 'x':
        for j in board:
            for i in j:
                if i == ' ':
                    nn.extend([0])
                elif i == 'x':
                    nn.extend([-1])
                else:
                    nn.extend([1])
    else:
        for j in board:
            for i in j:
                if i == ' ':
                    nn.extend([0])
                elif i == 'x':
                    nn.extend([1])
                else:
                    nn.extend([-1])
    n_net = net[:]
    n_net[0] = nn
    del n_net[3]
    del n_net[1]
    for i in range(SIZE):
        for j in range(HIDDEN):
            n_net[1][j] += n_net[0][i] * net[1][i * A_SIDE + j]
    for i in range(HIDDEN):
        n_net[1][i] = math.tanh(n_net[1][i])
    for i in range(HIDDEN):
        for j in range(SIZE):
            n_net[2][j] += n_net[1][i] * net[3][i * A_SIDE + j]
    for i in range(SIZE):
        n_net[2][i] = math.tanh(n_net[1][i])
    for i in range(A_SIDE):
        for j in range(A_SIDE):
            if board[i][j] == ' ':
                maxC = i * A_SIDE + j
                maxN = n_net[2][maxC]
                break
        else:
            continue
        break
    for i in range(0, SIZE):
        if n_net[2][i] > maxN and board[i // A_SIDE][i % A_SIDE] == ' ':
            maxN = n_net[2][i]
            maxC = i
    return [maxC // A_SIDE, maxC % A_SIDE]

def learn_no(n, n_board, is_win):
    cnt = 0
    for i in range(A_SIDE):
        for j in range(A_SIDE):
            if n_board[i][j] != ' ':
                cnt += 1
    error = -(is_win) * cnt * sigmoid_derivative(is_win)
    for i in range(HIDDEN):
        j = i % HIDDEN
        n[2][j] += error
    return n