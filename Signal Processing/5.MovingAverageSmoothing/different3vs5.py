# chuong trinh lam tron 1 tin hieu de khu nhieu(denoise)
# so sanh hieu ung lam tron cua 2 bo loc trung binh truot N diem voi N = 3 va N = 5
# Bai toan: ta co tin hieu bi lan voi nhieu x[n], di khoi phuc lai
# tin hieu goc s[n](an trong x[n])
# Ky vong KQ: y[n] cang giong s[n] cang tot
from scipy.signal import convolve, lfilter
import matplotlib.pyplot as plt
from numpy.random import randn
import numpy as np

# sinh tin hieu bi lan voi nhieu cong(additive noise)

# sinh tin hieu bi lan voi nhieu cong(additive noise)
# cong suat nhieu ti le voi sqr(A)
A = 0.5
# do dai tin hieu
L = 100
# bien thoi gian roi rac
n = np.arange(0, L)
# sinh tin hieu Gaussian white noise d[n](A=std cua tin hieu nhieu)
d = A*randn(L)
# sinh tin hieu goc s[n] = 2n(0.9) ^ n
s = 2*n*(0.9 ** n)
# tin hieu co nhieu x[n] = s[n]+d[n]
x = s + d

# cai dat bo loc voi kich thuoc N = 3 co PTSP: y[n] = 1/3*(x[n]+x[n-1]+x[n-2])
b = 1/3*np.ones((3))
a = [1]
y3 = lfilter(b, a, x)

# cai dat bo loc voi kich thuoc N = 5 co PTSP: y[n] = 1/5*(x[n]+x[n-1]+x[n-2]+x[n-3]+x[n-4])
b = 1/5*np.ones((5))
a = [1]
y5 = lfilter(b, a, x)

# ve do thi xep chong x[n], s[n] va y3[n] va y5[n] de test ket qua
plt.plot(n[0: L-1], x[0: L-1], 'b-')
plt.plot(n[0: L-1], s[0: L-1], 'g-')
plt.plot(n[0: L-1], y3[1: L], 'k+-')
# y3[n] bi dich phai 1 mau(tre pha) so voi x[n]
plt.plot(n[0: L-2], y5[2: L+1], 'r.-')
# y5[n] bi dich phai 2 mau(tre pha) so voi x[n]
plt.xlabel('Chi so mau n')
plt.ylabel('Bien do')
plt.legend(['x[n]', 's[n]', 'y3[n]', 'y5[n]'])

plt.show()

# sum of squared errors(SSE) bw output signal & original signal(w/o noise)
# SSE lower is better
diff1 = y3[1: L] - s[0: L-1]
diff2 = y5[2: L+1] - s[0: L-2]
print(np.sum(diff1*diff1))
print(np.sum(diff2*diff2))

# co the tang N de lam tron tin hieu nhieu hon(khu duoc noise nhieu hon),
# nhung can tranh over-smoothing(lam tron qua nhieu dan den meo tin hieu) khi
# N qua lon
