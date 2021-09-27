import sounddevice as sound
from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np

file_path = join(dirname(abspath(__file__)), "voice.wav")

frequency, signal = read(file_path)
print(frequency, ",", signal)

# plt.plot(signal)
# plt.ylabel("Amplitude")
# plt.xlabel("Samples")
# plt.title("Sample")
# plt.show()

# sound.play(signal, frequency)
# sound.wait()
# sound.stop()
L = len(signal)

# Cách 1
# E1 = 0
# for i in range(0, L):
#     E1 += signal[i]*signal[i]
# print(E1)

# Cách 2
A = np.array([x*x for x in signal])
E2 = np.sum(A)
print(E2)

Power = E2/L
print(Power)
