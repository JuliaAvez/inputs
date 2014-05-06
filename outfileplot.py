# Hi Professor Liu! This is the routine that I used to create plots, such as those that are in my research paper. I looked up matplotlib online for most of this.

import numpy as np
import matplotlib.pyplot as plt


ax = plt.subplot(111)


ax.grid(False) # this is for title, and axes labels
ax.set_xlabel('Galaxy ID --->')
ax.set_ylabel('Difference --->')
ax.set_title('Probability of Estimated Redshift lying within 68% of True Spectroscopic Redshift')

#ax.set_yticklabels([])
#ax.set_xticklabels([])


data= open('outfilewerr11.zout', 'r') #changed from outfile.zout


countvalues=[] #vector that contains x values
values68= [] #vector with y1 values
#values95= [] #vector with y2 values

count68diff = 0

for line in data.readlines():
    
    
    counter, diff68, diff95 = map(float, line.split()) #this line reads in all the input, splitting them on a blank space
    #print counter
    

    if (-1 < diff68 < 1):
        count68diff+=1
    

    countvalues.append(counter)
    values68.append(diff68)
#values95.append(diff95)

data.close()

print count68diff #how many values there are in the 68% confidence region
print count68diff/counter #ratio of # values in 68%/total # values


# the scatter plot:
ax.scatter(countvalues, values68, label = "68% of points are inside our 68% confidence region")

ax.set_xlim([0,1360])
ax.set_ylim([-2,2])
leg = ax.legend(numpoints=1)


frame  = leg.get_frame()
frame.set_facecolor('0.80')    # sets the legend frame face color to light gray


#plt.plot(countvalues, values95) #plot (x, y)

l = plt.axhline(y=0) # draws default line at y=0 that spans x range
l = plt.axvline(linewidth=3, color='r') # draws thick red line at x=0 that spans y range
l = plt.axhline(y=1) # draw a default hline at y=1 that spans the xrange
l = plt.axhline(y=-1) # draw a default hline at y=-1 that spans the xrange




plt.show()
