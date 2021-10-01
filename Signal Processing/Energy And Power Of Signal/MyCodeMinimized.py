from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import numpy as np

file_path = join(dirname(abspath(__file__)), "studio_male.wav")

frequency, signal = read(file_path)
signal = signal/32767

print(frequency, ",", signal)

E = np.sum(signal**2)
print(">> Energy : ", E)

L = len(signal)
P = E/L
print(">> Power : ", P)

# https://dsp.stackexchange.com/questions/44571/why-is-there-an-amplitude-difference-in-matlab-and-python
