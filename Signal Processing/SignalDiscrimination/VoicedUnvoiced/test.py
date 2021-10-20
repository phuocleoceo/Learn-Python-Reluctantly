import numpy as np
import math
# arr = np.array([4, 5, 6, 7, 8, 0, -1, 2])

# u = [[1, 2], [3, 5]]
# for x in u:
#     print(arr[x])

# print(np.floor(arr/2))

# T = 7
# f = np.argwhere(arr > T)
# print(len(f))

# g = len([i for i in arr if i > T])
# print(g)

# BRR = []
# BRR.append([4*2, 5*2])
# BRR.append([7, 8])
# print(BRR)

# b = [[1, 2], [4, 5]]
# print(b[0][1])

brr = [[38367, 41454], [55566, 58653], [70119, 73206], [78498, 80262]]

crr = []
for x in brr:
    n = np.arange(x[0], x[1]+int(0.02*44100), int(0.02*44100))
    for i in range(0, len(n)-1):
        crr.append([n[i], n[i+1]])
print(crr)
