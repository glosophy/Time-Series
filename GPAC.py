# Helper function to calculate numerator and denominator 
def phi_kk(j,k,ry):
    num = []
    num1 =[]
    num2 = []
    den = []
    M = math.ceil(len(ry)/2)
    if k==1:
        phi_kk = ry[M+j]/ry[M+j-1]
    else:
        for m in range(k):

          den.append(ry[M + j + m-1: M + j + m - k-1: -1])
          num2.append(ry[M + j  + m])

        den = np.array(den)
        x = np.array(num2)
        num3 = np.transpose([x])
        num1 = den[...,0:k-1]
        num = np.concatenate((num1,num3),axis=1)

        if np.linalg.det(den)!=0:
            phi_kk = np.linalg.det(num)/np.linalg.det(den)
        else:
            phi_kk = 'inf'
    return phi_kk


# Helper function to print the GPAC table as a matrix
def printMatrix(s):
    j,k = s.shape
    GPAC = pd.DataFrame(s)
    GPAC.columns = range(1, k+1)
    print(GPAC)


def Cal_GPAC(ryy, j, k):
    '''It takes the autocorrelation of an ARMA process and the max order of AR and MA'''
    phi = np.zeros((j,k-1))
    for kk in range(1,k):
        for jj in range(j):
            phi_kk1= phi_kk(jj,kk,ryy)
            phi[jj][kk-1]=phi_kk1

    printMatrix(phi)
