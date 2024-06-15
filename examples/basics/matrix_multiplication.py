import numpy as np

#define the  matrices

A = np.array([[1,-3], [2,-1]])

B = np.array([[2,3,-2], [-1,-4,6]])

#perform matrix multiplication

C = np.dot(A,B)

print("Matrix A * Matrix B:\n", C)
