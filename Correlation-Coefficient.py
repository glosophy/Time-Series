import numpy as np


def corr_coef(x,y):
    '''It returns the correlation coefficient for two given datasets'''
    
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sqrt(np.sum((x - x_mean)*(x - x_mean))) * np.sqrt(np.sum((y - y_mean)*(y - y_mean)))
    
    r = numerator / denominator
    
    return r
