import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, cos

# generate continuous-time sine waves with different frequencies
# sampling frequency
Fs = 1e3
# duration (in seconds)
D = 1.2
# create time vector t from 0(s) to D(s)
t = np.arange(0, D, 1/Fs)

# create sine functions with different freqencies

F = 0
x = cos(2*pi*F*t)
plt.subplot(5, 1, 1)
plt.plot(t, x)
plt.title('F=0')

F = 10
x = cos(2*pi*F*t)
plt.subplot(5, 1, 2)
plt.plot(t, x)
plt.title('F=10')

F = 20
x = cos(2*pi*F*t)
plt.subplot(5, 1, 3)
plt.plot(t, x)
plt.title('F=20')

F = 100
x = cos(2*pi*F*t)
plt.subplot(5, 1, 4)
plt.plot(t, x)
plt.title('F=100')

F = 200
x = cos(2*pi*F*t)
plt.subplot(5, 1, 5)
plt.plot(t, x)
plt.title('F=200')

plt.show()
