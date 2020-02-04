def difference(dataset, column=1, interval=1):
    '''Creates a differenced series for stationarity'''
    
    diff = list()
    for i in range(interval, len(dataset)):
        value = dataset.iloc[i, column] - dataset.iloc[i - interval, column]
        diff.append(value)
    return Series(diff)
    
