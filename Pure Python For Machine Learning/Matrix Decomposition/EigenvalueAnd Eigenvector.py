# Thuật toán Danhilepski được em tham khảo từ giáo trình PHƯƠNG PHÁP TÍNH trang 37/80
# được biên soạn bới cô ĐỖ THỊ TUYẾT HOA (2007 - Lưu hành nội bộ)
from math import pow
from numpy import roots


# Hàm in ma trận đẹp hơn
def Print_Matrix(title, M):
    print(title)
    for row in M:
        print(row)


# Kiểm tra ma trận đối xứng
def Is_Symmetric_Matrix(A):
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            if A[i][j] != A[j][i]:
                return False
    return True


# Ma trận full số 0
def Zeros_Matrix(row, col):
    M = [0]*row
    for i in range(0, row):
        M[i] = [0]*col
    return M


# Ma trận đơn vị
def Identity_Matrix(n):
    M = Zeros_Matrix(n, n)
    for i in range(0, n):
        M[i][i] = 1
    return M


# Copy ma trận
def Copy_Matrix(M):
    rows = len(M)
    cols = len(M[0])
    N = Zeros_Matrix(rows, cols)
    for i in range(0, rows):
        for j in range(0, cols):
            N[i][j] = M[i][j]
    return N


# Định thức
def Determinant_Matrix(M):
    n = len(M)
    A = Copy_Matrix(M)
    count = 0
    B = [0]*n

    for i in range(0, n-1):
        if A[i][i] == 0:
            check = 0

            for j in range(i+1, n):
                if A[i][j] != 0:
                    for k in range(0, n):
                        A[k][i], A[k][j] = A[k][j], A[k][i]
                    count += 1
                    check += 1
                    break
            if check == 0:
                return 0

        B[i] = A[i][i]
        for j in range(0, n):
            A[i][j] /= B[i]

        for j in range(i+1, n):
            scale = A[j][i]
            for k in range(0, n):
                A[j][k] -= scale*A[i][k]

    B[n-1] = A[n-1][n-1]
    det = 1.0
    for i in range(0, n):
        det *= B[i]

    if count % 2 == 0:
        return det
    else:
        return -det


# Ma trận bù, bỏ hàng i cột j
def Minor_Matrix(A, i, j):
    return [row[:j] + row[j+1:] for row in (A[:i]+A[i+1:])]


# Ma trận chuyển vị
def Transpose_Matrix(A):
    AT = Zeros_Matrix(len(A), len(A[0]))
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            AT[i][j] = A[j][i]
    return AT


# Ma trận nghịch đảo
def Inverse_Matrix(A):
    det = Determinant_Matrix(A)
    n = len(A)

    if det == 0:
        return None

    if n == 1 and len(A[0]) == 1:
        return 1/A[0][0]

    A_Inv = Zeros_Matrix(n, n)
    for i in range(0, n):
        for j in range(0, n):
            P = Minor_Matrix(A, i, j)
            A_Inv[i][j] = 1/det*pow(-1, i+j)*Determinant_Matrix(P)
    return Transpose_Matrix(A_Inv)


# Nhân 2 ma trận
def Multiply_Matrix(A, B):
    rowA = len(A)
    colA = len(A[0])
    rowB = len(B)
    colB = len(B[0])
    if colA != rowB:
        raise ArithmeticError("ColA != RowB")

    C = Zeros_Matrix(rowA, colB)
    for i in range(0, rowA):
        for j in range(0, colB):
            C[i][j] = 0
            for k in range(0, colA):
                C[i][j] += A[i][k]*B[k][j]
    return C


# Ma trận Phorebemit theo phương pháp Danhilepski
def Phorebemit_Matrix(a):
    n = len(a)
    A = Copy_Matrix(a)
    M, M1, B = Zeros_Matrix(n, n), Zeros_Matrix(n, n), Zeros_Matrix(n, n)
    M_Eigenvector = Identity_Matrix(n)

    for k in range(n-1, 0, -1):
        for i in range(0, n):
            for j in range(0, n):
                if i != k-1:
                    if i == j:
                        M[i][j] = 1
                        M1[i][j] = 1
                    else:
                        M[i][j] = 0
                        M1[i][j] = 0
                else:
                    M1[i][j] = A[k][j]
                    if j == k-1:
                        M[i][j] = 1/A[k][k-1]
                    else:
                        M[i][j] = -A[k][j]/A[k][k-1]
        B = Multiply_Matrix(A, M)
        A = Multiply_Matrix(M1, B)
        M_Eigenvector = Multiply_Matrix(M_Eigenvector, M)

    return A, M_Eigenvector


# Vector chứa Giá trị riêng Ma trận
def Eigenvalue_Matrix(A):
    Phorebemit_Mat = Phorebemit_Matrix(A)[0]
    return [1.0]+[-x for x in Phorebemit_Mat[0]]


# Ma trận chéo của giá trị riêng
def Diag_Matrix(v):
    n = len(v)
    Diag_Mat = Zeros_Matrix(n, n)
    for i in range(0, n):
        Diag_Mat[i][i] = v[i]
    return Diag_Mat


# Nhân ma trận với vector
def Multiply_Matrix_Vector(M, V):
    n = len(V)
    r = [0]*n
    for i in range(0, n):
        for j in range(0, n):
            r[i] += M[i][j]*V[j]
    return r


# Ma trận vecto riêng
def Eigenvector(M, Eigenvalue_Mat):
    n = len(Eigenvalue_Mat)
    A, RESULT_VECTOR = Zeros_Matrix(n, n), Zeros_Matrix(n, n)

    for i in range(0, n):
        for j in range(0, n):
            A[i][j] = pow(Eigenvalue_Mat[i], n-j-1)
        RESULT_VECTOR[i] = Multiply_Matrix_Vector(M, A[i])

    return Transpose_Matrix(RESULT_VECTOR)


# BÀI 2 TRƯỜNG HỢP A ĐỐI XỨNG VÀ Q TRỰC GIAO - CHƯA CHẠY ĐƯỢC VÌ PHẦN Q KHÁ PHỨC TẠP
# Nhân vecto với 1 số
# def Vector_Multi_Number(A, k):
#     return [x*k for x in A]


# # Trừ 2 vector
# def Vector_Minus_Vector(A, B):
#     C = [0]*len(A)
#     for i in range(0, len(A)):
#         C[i] = A[i]-B[i]
#     return C


# # Tich vô hướng 2 vector
# def Vector_Multi_Scalar(A, B):
#     sum = 0
#     for i in range(0, len(A)):
#         sum += A[i]*B[i]
#     return sum


# # Trực giao ma trận vecto riêng
# def Orthogonal_Matrix(M, Eigenvalue_Mat):
#     A = Transpose_Matrix(Eigenvector(M, Eigenvalue_Mat))
#     n = len(A)
#     OM = Zeros_Matrix(n, n)
#     OM[0] = A[0]
#     for i in range(1, n):
#         scalar_uv = Vector_Multi_Scalar(
#             OM[i-1], A[i]) / Vector_Multi_Scalar(OM[i-1], OM[i-1])
#         proj_uv = Vector_Multi_Number(OM[i-1], scalar_uv)
#         OM[i] = Vector_Minus_Vector(A[i], proj_uv)

#     Print_Matrix("", Transpose_Matrix(OM))


#----------------------------------MAIN CODE-----------------------------------------------------#

# A = [[2, 1, 0],
#      [1, 3, 1],
#      [0, 1, 2]]
A = [[2, 1],
     [4, 5]]

Eigenvalue = roots(Eigenvalue_Matrix(A))

Eigenvector_Matrix = Eigenvector(Phorebemit_Matrix(A)[1], Eigenvalue)

print("A phân rã thành : ")

Print_Matrix("Ma trận vector riêng (V) : ", Eigenvector_Matrix)
Print_Matrix("Ma trận giá trị riêng (diag(lamda)) : ", Diag_Matrix(Eigenvalue))
Print_Matrix("Ma trận vector riêng nghịch đảo (V^(-1)) : ",
             Inverse_Matrix(Eigenvector_Matrix))
