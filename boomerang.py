import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

x_all = []
y_all = []
for n in [10,20,30,40,60,80,160,240]:
    mat = []
    plt.axis([0,100,10,35])
    g = open(f'{n}_boomerang.dat','w')
    vec = []
    x = []
    y = []
    sticky_file = os.curdir + f'\\{n}\\5\\chromatincolours.dat'
    std_dict = {}
    avg_dict = {}
    for i in range(5,35,5):
        std_dict[i] = []
        avg_dict[i] = []
        filename = os.curdir + f"\\{n}\\{i}.dat"
        with open(filename, 'r') as f:
            text = f.read().split('\n')
            for line in text:
                line = line.split()
                if len(line) == 4 or len(line) == 0: break
                vec.append([float(line[1]),float(line[2])])
                x.append(float(line[1]))
                y.append(float(line[2]))
                g.write(f"{line[1]} {line[2]}\n")
        mat.append(vec)
    x_all.append(x)
    y_all.append(y)
    plt.scatter(x,y, label = f"{n}")
g = open('BoomerangAllDat.dat','w') 
for i in range(len(x)):
    for j in range(len(x_all)):
        g.write(str(x_all[j][i]))
        g.write(' ')
        g.write(str(y_all[j][i]))
        g.write(' ')
    g.write('\n')
g.close()
plt.ylim(0,40)
plt.legend()
plt.show()

