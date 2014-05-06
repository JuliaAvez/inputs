
#!/usr/bin/python
import math
import fileinput
import sys
import average
import gaussian
from scipy.optimize import curve_fit
import scipy

outfile = open('GoldAmpAvgStdev.txt', 'w') #writing to GoldAmpAvgStdev.py


nobjects = 585
for i in range(1, nobjects + 1):
    filename = str(i) + 'gold.pz'
    #filename stands for all of the files in OUTPUT that end in .pz
    data = open (filename, 'r')
#data = open('1.pz','r')
    x_z = [] #has to be inside for loop so objects will be defined
    y_pz = []

    

    for line in data.readlines():
        if not line.startswith(('#')):
            

            z, dummy, dummy, pz = map(float, line.split()) #this line reads in all the input, splitting them on a blank space
       
        
            
            
            if pz > .001:
                
                y_pz.append(pz)
                x_z.append(z)

    if len(y_pz) > 0:
        #print(x_z)
        #print(average.avg(x_z))
        
        #print(average.stdev(x_z))  not using this bc we are not taking the stdev of just the x_z values, we want to fit the distribution to a gaussian

        #popt, pcov = curve_fit(gaussian.gauss_function, x_z, y_pz) #optimizes parameters
        #print (i)
        try:
            popt,pcov = scipy.optimize.curve_fit(gaussian.gauss_function, x_z, y_pz,p0= [1,(average.avg(x_z)), .3]) #the try-except error handling procedure is to exceed the max call to fcn of 800 times

        except RuntimeError:
            print("Error - curve_fit failed")
                #print(popt)
            print i


#popt[0], popt[1], popt[2] = map(float, popt.split()) #assign values to popt (a, x0, sigma)
    outfile.write("%s \t %s \t %s \t %s \n" % (i, popt[0], popt[1], abs(popt[2])))  #writing values from outfile to 4colAmpAvgStdev.py
    if popt[1]<0:
        print i, popt
    if popt[0]<0:
        print i, popt
data.close()
outfile.close()

