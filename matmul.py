import numpy as np
import csv

'''def csv2mat(filename):
    return np.array(list(csv.reader(open(filename, "r"), delimiter=",")))
A=csv2mat('A.csv')
b=csv2mat('b.csv')
'''

def readm(fname='A.csv'):
    f= open(fname,'r')
    A=[]
    for line in f.readlines():
        A.append([float(x) for x in line.strip().split(',')])
    f.close()
    return A

def matmul(A,b):
    m,n=len(A),len(b[0])
    J = len(A[0])
    if len(A[0])==len(b):
        C=[ [0]*n for i in range(m)]
        for r in range(m):
            for c in range(n):
                C[r][c] = sum([float(A[r][j])*float(b[j][c]) for j in range(J)])
        return C
    return [] #can't matmul