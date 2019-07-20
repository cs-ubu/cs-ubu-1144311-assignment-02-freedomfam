from matmul import readm,matmul

A = readm('A.csv')

b = readm('b.csv')

C = matmul(A,b)

print(C)