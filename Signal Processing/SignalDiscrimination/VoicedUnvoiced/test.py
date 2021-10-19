# from prettytable import PrettyTable

# myTable = PrettyTable(["STT", "Name"])

# myTable.add_row(["1", "Phuoc"])

# myTable.add_row(["2", "Ngan"])

# myTable.add_row(["3", "Hoang"])

# myTable.add_row(["4", "Duy"])

# print(myTable)
import numpy as np

arr = np.array([4, 5, 6, 7, 8])
print(sum(arr))
print(np.sum(arr))

T = 7
f = np.argwhere(arr > T)
print(len(f))

g = len([i for i in arr if i > T])
print(g)

# print(np.sum(arr % 2 == 0))

# T = 1
# print(np.sum(f(f > T)-T))
