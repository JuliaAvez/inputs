#!/usr/bin/python
import math
import fileinput
import sys

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)


data = open('photz.zout','r') #

speczfile = open('CANDELS_GOODSS_Specz.dat','r') #we are creating this file so we open it for writing

specz= speczfile.readlines() #starts from 0
speczfile.close()
counter=0

outfile= open('2coloutfile.zout', 'w')
for line in data.readlines():
    if not line.startswith(('#')):
        counter += 1
        
        id, dummy, dummy, dummy, dummy, dummy, dummy, z_m2, dummy, l68, u68, l95, u95, dummy, dummy, dummy= map(float, line.split()) #this line reads in all the input, splitting them on a blank space
        
        diff68= (z_m2-float(specz[counter-1]))/((u68-l68)/2)
        
        
        
        
        
        outfile.write("%s \t %s \n" % (counter, diff68))
        

data.close()

outfile.close()