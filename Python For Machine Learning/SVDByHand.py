import numpy as np
from numpy.linalg import eig, matrix_rank


def generate_D(m, n, r, S):
    D = np.zeros((m, n))
    for i in range(0, r):
        D[i, i] = S[i]
    return D


A = np.array([[1, 2], [3, 4], [2, 5]])
# A = np.array([[1, 2, 3], [4, 5, 6]])
print(">> Matrix A: \n", A)


AdotAT = np.dot(A, np.transpose(A))
ATdotA = np.dot(np.transpose(A), A)

U = eig(AdotAT)[1]  # U là vecto riêng của A.AT
print(">> Matrix U: \n", U)

# S là căn( giá trị riêng của AT.A) rồi sắp xếp giảm dần
S = np.sqrt(eig(ATdotA)[0])
# S = np.sort(S)[..., ::-1]
S = np.sort(S)[::-1]
print(">> Matrix S: \n", S)

D = generate_D(len(A), len(A[0]), matrix_rank(A), S)
print(">> Matrix D : \n", D)

VT = np.transpose(eig(ATdotA)[1])  # V là vecto riêng của AT.A
print(">> Matrix VT : \n", VT)

print(">> U.D.VT : \n", (U.dot(D)).dot(VT))
