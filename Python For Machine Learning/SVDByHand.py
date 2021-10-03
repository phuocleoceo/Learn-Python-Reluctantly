import numpy as np
from numpy.linalg import eig, matrix_rank


def Generate_S_V(S, V):
    idx = S.argsort()[::-1]
    S = S[idx]
    V = V[:, idx]


def Generate_D(A, S):
    m, n = np.shape(A)
    r = matrix_rank(A)
    D = np.zeros((m, n))
    for i in range(0, r):
        D[i, i] = S[i]
    return D


def Generate_U(A, VT, D):
    m, n = np.shape(A)
    U = np.zeros((m, m))
    for i in range(0, min(m, n)):
        U[i] = A.dot(VT[i]) / D[i][i]
    return U.T


def SVD(A):
    ATdotA = (A.T).dot(A)
    S, V = eig(ATdotA)
    S = np.sqrt(S[S >= 0])
    Generate_S_V(S, V)

    D = Generate_D(A, S)
    VT = V.T
    U = Generate_U(A, VT, D)

    return U, D, VT


A = np.array([[1, 3, 5],
              [7, 8, 9]])
# A = np.array([[1, 3],
#               [7, 8],
#               [2, 3],
#               [10, 11]])
print(">> Matrix A: \n", A)

U, D, VT = SVD(A)

print(">> Matrix U: \n", U)

print(">> Matrix D : \n", D)

print(">> Matrix VT : \n", VT)

print(">> U.D.VT : \n", (U.dot(D)).dot(VT))
