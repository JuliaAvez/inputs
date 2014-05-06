
#!/usr/bin/python
import math
import fileinput
import sys
from gold import *
import os

counter=0
nobjects = 1338
for i in range(1, nobjects + 1):
    filename = str(i) + '.pz'
    #filename stands for all of the files in OUTPUT that end in .pz
    data = open (filename, 'r')
#data = open('1.pz','r')

# Hi Professor Liu! This is the routine that I used to convert the best samples into what we called the Gold distribution.
    
    probdist= open(str(i) + 'candels.txt', 'w') #creating to write z and pz from data to this file (redshift prob dist for 1338 obj)
    
    
#linenumb= file_len('CANDELS_GOODSS_Specz.dat') # counts number of lines
#print linenumb

    for line in data.readlines():
        if not line.startswith(('#')):
            counter += 1

            z, dummy, dummy, pz = map(float, line.split()) #this line reads in all the input, splitting them on a blank space
       
        
            probdist.write("%s \t %s \n" % (z, pz)) #takes just z and pz values

    data.close()
    probdist.close()

#-----------------------------------------------------------------------------------
          
            #from here on in, we write only the golden redshift prob dist to a new file name
gold = [] #created a vector, gold (empty list)
golden_sample = open('585gold.txt','r')
for line in golden_sample.readlines():

    dummy, galaxygold = map(int, line.split())
    gold.append(galaxygold) #we appended the list of gold galaxy numbers (16 for 1st) to gold vector


#counter = 0

nobjects = 585
for i in range(1, nobjects + 1):
    filename_gold = str(gold[i-1]) + '.pz' #using filename
    #goldist = open(str(i) + 'gold.pz','w') #creating to write gold sample to these files
    #data_gold = open(filename, 'r') #reading from this file
        #for line in data_gold.readlines():
        #if not line.startswith(('#')):
        #if index in gold:
    os.system('cp '+str(gold[i-1])+'.pz '+str(i) + 'gold.pz')
                #os.system('cp '+filename+'.pz ')
                
    #counter += 1

#index, gold_galaxy_number = map(float, line.split()) #this line reads in all the input, splitting them on a blank space
                
                
#goldist.write("%s \t %s \n" % (z, pz)) #takes just z and pz values

        
        
#data_gold.close()
golden_sample.close()
#goldist.close()
