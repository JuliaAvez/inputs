
#!/usr/bin/python
import math
import fileinput
import sys

def file_len(fname): # this is the counting function for lines in a file only
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)


data = open('photerr10.zout','r') 

speczfile = open('CANDELS_GOODSS_Specz.dat','r') #we are creating this file so we open it for writing

specz= speczfile.readlines() #starts from 0
speczfile.close()
counter=0

outfile= open('outfilewerr10.zout', 'w')
z_est= open('photestwerr10.zout', 'w') # opening to write z_m2 separately

linenumb= file_len('CANDELS_GOODSS_Specz.dat') # counts number of lines
print linenumb

for line in data.readlines():
    if not line.startswith(('#')):
        counter += 1

        id, dummy, dummy, dummy, dummy, dummy, dummy, z_m2, dummy, l68, u68, l95, u95, dummy, dummy, dummy= map(float, line.split()) #this line reads in all the input, splitting them on a blank space
        
        diff68= (z_m2-float(specz[counter-1]))/((u68-l68)/2)
        # if (math.abs(diff68) < 1)):
        diff95= (z_m2-float(specz[counter-1]))/((u95-l95)/2)
       
            
        
        z_est.write("%s \t %s \n" % (id, z_m2)) #takes just id and z_m2 values
        
        if (counter < linenumb):
            
        
            outfile.write("%s \t %s \t %s \n" % (counter, diff68, diff95))

        else:
            outfile.write("%s \t %s \t %s" % (counter, diff68, diff95)) # this gets rid of last line with nothing in it
            

data.close()                              
z_est.close()
outfile.close()