from mat import *

A = readm('A.csv')
b = readm('b.csv')

def solve(A, b):
    """ solve(A,b)
    using Gauss method

    1. elimination
    2. back substitution
    """
    
    # YOUR CODE HERE
    import numpy as np
    A,b = np.array(A),np.array(b)
    #1 . elimination
    n = len(A[0])
    x = [0]*n
    print(f'n={n}')
    for k in range(n-1): #pivot eq 
        print(f'k={k}')
        for j in range(k+1,n):
            print(f'\tกำจัดตัวแปรที่ {k},ออกจากสมาการที่2 {j}')
            lam = A[j][k]/A[k][k]
            #A update A[j][k...]
            A[j,k:n] = A[j,k:n] - lam*A[k,k:n]
            #print(f'\t\tlambda={lam}')
            #B update
            b[j] = b[j] - lam*b[k]
        print(A)
        print(b)
    #2 . back substitution
  #  x[n-1] = b[n-1] / A[n-1][n-1]
    for k in range(n-1,-1,-1):
        print(f'back sub k={k}')
        x[k] = (b[k]- np.dot(A[k,k+1:n], x[k+1:n]))//A[k,k]
    
    return x.flatten()

print(solve(A,b))
