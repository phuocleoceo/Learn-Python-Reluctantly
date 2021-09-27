import numpy as np

arr = np.array([[16, 3, 2, 13], [5, 30, 11, 8],
               [9, 6, 7, 12], [2, 15, 14, 1]])

print(arr)
print(arr.sum(axis=1))  # Tổng theo hàng
print(arr.sum(axis=0))  # Tổng theo cột

print(arr[1, 2])

# [a,b]
print(arr[1, 2:4])   # chọn mảng index a, cắt theo b
print(arr[0:2, 2])  # cắt mảng brr theo a, chọn index b
print(arr[0:2, 1:4])  # cắt brr theo a, cắt mỗi phần tử sau đó theo b

# Tạo mảng 1 chiều từ a->b , bước nhảy c
brr = np.array(range(100, 50, -7))  # step2
print(brr)

# Ma trận chuyển vị
print(np.transpose(arr))
print(arr.T)

# Đổi thử tự hàng cột
print(arr[:, [0, 2, 1, 3]])

# Tạo ndarray từ list
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list)
ndarray_from_list = np.asarray(my_list, dtype=int)
print(ndarray_from_list)

# Read file
# https://stackoverflow.com/questions/7618858/how-to-to-read-a-matrix-from-a-given-file
