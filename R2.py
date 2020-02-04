def R2(y_hat, y_true):
    '''Calculates R^2'''

    mean = np.mean(y_true)
    numerator = []
    denominator = []

    for i in y_hat:
        num = (i - mean) ** 2
        numerator.append(num)

    for j in y_true:
        den = (j - mean) ** 2
        denominator.append(den)

    R2 = np.sum(numerator) / np.sum(denominator)
    return R2
