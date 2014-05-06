import math
import fileinput
import sys

#nobjects = 1338
    #for i in range(1, nobjects + 1):
    #filename = str(i) + '.pz'
    #filename stands for all of the files in OUTPUT that end in .pz
#data = open (filename, 'r')

#numbers = filename

#-----------------------------------------------------------------------------------

def avg(numbers):
    total = 0
    for number in numbers:  #is a list
        
            total += float(number)
    return total/len(numbers) #finds avg

#data.close()

pz = [] #vector pz
sqr = []

def stdev(numbers):
    total = 0
    for number in numbers:
        if numbers[-3:]=='.pz':
            
            pz.append(number - avg) #this part finds the deviation of each number from avg
            for number in pz:
                
                sqr.append(float(number*number)) #this part squares each of the deviations
                print(sqr)
            
                mean = sum(sqr)/len(sqr) #this part finds the avg of those squared dev's
                print(mean)
                
                stdev = mean ** 0.5  #this part takes the square root of the squares
                print('The standard deviation is', stdev)

