import numpy as np
from numpy import random
from math import factorial

# Ma trận các số 0
arr = np.zeros((2, 4), dtype=int)
print(arr)

# Ma trận các số 1
brr = np.ones((2, 3), dtype=int)
print(brr)

# Ma trận ngẫu nhiên
crr = random.rand(4, 4)
print(crr)

# Ma trận ngẫu nhiên phân bố trực giao
drr = random.randn(3, 3)
print(drr)

# Ma trận đơn vị
err = np.eye(3, dtype=int)
print(err)


# tạo ra ma trận cấp n gồm các số nguyên từ 1 đến n2 với tổng các
# hàng bằng tổng các cột.n phải lớn hơn hay bằng 3.
def magic(n):
    n = int(n)
    if n < 3:
        raise ValueError("Size must be at least 3")
    if n % 2 == 1:
        p = np.arange(1, n+1)
        return n*np.mod(p[:, None] + p - (n+3)//2, n) + np.mod(p[:, None] + 2*p-2, n) + 1
    elif n % 4 == 0:
        J = np.mod(np.arange(1, n+1), 4) // 2
        K = J[:, None] == J
        M = np.arange(1, n*n+1, n)[:, None] + np.arange(n)
        M[K] = n*n + 1 - M[K]
    else:
        p = n//2
        M = magic(p)
        M = np.block([[M, M+2*p*p], [M+3*p*p, M+p*p]])
        i = np.arange(p)
        k = (n-2)//4
        j = np.concatenate((np.arange(k), np.arange(n-k+1, n)))
        M[np.ix_(np.concatenate((i, i+p)), j)
          ] = M[np.ix_(np.concatenate((i+p, i)), j)]
        M[np.ix_([k, k+p], [0, k])] = M[np.ix_([k+p, k], [0, k])]
    return M


frr = magic(3)
print(frr)

# tạo ra ma trận xác định dương mà các phần tử lấy từ tam giác Pascal


def binomial(x, y):
    try:
        return factorial(x) / (factorial(y) * factorial(x - y))
    except ValueError:
        return 0


def pascals_triangle(number_of_rows):
    triangle = []
    if number_of_rows <= 0:
        return None
    else:
        for row in range(number_of_rows+1):
            triangle.append([binomial(row, column) for column in range(row+1)])
    return triangle


grr = pascals_triangle(4)
print(grr)
