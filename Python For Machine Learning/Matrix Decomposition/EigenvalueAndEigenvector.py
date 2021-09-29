import numpy as np

A = np.array([[2, 1], [4, 5]])
eigenvalue, eigenvector = np.linalg.eig(A)

print("<< Decomposition A : >>")
print(">> V : ")
print(eigenvector)
print(">> Diag(lamda) : ")
print(np.diag(eigenvalue))
print(">> V^-1 : ")
print(np.linalg.inv(eigenvector))
