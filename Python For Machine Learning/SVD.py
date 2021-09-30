import numpy as np


m, n = 5, 4

A = np.random.rand(m, n)

U, S, V = np.linalg.svd(A)

print(">> Matrix A: \n", A)

print(">> Matrix U: \n", U)

print(">> Matrix S: \n", S)

print(">> Matrix V: \n", V)

# print(">> A.AT : \n", np.dot(A, A.T))
