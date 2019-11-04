import numpy as np


def autocorr(x):
    '''It returns the autocorrelation function for a given series.'''
    
    k = range(0,len(x))
    mean = np.mean(x)
    autocorr = []
    
    for i in k:
        num = 0
        den = 0
        
        for j in range(i, len(x)):
            num += (x[j] - mean) * (x[j-i] - mean)
        
        den = np.sum((x - mean) ** 2)
        
        autocorr.append(num / den)
    
    return autocorr
