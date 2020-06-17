import random

def mutate(net):
    n_net = []
    for i in range(len(net)):
        n_net.append([])
        for j in range(len(net[i])):
            if random.random() < 0.25:
                n_net[-1].append(random.random())
            else:
                n_net[-1].append(net[i][j])
    return n_net
                
def crossover(net1, net2):
    n_net = []
    for i in range(len(net1)):
        n_net.append([])
        for j in range(len(net1[i])):
            pos = random.random()
            if pos < 0.45:
                n_net[-1].append(net1[i][j])
            elif pos < 0.9:
                n_net[-1].append(net2[i][j])
            else:
                n_net[-1].append(net1[i][j] * 0.5 + net2[i][j] * 0.5)
    return n_net