# Hi Professor Liu! This is a routine I created to sort of "clear up" Vivi's Correspondence file below and transfer only those values that I need into my 585.txt file. Please email me if you want me to clear anything up here. This file was only used for my reference, to make it easier to look at. ;)
#!/usr/bin/python
import math
import fileinput
import sys
import average
import gaussian
from scipy.optimize import curve_fit
import scipy


data = open('Correspondence_all_gold.dat', 'r') #readimg from this file
outfile = open('585gold.txt', 'w') #writing to 585gold.txt

counter = 0

for line in data.readlines():
    
    index, galaxy_number = map(int, line.split()) #this line reads in all the input, splitting them on a blank space
       
    
            
    if galaxy_number > 0:
        counter += 1
        
        outfile.write("%s \t %s \n" % (counter, index))  #writing values from data to outfile
data.close()
outfile.close()

