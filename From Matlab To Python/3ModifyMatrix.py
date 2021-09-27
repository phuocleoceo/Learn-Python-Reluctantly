import numpy as np

a = np.ones((3, 3), dtype=int)
b = np.ones((3, 3), dtype=int)*5
# c = [a+2, b]
# print(c)

d = np.concatenate((a+2, b))
print(d)

# Ma trận cấp 3, chọn những cột mình cần
e = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(e)
print(e[:, [0, 2]])

# xoá theo cột mình muốn (ở đây là cột 2) n
# f = e[:, : 2]  # 0->n
# g = e[:, 3:]  # n+1 -> hết
# print(np.concatenate((f, g), axis=1))


def remove_col(arr, col):
    return np.concatenate((arr[:, :col], arr[:, col+1:]), axis=1)


print(remove_col(e, 2))
