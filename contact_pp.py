from math import dist
from turtle import distance
import numpy as np  
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

mean_vec = []
std_vec = []
spacing_array = [10,20,30,40,60,80,160,240]
mat = []

def powerlaw(x,a,b):
    return a*np.log(x)+b

def explaw(x,a,b):
    return a*np.exp(b*x)
    
l = open('contactdistance_all.dat','w')
for n in spacing_array:
    n_mat = np.zeros((20,20))
    probability = {i : [] for i in range(1,20)}
    for m in [5 ,10,15,20,25,30]:
        m_mat = np.zeros((20,20))
        path = os.curdir + f"\\{n}\\{m}\\"
        filename = path + "allcontact.dat"
        with open(filename,'r') as f:
            data = f.read().split('\n')
            count = 0
            vec = []
            for line in data:
                if count == 0: 
                    count += 1
                    continue
                line = line.split('\t')
                if len(line) == 1: continue
                line.pop()
                temp = np.array([int(line[i]) for i in range(1,len(line))])
                temp = temp
                for k in range(1,len(line)):
                    m_mat[count-1,k-1] = temp[k-1]
                    n_mat[count-1,k-1] += temp[k-1]
                    d = abs(count - k)
                    if d == 0: continue
                    probability[d].append(temp[k-1])
                count += 1  
        m_mat = m_mat/np.max(m_mat)
        g = open(path + "allcontact_pp.dat",'w')
        for i in range(20):
            for j in range(20):
                g.write(f"{np.round(m_mat[i][j],3)}\t")
            g.write('\n')   
        g.close()
    
    n_mat = n_mat/np.max(n_mat)
    f = open(os.curdir + f"\\{n}\\""allcontact_pp.dat",'w')
    for i in range(20):
        for j in range(20):
            f.write(f"{np.round(n_mat[i][j],3)}\t")
        f.write('\n')  
    f.close()

    g = open(os.curdir + f"\\{n}\\contactdistance.dat",'w')
    vec = []
    sum = 0
   

# mat = np.transpose(np.array(mat))
# np.savetxt('contactprobability_all.dat',mat)
# # plt.xlabel('Spacing')
# # plt.ylabel('Average Contacted Bead Distance')
# # plt.legend()
# # plt.show()
# plt.xlabel('Sticky Bead Distance')
# plt.ylabel('Contact Probability')
# plt.legend()
# plt.show()


