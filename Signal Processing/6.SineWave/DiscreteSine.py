import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, pi

# create vector n of 41 elements(time base of signal)
n = np.arange(-20, 21)
# create sine functions with different freqencies

# w0 = 0
w = 0
x = cos(w*n)
plt.subplot(5, 2, 1)
plt.stem(n, x)
plt.title('w=0')

# w1 = pi/4
w = pi/8
x = cos(w*n)
plt.subplot(5, 2, 3)
plt.stem(n, x)
plt.title('w=pi/8')

# w0 = 0
w = pi/4
x = cos(w*n)
plt.subplot(5, 2, 5)
plt.stem(n, x)
plt.title('w=pi/4')

# w1 = pi/4
w = pi/2
x = cos(w*n)
plt.subplot(5, 2, 7)
plt.stem(n, x)
plt.title('w=pi/2')

# w1 = pi/4
w = pi
x = cos(w*n)
plt.subplot(5, 2, 9)
plt.stem(n, x)
plt.title('w=pi')

# ----------
# w = 2pi
w = 0
x = cos((2*pi-w)*n)
plt.subplot(5, 2, 2)
plt.stem(n, x)
plt.title('w=2pi-0')

# w = 2pi-pi/8
w = pi/8
x = cos((2*pi-w)*n)
plt.subplot(5, 2, 4)
plt.stem(n, x)
plt.title('w=2pi-pi/8')

# w = 2pi-pi/4
w = pi/4
x = cos((2*pi-w)*n)
plt.subplot(5, 2, 6)
plt.stem(n, x)
plt.title('w=2pi-pi/4')

# w = 2pi-pi/2
w = pi/2
x = cos((2*pi-w)*n)
plt.subplot(5, 2, 8)
plt.stem(n, x)
plt.title('w=2pi-pi/2')

# w = pi
w = pi
x = cos((2*pi-w)*n)
plt.subplot(5, 2, 10)
plt.stem(n, x)
plt.title('w=2pi-pi')

plt.show()
