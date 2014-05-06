import numpy as np
#Gaussian function
def gauss_function(x, a, x0, sigma): #a is normalization(amp), x0 is avg, sigma is stdev
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

