import numpy as np
from numpy.linalg import eig, matrix_rank


def generate_D(A, S):
    r = matrix_rank(A)
    m, n = np.shape(A)
    D = np.zeros((m, n))
    for i in range(0, r):
        D[i, i] = S[i]
    return D


# A = np.array([[1, 2],
#               [3, 4],
#               [2, 5]])
A = np.array([[1, 2, 3],
              [4, 5, 6]])
print(">> Matrix A: \n", A)

AdotAT = A.dot(A.T)
ATdotA = (A.T).dot(A)

_, U = eig(AdotAT)
print(">> Matrix U: \n", U)

SS, V = eig(ATdotA)

S = np.sqrt(SS)
S = np.sort(S)[::-1]
# S = np.sort(S)[..., ::-1]
# print(">> Matrix S: \n", S)

D = generate_D(A, S)
print(">> Matrix D : \n", D)

VT = V.T
print(">> Matrix VT : \n", VT)

print(">> U.D.VT : \n", (U.dot(D)).dot(VT))
