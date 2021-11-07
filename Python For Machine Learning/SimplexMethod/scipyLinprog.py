from scipy.optimize import linprog

# f(x) = 5x1 + 4x2 + 5x3 + 2x4 + x5 + 3x6 -> min
# 2x1 + 4x2 + 3x3 + x4 = 52
# 4x1 + 2x2 + 3x3 + x5 = 60
# 3x1 + x3 + x6 = 36
# xj >= 0 (j=1..6)
c = [5, 4, 5, 2, 1, 3]
a = [[2, 4, 3, 1, 0, 0], [4, 2, 3, 0, 1, 0], [3, 0, 1, 0, 0, 1]]
b = [52, 60, 36]

rs = linprog(c, A_ub=a, b_ub=b)
print(rs)

# => Cannot get INTERGER SOLUTION
