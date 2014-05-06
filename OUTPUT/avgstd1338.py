# this routine creates a file with 3 columns: (1) the counter of 1338 obj, (2) the avg (x0) and (3) the stdev (sigma)
import math
import fileinput
import sys
from scipy.optimize import curve_fit
import gaussian
import scipy
import numpy as np

counter=0
nobjects = 1338
for i in range(1, nobjects + 1):
    filename = str(i) + '.pz'
    counter += 1
    
    data = open(filename,'r') #reading counter of obj from stdev.py
    #popt = open('gaussian.py', 'r') #reading x0 and sigma from gaussian.py
    


    outfile = open('3colAvgStdev.py', 'w') #writing to 3colAvgStdev.py
    
        for line in data.readlines():
        #if filename[-3:]=='.pz':
        #counter += 1
            
            for line in popt.readlines():
                if not line.startswith(('#')):
                    dummy, dummy, x0, sigma = map(float, line.split())
                        #taking only values that we will write



            outfile.write("%s \t" % (counter)) #writing counter from outfile to 3colAvgStdev.py
            popt.write("%s \t %s \n" % (x0, sigma)) #writing x0 and sigma from popt

data.close()
outfile.close()