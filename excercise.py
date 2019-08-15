import numpy as np

def fillMatrix(n):
    matrixA = np.chararray((n, n))
    matrixA[:] = ' ' 
    for i in range(0, n):
        matrixA[0][i] = '*'
        matrixA[n-1][i] = '*'
        matrixA[i][n-1] = '*'
        matrixA[i][0] = '*'       
        matrixA[i][i] = '*'
        matrixA[i][(n-1)-i] = '*'            
    return matrixA


n = int(input("Enter the size of the array: "))
   
matrixA = fillMatrix(n)
print(matrixA)
