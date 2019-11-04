import numpy as np
import matplotlib.pyplot as plt


def plot_ACF(x):
    '''It returns the ACF plot for a given list of residuals'''

    list20 = x[0:]

    # Reverse the list to make it mirror the y axis
    list_r = list20[::-1]
    list_r = list_r[0:(len(list20)-1)]

    # Join both lists
    join_list = list_r + list20

    # Create list with lag
    lag = [i for i in range(-(len(list_r)), len(list20))]

    plt.stem(lag, join_list)
    plt.title('Autocorrelation Plot')
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation')

    return plt.show()
