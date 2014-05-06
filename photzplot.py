import numpy as np
import matplotlib.pyplot as plt

#a = np.arange(0,3,.02) # all this stuff is for the legend
#b = np.arange(0,3,.02)
#c = np.exp(a)
#d = c[::-1]

#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(a,c,'k--',a,d,'k:',a,c+d,'k')


data = open('photestwerr11.zout', 'r')

x=[]
y=[]

for line in data.readlines():
    
    counter, diff68 = map(float, line.split()) #this line reads in all the input, splitting them on a blank space
    
    x.append(counter)
    y.append(diff68)
    

data.close()

# the scatter plot:
axScatter = plt.subplot(111)
axScatter.scatter(x, y)
axScatter.set_xlim([0,1370])
axScatter.set_ylim([0,5])

leg = axScatter.legend(('Redshift'),
                'far right', shadow=True)

frame  = leg.get_frame()
frame.set_facecolor('0.80')    # set the legend frame face color to light gray



axScatter.grid(False) # this is for title, and axes labels
axScatter.set_xlabel('Counter --->')
axScatter.set_ylabel('Difference --->')
axScatter.set_title('Estimator of Difference')

axScatter.set_yticklabels([])
axScatter.set_xticklabels([])


l = plt.axhline(linewidth=3, color='r') # draws thick red line at y=0 that spans x range
l = plt.axvline(linewidth=3, color='r') # draws thick red line at x=0 that spans y range

plt.show()