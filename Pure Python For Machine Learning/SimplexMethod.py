import numpy as np
import math
from prettytable import PrettyTable
# Thư viện vẽ bảng

# m = len(a) = số hàng của a = len(b) = số ràng buộc
# n = len(a[0]) = số cột của a = len(c) = len(delta) = số ẩn (biến)


def DrawSimplexTable(a, b, BasicVar, Coeff, Fmin, delta):
    m, n = np.shape(a)
    simplexTable = PrettyTable(
        ["HeSo", "AnCB", "PhuongAn"]+["x"+str(i+1)+" : "+str(c[i]) for i in range(n)])
    for i in range(m):
        simplexTable.add_row([Coeff[i], "x"+str(BasicVar[i]+1), b[i]]+a[i])
    simplexTable.add_row(["", "", Fmin]+delta.tolist())
    print(simplexTable)


# Nếu tồn tại k:  ∆k >0 và với mọi i = 1..m:  aik≤0 thì bài toán vô nghiệm.
# Nếu ∆k >0, và  tồn tại i: aik>0 thì chuyển sang bước 3
def IsImpossible(a, delta):
    m, n = np.shape(a)
    for k in range(n):
        if delta[k] > 0:
            for i in range(m):
                if a[i][k] > 0:
                    return False
    return True


# Nếu mọi j=1..n: ∆j ≤ 0 thì xo là phương án tối ưu
def IsOptimal(delta):
    for j in range(len(delta)):
        if delta[j] > 0:
            return False
    return True


def UpdateSimplexTable(a, b, r, s):
    m, n = np.shape(a)
    a_new = np.zeros((m, n), dtype=float)
    b_new = np.zeros((m), dtype=float)

    for i in range(m):
        if i == r:
            b_new[r] = b[r] / a[r][s]
            for j in range(n):
                a_new[r][j] = a[r][j]/a[r][s]
        else:
            b_new[i] = b[i] - b[r] / a[r][s] * a[i][s]
            for j in range(n):
                a_new[i][j] = a[i][j] - a[r][j] / a[r][s] * a[i][s]

    return a_new, b_new


def SimplexMethod(c, b, a):
    m, n = np.shape(a)
    delta = np.zeros((n))

    # BasicVar lưu chỉ số biến được xét, Coeff lưu hệ số
    BasicVar = []
    Coeff = []
    # Check 1 phần tử ma trận ==1 , tính tổng của cột chứa nó
    # Nếu Tổng cột đó bằng nó (1) => các phần tử khác cùng hàng đều = 0  => ẨnCB
    for i in range(m):
        for j in range(n):
            if a[i][j] == 1:
                aj = [x[j] for x in a]
                if np.sum(aj) == a[i][j]:
                    BasicVar.append(j)
                    Coeff.append(c[j])

    # Fmin= sum( bi * ci )
    # ∆(j) = sum( ci * aij ) - cj
    Fmin = np.sum([Coeff[i]*b[i] for i in range(m)])
    for j in range(n):
        delta[j] = np.sum([Coeff[i]*a[i][j] for i in range(m)]) - c[j]
    DrawSimplexTable(a, b, BasicVar, Coeff, Fmin, delta)

    while not IsOptimal(delta):
        if IsImpossible(a, delta):
            print("Bai Toan Vo Nghiem !")
            return

        # Nếu ∆s = max {∆j} với ∆j > 0 (j=1..n)
        # thì đưa xs đưa vào tập ẩn cơ bản
        s = np.argmax(delta > 0)

        # Nếu br/ars =  min {bi/ais} với ais > 0
        # thì loại xr ra khỏi tập ẩn cơ bản
        b_as = [b[i]/a[i][s] if a[i][s] > 0 else math.inf for i in range(m)]
        r = np.argmin(b_as)

        # thay r thành s
        BasicVar[r] = s
        Coeff[r] = c[s]

        a, b = UpdateSimplexTable(a, b, r, s)

        Fmin = np.sum([Coeff[i]*b[i] for i in range(m)])
        for j in range(n):
            delta[j] = np.sum([Coeff[i]*a[i][j] for i in range(m)]) - c[j]
        DrawSimplexTable(a.tolist(), b, BasicVar, Coeff, Fmin, delta)

    # print(BasicVar)
    # print(Coeff)
    # print(b)
    x = [0]*n
    for i in range(m):
        x[BasicVar[i]] = b[i]

    print("Fmin: ", Fmin)
    print("x: ", x)


# f(x) = 5x1 + 4x2 + 5x3 + 2x4 + x5 + 3x6 -> min
# 2x1 + 4x2 + 3x3 + x4 = 52
# 4x1 + 2x2 + 3x3 + x5 = 60
# 3x1 + x3 + x6 = 36
# xj >= 0 (j=1..6)
c = [5, 4, 5, 2, 1, 3]
b = [52, 60, 36]
a = [[2, 4, 3, 1, 0, 0],
     [4, 2, 3, 0, 1, 0],
     [3, 0, 1, 0, 0, 1]]

# c = [3, -1, 2, -2]
# b = [1, 1]
# a = [[1, 1, 0, -2],
#      [0, -2, 1, 3]]

# c = [1, -1, 0, -2, 2, -2]
# b = [2, 12, 9]
# a = [[1, 0, 0, 1, 1, -1],
#      [0, 1, 0, 1, 0, 1],
#      [0, 0, 1, 2, 4, 3]]

# c = [-5, -8, 0, 0]
# b = [1, 2]
# a = [[1, 2, 1, 0],
#      [1, 1, 0, 1]]

# c = [0, 1, -3, 0, 2, 0]
# b = [7, 12, 10]
# a = [[1, 1, -1, 0, 1, 0],
#      [0, -4, 4, 1, 0, 0],
#      [0, -5, 3, 0, 1, 1]]

SimplexMethod(c, b, a)
