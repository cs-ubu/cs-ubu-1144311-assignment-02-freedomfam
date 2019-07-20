import numpy as np
import csv

def readm(fname='A.csv'):
    f= open(fname,'r')
    A=[]
    for line in f.readlines():
        A.append([float(x) for x in line.strip().split(',')])
    f.close()
    return A


'''A = [[3, 2, -4], [2, 3, 3], [5, -3, 1]]
b = [3, 15, 14]'''
def guass(a,b):
    a = np.array(a)
    b=np.array(b)
    n=len(a)
    for k in range(0, n-1):
      for i in range(k+1, n):
        if a[i,k] != 0.0:
            lam = a[i,k]/a[k,k]
            a[i,k+1:n] = a[i, k+1:n] - lam*a[k,k+1:n]
            b[i] = b[i] - lam*b[k]
    x=[0]*n
    for k in range(n-1, -1, -1):
      x[k] = (b[k] - np.dot(a[k,k+1:n], x[k+1:n]))/a[k,k]
    return x

a=readm('A.csv')
b=readm('b.csv')
print(guass(a,b))
