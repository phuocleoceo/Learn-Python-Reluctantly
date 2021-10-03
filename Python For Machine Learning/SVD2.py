import math
import numpy as np


def NhapMaTran(Matrix, m, n):
    for i in range(m):
        Matrix.append([])
        row = list(map(int, input(f"Nhập {n} phần tử của hàng {i}: ").split()))
        while len(row) != n:
            row = list(
                map(int, input(f"Nhập {n} phần tử của hàng {i}: ").split()))
        Matrix[i] = row
    return Matrix


def XuatMaTran(Matrix):
    for i in Matrix:
        print(i)

# Ma trận chuyển vị


def ChuyenVi(Matrix, m, n):
    Answer = np.zeros((n, m), float)
    for i in range(m):
        for j in range(n):
            Answer[j][i] = Matrix[i][j]
    return Answer

# Nhân 2 ma trận


def dot(A, B, m, n, q):
    Answer = np.zeros((m, q), float)

    for i in range(m):
        for j in range(q):
            for k in range(n):
                Answer[i][j] += A[i][k] * B[k][j]
    return Answer


def arrange(l, A):
    A = A.transpose()
    d = list(zip(l, A))
    l.sort(reverse=True)
    d.sort(key=lambda x: x[0], reverse=True)
    return np.array([i[1] for i in d]).transpose()


def SVD(Matrix, m, n):
    U = np.zeros((m, m), float)
    V = np.zeros((n, n), float)
    w, V = np.linalg.eig(dot(ChuyenVi(Matrix, m, n), Matrix, n, m, n))
    w = list(w)
    V = arrange(w, V)
    D = np.zeros((m, n), float)
    # Vì vector lưu theo hàng dọc nên phải chuyển vị
    temp = V.transpose()
    # Xét trường hợp cột lớn hơn hàng
    if n > m:
        # Ma trận chéo hóa có đường chéo giới hạn bởi số hàng
        for i in range(m):
            D[i][i] = math.sqrt(w[i])
        # Tính U theo công thức U[i] =  A * V[i] / lamda[i]
        for i in range(m):
            U[i] = (np.array(Matrix) @ np.array(temp[i])) / D[i][i]
    else:
        # Ma trận chéo hóa có đường chéo giới hạn bởi số cột
        for i in range(n):
            D[i][i] = math.sqrt(w[i])
        # Tính U theo công thức U[i] =  A * V[i] / lamda[i]
        for i in range(n):
            U[i] = (np.array(Matrix) @ np.array(temp[i])) / D[i][i]
    U = ChuyenVi(U, m, m)
    V = temp
    return U, D, V


# Main
Matrix = []
U = []
D = []
VT = []
try:
    m = int(input("Nhập số hàng của ma trận: "))
    n = int(input("Nhập số cột của ma trận: "))
    if m < 1 and n < 1:
        print("số hàng và số cột của ma trận là số nguyên dương")
    else:
        NhapMaTran(Matrix, m, n)
        XuatMaTran(Matrix)
        U, D, VT = SVD(Matrix, m, n)
        # U (m x m)
        print("\nU =")
        XuatMaTran(U)
        # D (m x n)
        print("\nD = ")
        XuatMaTran(D)
        # VT (n x n)
        print("\nVT =")
        XuatMaTran(VT)
        # Kiểm tra bằng cách nhân vào
        print("\nCheck = ")
        temp = dot(U, D, m, m, n)
        XuatMaTran(dot(temp, VT, m, n, n))

        # U, S, V = np.linalg.svd(Matrix)

        # print('----- Matrix A: -----\n' + str(Matrix) + '\n')

        # print('----- Matrix U: -----\n' + str(U) + '\n')

        # print('----- Matrix S: -----\n' + str(S) + '\n')

        # print('----- Matrix V: -----\n' + str(V) + '\n')
except ValueError:
    print("số hàng và số cột của ma trận là số nguyên dương")
