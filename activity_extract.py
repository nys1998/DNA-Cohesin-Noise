from math import dist
from turtle import distance
import numpy as np
import os

for n in [160]:
    sticky_file = os.curdir + f'\\{n}\\5\\chromatincolours.dat'
    sticky_dict = {}
    sum_dict = {}
    for m in range(5,35,5):
        sticky_array = []
        all_array = []
        with open(sticky_file,'r') as f:
            for line in f:
                text = line.split()
                if int(text[1]) == 4:
                    sticky_array .append(int(text[0]))
                    sticky_dict[text[0]] = []
                    sum_dict[text[0]] = [] 

        def Check_State(stickyvec,onprotein):
            n_onprotein = len(onprotein)
            if n_onprotein == 0:
                return 0 
            onprotein_copy = np.copy(onprotein)
            for i in range(3):
                temp = np.zeros([n_onprotein,3])
                temp[:,i] = 100 # Box size

                for j in [-1,1]:
                    ghostprotein = onprotein_copy + j*temp
                    onprotein = np.concatenate((onprotein,ghostprotein),axis = 0)

            difference = np.subtract(onprotein,stickyvec)
            difference = np.square(difference)
            difference = np.sum(difference,axis=1)
            difference = np.sqrt(difference)
            difference = np.sum((difference < 3.5))
            if difference > 0:
                return 1
            else:
                return 0     

        for i in range(101,201):
            filename = os.curdir + f"\\{n}\\{m}\\Red\\Omnigenic." + str(i) + ".lammpstrj"
            timestep = 0
            with open(filename,'r') as f:
                atom_count = 0
                sticky = []
                on_protein = []
                sticky_coordinate = []
                on_protein_coordinate = []
                for line in f:
                    cur_line = line.split()
                    if "timestep" in line.lower():
                        if timestep > 0:
                            header = ""
                            sticky_coordinate = np.array(sticky_coordinate)
                            on_protein_coordinate = np.array(on_protein_coordinate)
                            for j in range(len(sticky)):
                                sticky_dict[str(sticky[j]-2*m)].append(Check_State(sticky_coordinate[j,:],on_protein_coordinate))
                            sticky = []
                            on_protein = []
                            sticky_coordinate = []
                            on_protein_coordinate = []
                        timestep += 1
                    if len(cur_line) == 8:
                        if cur_line[1] == '1':
                            on_protein.append(int(cur_line[0]))
                            coordinate = []
                            for k in range(3):
                                coordinate.append(float(cur_line[2+k]))
                            on_protein_coordinate.append(coordinate)
                            

                        if cur_line[1] == '4':
                            sticky.append(int(cur_line[0]))
                            coordinate = []
                            for k in range(3):
                                coordinate.append(float(cur_line[2+k]))
                            sticky_coordinate.append(coordinate)
            try:
                os.mkdir(os.curdir + f"\\{n}\\{m}\\output")
            except:
                pass

            save_name = os.curdir + f"\\{n}\\{m}\\output\\sticky_state_" + str(i) + ".dat"
            g = open(save_name,'w')

            for key in sticky_dict:
                temp = []
                row = key + " "
                sum = 0
                for item in sticky_dict[key]:
                    row += str(item) + " "
                    sum += item
                row += "\n"
                g.write(row)
                sum_dict[key].append(sum)
            g.close()
            sticky_dict = {k : [] for k in sticky_dict}

        h = open(os.curdir + f"\\{n}\\{m}\\output\\total.dat",'w')

        average_dict = {}
        for key in sum_dict:
            temp = []
            row = key + " "
            sum = 0
            for item in sum_dict[key]:
                row += str(item) + " "
                sum += item
                all_array.append(item)
            average = sum/100
            average_dict[key] = average
            row += "\n"
            h.write(row)
        avg = np.average(all_array)
        std = np.std(all_array)
        h.write(f"Average: {avg} \n")
        h.write(f"Standard Deviation: {std}\n")
        h.close()
                
        h = open(os.curdir + f"\\{n}\\{m}\\output\\correlation.dat",'w')

        row = ""
        for i in range(len(sticky_array)):
            row += str(sticky_array[i]) + " "
        row += "\n"
        h.write(row)
        row = ""
        for i in range(len(sticky_array)):
            distance_to_next = 0
            if i == 0:
                distance_to_next = abs(sticky_array[1]-sticky_array[0])
            elif i == len(sticky_array)-1:
                distance_to_next = abs(sticky_array[-1]-sticky_array[-2])
            else:
                distance_to_next = abs(sticky_array[i+1]-sticky_array[i])
                if distance_to_next > abs(sticky_array[i-1]-sticky_array[i]):
                    distance_to_next =  abs(sticky_array[i-1]-sticky_array[i])
            row += str(distance_to_next) + " "
        row += "\n"
        h.write(row)
        row = ""
        for i in range(len(sticky_array)):
            row += str(average_dict[str(sticky_array[i])]) + " "
        h.write(row)
        h.close()