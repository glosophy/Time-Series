import statsmodels
from statsmodels.tsa.stattools import adfuller


def ADF_Cal(x):
    '''It takes a series and returns the Augmented Dickey Fuller test values'''
    
    result = adfuller(x)
    
    print("ADF Statistic: %f" %result[0])
    print("p-value %f" %result[1])
    print("Critical values:")
    
    for key, value in result[4].items():
        print("\t%s: %.3f" % (key, value))
