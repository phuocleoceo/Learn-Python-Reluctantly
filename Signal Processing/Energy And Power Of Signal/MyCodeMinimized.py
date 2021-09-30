from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import numpy as np

file_path = join(dirname(abspath(__file__)), "voice.wav")

frequency, signal = read(file_path)
print(frequency, ",", signal)
signal = np.array(signal, dtype=np.int64)

E = 0
for x in signal:
    E += x*x
print(">> Energy : ", E)

L = len(signal)
P = E/L
print(">> Power : ", P)
