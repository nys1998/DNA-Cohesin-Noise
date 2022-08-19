from math import dist
from turtle import distance
import numpy as np
import os

for n in [240]:
    sticky_file =  os.curdir + f'\\{n}\\5\\chromatincolours.dat'

    for m in [5,10,15,20,25,30]:
        sticky_dict = {}
        sticky_array = []
        all_array = []
        count = 0
        with open(sticky_file,'r') as f:
            for line in f:
                text = line.split()
                if int(text[1]) == 4:
                    sticky_array .append(int(text[0]))
                    sticky_dict[int(text[0])] = count 
                    count += 1
        total_mat = np.zeros((len(sticky_array),len(sticky_array)))


        for i in range(101,201):
            path = os.curdir + f"\\{n}\\{m}"
            try:
                os.mkdir(path + "\\Contact")
            except:
                pass
            filename = path + "\\Red\\Omnigenic." + str(i) + ".lammpstrj"
            timestep = 0
            sticky_mat = np.zeros((len(sticky_array),len(sticky_array)))
            sticky_coordinate = np.zeros((len(sticky_array),3))
            with open(filename,'r') as f:
                for line in f:
                    cur_line = line.split()
                    if "timestep" in line.lower():
                        if timestep > 0:
                            for j in range(1,len(sticky_array)):
                                temp = sticky_coordinate - np.roll(sticky_coordinate,shift=-j,axis = 0)
                                temp = np.sqrt(np.sum(np.square(temp),axis=1)) < 3.5
                                for k in range(len(temp)):
                                    if temp[k]:
                                        v = k+j
                                        if v >= len(temp):
                                            v = v -len(temp)
                                        sticky_mat[k][v] = sticky_mat[k][v] + 1
                                        total_mat[k][v] = total_mat[k][v] + 1
                            sticky_coordinate = np.zeros((len(sticky_array),3))
                        timestep += 1
                    if len(cur_line) == 8:
                        if cur_line[1] == '4':
                            for k in range(3):
                                sticky_coordinate[sticky_dict[int(cur_line[0])-2*m],k]=(float(cur_line[2+k]))
            g = open(path + f"\\Contact\\contact_{i}.dat",'w')
            g.write('\t')
            for j in range(len(temp)):
                g.write(f'{sticky_array[j]}\t')
            g.write('\n')
            for j in range(len(temp)):
                g.write(f'{sticky_array[j]}\t')
                for k in range(len(temp)):
                    g.write(f'{int(sticky_mat[j][k])}\t')
                g.write('\n')
            g.close()

        g = open(os.curdir + f"\\{n}\\{m}"+ f"\\allcontact.dat",'w')
        g.write('\t')
        for j in range(len(temp)):
            g.write(f'{sticky_array[j]}\t')
        g.write('\n')
        for j in range(len(temp)):
            g.write(f'{sticky_array[j]}\t')
            for k in range(len(temp)):
                g.write(f'{int(total_mat[j][k])}\t')
            g.write('\n')    
        g.close()
