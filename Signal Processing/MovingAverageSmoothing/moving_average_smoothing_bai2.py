# chuong trinh lam tron 1 tin hieu de khu nhieu(denoise)
# dung bo loc trung binh truot 3 diem(3-points moving-averaging filter)
# co PTSP: y[n] = 1/3*(x[n]+x[n-1]+x[n-2])(he nhan qua)
# problem statement: co tin hieu bi lan voi nhieu x[n], di khoi phuc lai
# tin hieu goc s[n](an trong x[n])
# ky vong KQ: y[n] cang giong s[n] cang tot
from scipy.signal import convolve, lfilter
import matplotlib.pyplot as plt
from numpy.random import randn
import numpy as np


# sinh tin hieu bi lan voi nhieu cong(additive noise)
# cong suat nhieu ti le voi sqr(A)
A = 0.5
# do dai tin hieu
L = 51
# bien thoi gian roi rac
n = np.arange(0, L)
# sinh tin hieu Gaussian white noise d[n](A=std cua tin hieu nhieu)
d = A*randn(L)
# sinh tin hieu goc s[n] = 2n(0.9) ^ n
s = 2*n*(0.9 ** n)
# tin hieu co nhieu x[n] = s[n]+d[n]
x = s + d

plt.figure(1)
plt.subplot(3, 1, 1)
plt.plot(n, d, 'r-', n, s, 'k--', n, x, 'b-.')
plt.xlabel('Chi so thoi gian n')
plt.ylabel('Bien do')
plt.legend(['d[n]', 's[n]', 'x[n]'])
plt.title('Noise" d[n] vs. original s[n] vs. noisy signals x[n]')

#############################################################################################
# CACH 1: cai dat he thong bang cach dich thoi gian va tinh
# TBC cua 3 tin hieu

# x1[n] = x[n]
x1 = x
# x2[n] = x[n-1]
x2 = np.append(0, x[0:L-1])
# x3[n] = x[n-2]
x3 = np.concatenate(([0, 0], x[0:L-2]))

# ve do thi x[n], x[n-1], x[n-2]
plt.subplot(3, 1, 2)
plt.plot(n, x1, 'r-.', n, x2, 'b-.', n, x3, 'k-.')
plt.xlabel('Chi so thoi gian n')
plt.ylabel('Bien do')
plt.legend(['x[n]', 'x[n-1]', 'x[n-2]'])
plt.title('time-shifted signals of x[n]')

y1 = 1/3*(x1+x2+x3)

# ve do thi y1[n] vs. s[n]
plt.subplot(3, 1, 3)
plt.plot(n, y1[0:L], 'r-', n, s[0:L], 'b-')
plt.xlabel('Chi so thoi gian n')
plt.ylabel('Bien do')
plt.legend(['y1[n]', 's[n]'])
plt.title('3-points smoothed y1[n] vs. original signal s[n]')

#############################################################################################
# cach 2: cai dat he thong bang cach dung ham tinh tong chap conv()
# he lay TB truot KHONG nhan qua = ghep noi tiep he som 1 don vi co h1[n] = delta(n+1)
# voi he lay TB truot nhan qua co PTSP yNQ[n] = 1/3*(x[n]+x[n+1]+x[n+2])

# hNQ[n] = [1/3, 1/3, 1/3](Matlab hieu la n=0, 1, 2)
hNQ = 1/3 * np.ones((3))
y2 = convolve(x, hNQ)

# ve do thi y2[n] vs. s[n]
plt.figure(2)
plt.plot(n, y2[0:L], 'r-', n, s[0:L], 'b-')
plt.xlabel('Chi so thoi gian n')
plt.ylabel('Bien do')
plt.legend(['y2[n]', 's[n]'])
plt.title('3-points smoothed y2[n] vs. original signal s[n]')

# ve do thi xep chong y1[n] va y2[n] de test ket qua
plt.figure(3)
plt.plot(n, y1, 'r-', n, y2[0:L], 'b-')
plt.xlabel('Chi so thoi gian n')
plt.ylabel('Bien do')
plt.legend(['y1[n]', 'y2[n]'])
plt.title('cach1  vs. cach2')

#############################################################################################
# cach 3: dung vong lap(hieu n la mot chi so mau nao do)
# PUT YOUR CODE HERE
plt.figure(4)

y3 = np.array([0]*L, dtype=float)
x_z = np.concatenate(([0, 0], x))
# Su dung bien i vi trong Python, neu dung bien n de lap thi se trung voi n thoi gian o tren
for i in range(0, L):
    j = i+2
    y3[i] = 1/3*(x_z[j]+x_z[j-1]+x_z[j-2])

plt.plot(n, y1[0:L], 'r-', n, y2[0:L], 'b-', n, y3[0:L], 'g-')
plt.xlabel('Chi so thoi gian n')
plt.ylabel('Bien do')
plt.legend(['y1[n]', 'y2[n]', 'y3[n]'])
plt.title('cach1  vs. cach2  vs. cach3')

#############################################################################################
# cach 4: dung lfilter cua scipy.signal
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html

b = [1/3, 1/3, 1/3]
a = [1]
y4 = lfilter(b, a, x)
plt.plot(n, y1[0:L], 'r-', n, y2[0:L], 'b-',
         n, y3[0:L], 'g-', n, y4[0:L], 'y-')
plt.xlabel('Chi so thoi gian n')
plt.ylabel('Bien do')
plt.legend(['y1[n]', 'y2[n]', 'y3[n]', 'y4[n]'])
plt.title('cach1  vs. cach2  vs. cach3 vs. cach 4')

plt.show()
