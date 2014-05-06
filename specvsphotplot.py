import numpy as np
import matplotlib.pyplot as plt




data= open('photestwerr11.zout', 'r') #changed from photest.zout


xvalues=[] #vector that contains zspec
yvalues= [] #vector with photz values


speczfile = open('CANDELS_GOODSS_Specz.dat','r')

specz= speczfile.readlines() #starts from 0
speczfile.close()
counter=0

for i in range(1, len(specz)+1):
    
    xvalues.append(float(specz[i-1]))

for line in data.readlines():

    
    id, zphot = map(float, line.split()) #this line reads in all the input, splitting them on a blank space
        
    yvalues.append(zphot)
    



data.close()



# the scatter plot:
ax = plt.subplot(111)
ax.scatter(xvalues, yvalues)




    #leg = ax.legend(('specz (true)', 'photz (est)'),
#'upper center', shadow=True)

ax.grid(False) # this is for title, and axes labels
ax.set_xlabel('specz (true) --->')
ax.set_ylabel('photest.zout (estimate) --->')
ax.set_title('Estimated vs True Redshifts')

ax.set_yticklabels([0,1,2,3,4,5,6,7])
ax.set_xticklabels([0,1,2,3,4,5,6,7])

ax.set_xlim([0,7])
ax.set_ylim([0,7])
#frame  = leg.get_frame()
#frame.set_facecolor('0.80')    # sets the legend frame face color to light gray



l = plt.axhline(linewidth=3, color='r') # draws thick red line at y=0 that spans x range
l = plt.axvline(linewidth=3, color='r') # draws thick red line at x=0 that spans y range


plt.show()

