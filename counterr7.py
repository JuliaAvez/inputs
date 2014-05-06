#This is a counting file that takes the counter and diff95 from outfile. The print commands tell me how many values are in diff95, if diff95 was our confidence region bet 1 and -1 (similar to what we did with diff68 in outplot.py).

outfile = open('outfilewerr7.zout', 'r') 

count68diff = 0
count95diff = 0

speczfile = open('CANDELS_GOODSS_Specz.dat','r') #will use specz from here

specz = speczfile.readlines() #starts from 0
speczfile.close()

#print len(specz)

counter=0
counternot=0
photest = open ('photestwerr7.zout', 'r')

photz=[] #creates a list that we will use throughout the for loop

for line in photest.readlines():

    dummyid, z_m2 =  map(float, line.split())

    photz.append(z_m2)

photest.close()


#print len(photz)

for line in outfile.readlines():
    
    
    counter, diff68, diff95 = map(float, line.split()) #this line reads in all the input, splitting them on a blank space
    

    if (-1 < diff68 < 1):
        count68diff+=1
    

    if (-1 < diff95 < 1):
        count95diff+=1

    if (float(specz[int(counter -1)]) != 0.0) :

        if (((abs(float(specz[int(counter - 1)])- photz[int(counter - 1)]))/(float(specz[int(counter - 1)]))) < 1):
            counternot += 1

outfile.close()



print 'counter of not outliers:', counternot
print 'ratio of 68diff to total:', float(count68diff)/float(counternot)

#print  count68diff #how many values there are in the 95% confidence region
#print count68diff/counter #ratio of # values in 95% / total # values


#print count95diff #how many values there are in the 95% confidence region
#print count95diff/counter #ratio of # values in 95% / total # values
print 'ratio of 95diff to total:', float(count95diff)/float(counternot)
