#This is a counting file that takes the counter and diff95 from outfile. The print commands tell me how many values are in diff95, if diff95 was our confidence region bet 1 and -1 (similar to what we did with diff68 in outplot.py).

data= open('outfile.zout', 'r')

count95diff = 0

for line in data.readlines():
    
    
    counter, diff68, diff95 = map(float, line.split()) #this line reads in all the input, splitting them on a blank space
    #print counter
    
    if (-1 < diff95 < 1):
        count95diff+=1

data.close()

print count95diff #how many values there are in the 95% confidence region
print count95diff/counter #ratio of # values in 95% / total # values
