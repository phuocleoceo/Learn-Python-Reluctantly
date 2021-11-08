import matplotlib.pyplot as plt
import sounddevice as sound
import numpy as np

A = 2
F0 = 5000
tStart = 0
tEnd = 2

Fs1 = 3*F0
t1 = np.linspace(tStart, tEnd, Fs1)
x1 = A*np.cos(2*np.pi*F0*t1)

Fs2 = int(1.5*F0)
t2 = np.linspace(tStart, tEnd, Fs2)
x2 = A*np.cos(2*np.pi*F0*t2)

plt.subplot(2, 2, 1)
plt.plot(t1[0:25], x1[0:25], "-")

plt.subplot(2, 2, 2)
plt.stem(t1[0:25], x1[0:25], "-")

plt.subplot(2, 2, 3)
plt.plot(t2[0:25], x2[0:25], "-")

plt.subplot(2, 2, 4)
plt.stem(t2[0:25], x2[0:25], "-")

plt.show()

sound.play(x1, Fs1)
# sound.play(x2, Fs2)
sound.wait()
sound.stop()
