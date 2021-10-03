import numpy as np
import sys


def is_symmetric_matrix(A):
    n = len(A)
    for i in range(0, n):
        for j in range(0, n):
            if A[i, j] != A[j, i]:
                return False
    return True


def is_positive_definite_matrix(V):
    for x in V:
        if x <= 0:
            return False
    return True


def cholesky_decomposition(A):
    L = np.zeros_like(A)
    n = len(A)
    for j in range(0, n):
        for i in range(j, n):
            if i == j:
                sumk = 0
                for k in range(0, j):
                    sumk += L[i, j]**2
                L[i, j] = np.sqrt(A[i, j]-sumk)
            else:
                sumk = 0
                for k in range(0, j):
                    sumk += L[i, k]*L[j, k]
                L[i, j] = (A[i, j]-sumk)/L[j, j]
    return L


A = np.array([[7.5, 1, 0.5],
              [1, 10, 2.5],
              [0.5, 2.5, 8]])
print(">> A : \n", A)

m, n = np.shape(A)
if m != n:
    sys.exit(">> Ma tran A khong vuong !")


if not is_symmetric_matrix(A):
    sys.exit(">> Ma tran A khong doi xung !")

V = np.linalg.eigvals(A)
print(">> V : \n", V)
if not is_positive_definite_matrix(V):
    sys.exit(">> Ma tran A khong xac dinh duong !")


L = cholesky_decomposition(A)
print(">> L : \n", L)

print(">> Check L.LT : \n", L.dot(L.T))
