import numpy as np


def generate_D(m, n, r, S):
    D = np.zeros((m, n))
    for i in range(0, r):
        D[i, i] = S[i]
    return D


# A = np.array([[1, 2],
#               [3, 4],
#               [2, 5]])
A = np.array([[1, 3, 5],
              [7, 8, 9]])
print(">> Rank A : ", np.linalg.matrix_rank(A))

U, S, V = np.linalg.svd(A)
D = generate_D(len(A), len(A[0]), np.linalg.matrix_rank(A), S)

print(">> Matrix A: \n", A)

print(">> Matrix U: \n", U)

print(">> Matrix S: \n", S)

print(">> Matrix D: \n", D)

print(">> Matrix V: \n", V)  # this V is VT

print("U.D.VT : \n", (U.dot(D)).dot(V))
