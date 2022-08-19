import numpy as np
import matplotlib.pyplot as plt
import os

for k in [10,20,30,40,60,80,160,240]:
    file = f'.\\{k}\\allcontact_pp.dat'
    f = np.loadtxt(file)
    print(f"{k} {np.mean(f)}")
    for i in range(20):
        f[i,i] = 1
    plt.clf()
    plt.imshow(f,vmin = 0, vmax = 1)
    plt.colorbar()
    plt.title(f'{k}')
    plt.savefig(f'contactmap_{k}_loop.png', format = 'png',bbox_inches='tight')
