from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sounddevice as sound
import numpy as np
import math
import STE_Method
import ZRC_Method

file_path = join(dirname(dirname(abspath(__file__))),
                 "TrainingSignal", "studio_M1_1b.wav")

Fs, signal = read(file_path)

signal = signal / max(abs(signal))
assert min(signal) >= -1 and max(signal) <= 1
print(">> Fs : ", Fs, "Hz")
print(">> len(signal) : ", len(signal), "samples")
print(">> Signal : ", signal)

# sound.play(signal, Fs)
# sound.wait()

NguongZRC = 0.8
NguongSTE = 0.001
ThoiLuongKhung = 0.02  # 20-25ms
DoDaiKhung = int(ThoiLuongKhung*Fs)  # 1 khung gồm bnhieu tín hiệu
SoLuongKhung = math.floor(len(signal)/DoDaiKhung)

Khung = np.zeros((SoLuongKhung, DoDaiKhung), dtype=float)
temp = 0
for i in range(0, SoLuongKhung):
    Khung[i, :] = signal[temp:temp+DoDaiKhung]
    temp += DoDaiKhung

ste, ste_mau = STE_Method.STE(Khung)
zrc, zrc_mau = ZRC_Method.ZRC(Khung, len(signal))

t = np.linspace(0, len(signal)/Fs, len(signal), dtype=float)
plt.subplot(3, 1, 1)
plt.plot(t, signal)
plt.xlabel("Thoi gian")
plt.ylabel("Bien do")
plt.title("Tin hieu vao")

t1 = np.linspace(0, len(ste_mau)/Fs, len(ste_mau), dtype=float)
t2 = np.linspace(0, len(zrc_mau)/Fs, len(zrc_mau), dtype=float)
plt.subplot(3, 1, 2)
plt.plot(t1, ste_mau)
plt.plot(t2, zrc_mau)
plt.xlabel("Thoi gian")
plt.ylabel("Gia tri")
plt.title("Nang luong va ti le vuot qua khong")

# a = np.array([0]*len(ste))
# for i in range(0, len(ste)):
#     if ste[i] > NguongSTE:
#         a[i] = 1
#     else:
#         a[i] = 0

# NguongKhoangLang = int(300/(ThoiLuongKhung*1000))
# for i in range(0, len(a)-NguongKhoangLang):
#     if a[i] == 1 and a[i+NguongKhoangLang] == 1:
#         a[i:i+NguongKhoangLang] = 1

# for i in range(0, len(a)-1):
#     if (a[i] == 0 and a[i+1] == 1) or (a[i] == 1 and a[i+1] == 0):
#         plt.subplot(3, 1, 3)
#         plt.plot(t, signal)
#         plt.title("Phan doan tieng noi va khoang lang")
#         plt.plot([(i+1)*ThoiLuongKhung, (i+1) *
#                  ThoiLuongKhung], [-1, 1], "--k")

plt.show()
