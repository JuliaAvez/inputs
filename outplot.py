# Hi Professor Liu! This is one of my first plotting routines.

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib
#from pylab import *
#import matplotlib.mlab as mlab
#import matplotlib.cbook as cbook

a = np.arange(0,3,.02) # all this stuff is for the legend 
b = np.arange(0,3,.02)
c = np.exp(a)
d = c[::-1]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(a,c,'k--',a,d,'k:',a,c+d,'k')
#leg = ax.legend(('Model length', 'Data length', 'Total message length'),
#'upper center', shadow=True)

ax.grid(False) # this is for title, and axes labels
ax.set_xlabel('Counter --->')
ax.set_ylabel('Difference --->')
ax.set_title('Estimator of Difference')

ax.set_yticklabels([])
ax.set_xticklabels([])

#frame  = leg.get_frame()
#frame.set_facecolor('0.80')    # set the legend frame face color to light gray


data = open('2coloutfile.zout', 'r')


xvalues=[] #vector that contains x values
yvalues= [] #vector with y values

count68diff=0 #this is for the if statement below

for line in data.readlines():
    
    
    counter, diff68 = map(float, line.split()) #this line reads in all the input, splitting them on a blank space


    if (-1 < diff68 < 1):
       count68diff+=1
    
    xvalues.append(counter)
    yvalues.append(diff68)
   

data.close()

print count68diff #how many values there are in the 68% confidence region
print count68diff/counter #ratio of # values in 68%/total # values

# the scatter plot:
axScatter = plt.subplot(111)
axScatter.scatter(xvalues, yvalues)
axScatter.set_aspect(200)

axScatter.set_xlim([0,1340])
axScatter.set_ylim([-3,3])



l = plt.axhline(linewidth=3, color='r') # draws thick red line at y=0 that spans x range

l = plt.axhline(y=1) # draw a default hline at y=1 that spans the xrange
l = plt.axhline(y=-1) # draw a default hline at y=-1 that spans the xrange

plt.show()

