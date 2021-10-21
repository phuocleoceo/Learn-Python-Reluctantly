import numpy as np

# Fs = 44100
# lab = [0.45, 0.48, 0.77, 0.79, 0.88, 0.92, 1.32, 1.37, 1.53, 1.59, 1.93]
# lab_label = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

# U_label = []
# V_label = []
# for i in range(0, len(lab_label)):
#     n = [int(lab[i]*Fs), int(lab[i+1]*Fs)]
#     if lab_label[i] == 0:
#         U_label.append(n)
#     else:
#         V_label.append(n)

# print("U label: ", U_label)
# print("V label : ", V_label)

# U = []
# for u in U_label:
#     n = np.arange(u[0], u[1], int(0.02*Fs))
#     for i in range(0, len(n)-1):
#         U.append([n[i], n[i+1]])
# V = []
# for v in V_label:
#     n = np.arange(v[0], v[1], int(0.02*Fs))
#     for i in range(0, len(n)-1):
#         V.append([n[i], n[i+1]])

# print("U : ", U)
# print("V : ", V)

# print(np.arange(33957, 34839+1, 882))

# zrr = np.array([4, 5])
# print(np.sum(zrr**2))

vrr = np.array([1, 2, 3, 4, 5, 6, 10])
T = 5
print(len([i for i in vrr if i > T]))
print(np.sum(vrr > T))
