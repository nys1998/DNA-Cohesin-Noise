import numpy as np
import os

for n in [10,20,30,40,60,80,160,240  ]:
    for m in range(5,35,5):
        filename = os.curdir + f"/{n}/{m}/output/total.dat" 
        h = open(os.curdir + f"/{n}/{m}/output/stddev.dat",'w' )
        k = open(os.curdir + f"/{n}/{m}.dat",'w')
        with open(filename,'r') as f:
            data = f.read()
            data = data.split('\n')
            stdvec = []
            for line in data:
                split = line.split()
                if len(split) < 5:
                    break

                site = split[0]
                vec = [int(split[i]) for i in range(1,len(split))]
                avg = np.average(vec)
                std = np.std(vec)
                h.write(f"{site} {avg} {std}\n")
                k.write(f"{site} {avg} {std}\n")
                stdvec.append(std)
            stdavg = np.average(stdvec)
            h.write(f"Average standard deviation: {stdavg}")
        h.close()
        k.close()

        
