import numpy as np
import math

arr = np.array([[1, 2], [6, 7]])
brr = np.array([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])

# print(arr+brr)
# print(arr-brr)
# print(arr*brr)
# print(arr/brr)

# Số cột Ma trận 1 phải bằng số hàng Ma trận 2
# print(arr@brr)
# print(arr.dot(brr))
# print(brr@arr)


# crr = np.array([[1, 2], [3, 4]])
# # Luỹ thừa từng phần tử ma trận
# print(crr**2)
# # Luỹ thừa ma trận
# print(np.linalg.matrix_power(crr, 4))

# Định thức
A = np.array([[2, 1], [5, 3]])
print(np.linalg.det(A))  # floating point bug

# Ma trận nghịch đảo
B = np.array([[1, 2, 3], [2, 5, 3], [1, 0, 8]])
C = np.linalg.inv(B)
print(C)

for x in C:
    for y in x:
        y = int(math.floor(y))
print(C)
