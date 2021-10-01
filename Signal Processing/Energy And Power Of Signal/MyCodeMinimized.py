from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import numpy as np

file_path = join(dirname(abspath(__file__)), "studio_male.wav")

frequency, signal = read(file_path)
signal = np.array([x/32767 for x in signal])

print(frequency, ",", signal)

E = 0
for x in signal:
    E += x*x
print(">> Energy : ", E)

L = len(signal)
P = E/L
print(">> Power : ", P)

# https://dsp.stackexchange.com/questions/44571/why-is-there-an-amplitude-difference-in-matlab-and-python
