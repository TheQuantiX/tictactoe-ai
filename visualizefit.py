import matplotlib.pyplot as plt

f = open('topfitness.txt')
a = f.readlines()[1:]
a = list(map(lambda x : int(x.split(',')[1]), a))
f.close()

plt.plot(a)
plt.xlabel('generation number')
plt.ylabel('fitness value')
plt.show()
