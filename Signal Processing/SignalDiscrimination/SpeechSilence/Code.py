from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sounddevice as sound
import numpy as np
import math
import STE_Module

NguongChung = 0.001

file_path = join(dirname(dirname(abspath(__file__))),
                 "TrainingSignal", "studio_M1.wav")

Fs, signal = read(file_path)

signal = signal / max(abs(signal))
assert min(signal) >= -1 and max(signal) <= 1
print(">> Fs : ", Fs, "Hz")
print(">> len(signal) : ", len(signal), "samples")
print(">> Signal : ", signal)

# sound.play(signal, Fs)
# sound.wait()

ThoiLuongKhung = 0.02  # 20-25ms
DoDaiKhung = int(ThoiLuongKhung*Fs)  # 1 khung gồm bnhieu tín hiệu
SoLuongKhung = math.floor(len(signal)/DoDaiKhung)

Khung = np.zeros((SoLuongKhung, DoDaiKhung))
temp = 0
for i in range(0, SoLuongKhung):
    Khung[i, :] = signal[temp:temp+DoDaiKhung]
    temp += DoDaiKhung

ste = STE_Module.STE(Khung)

ste_wave = np.array([0]*DoDaiKhung, dtype=float)
temp = 0
for i in range(0, len(ste)):
    ste_wave[temp:temp+DoDaiKhung] = ste[i]
    temp += DoDaiKhung

print("ABC", np.sum(ste_wave))

t = np.linspace(0, len(signal)/Fs, len(signal))
t1 = np.linspace(0, len(ste_wave)/Fs, len(ste_wave))

# plt.subplot(2, 1, 1)
# plt.plot(t, signal)
# plt.title("Tin hieu vao")

# plt.subplot(2, 1, 2)
# plt.plot(t1, ste_wave)
# plt.title("Nang luong tin hieu")

# plt.show()
# plt.title('Short-Time Zero Crossing Counts')
# plt.ylabel('ZCC')
# plt.xlabel('FRAME')
# plt.show()
