from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sounddevice as sound
import numpy as np
import math
import STE_Method
import ZRC_Method

# file = "phone_F1.wav"
# file_chuan = [0.53, 1.14, 1.21, 1.35, 1.45, 1.60, 1.83,
#               2.20, 2.28, 2.35, 2.40, 2.52, 2.66, 2.73, 2.75]
# file = "phone_M1.wav"
# file_chuan = [0.46, 1.39, 1.50, 1.69, 1.79,
#               2.78, 2.86, 2.93, 3.10, 3.29, 3.45, 3.52]
# file = "studio_M1.wav"
# file_chuan = [0.87, 0.94, 1.26, 1.33, 1.59, 1.66, 1.78, 1.82, 2.06]
file = "studio_F1.wav"
file_chuan = [0.68, 0.70, 1.10, 1.13, 1.22, 1.27,
              1.65, 1.70, 1.76, 1.79, 1.86, 1.92, 2.15]

file_path = join(dirname(dirname(abspath(__file__))),
                 "TrainingSignal", file)

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

id_ste = np.argwhere(ste > NguongSTE)
id_zrc = np.argwhere(zrc < NguongZRC)

a = np.array([0]*len(ste))
for i in range(0, len(ste)):
    if ste[i] > NguongSTE and zrc[i] < NguongZRC:
        a[i] = 1
    else:
        a[i] = 0


for i in range(0, len(a)-1):
    if (a[i] == 0 and a[i+1] == 1) or (a[i] == 1 and a[i+1] == 0):
        plt.subplot(3, 1, 3)
        plt.plot(t, signal)
        plt.title("Phan doan am huu thanh va vo thanh")
        plt.plot([i*ThoiLuongKhung, i * ThoiLuongKhung], [-1, 1], "-b")

for x in file_chuan:
    plt.plot([x, x], [-1, 1], "-r")

plt.show()
# id = np.array([])
# for i in range(0, SoLuongKhung):
#     for j in range(0, len(id_zrc)):
#         if i == id_zrc[j]:
#             for k in range(0, len(id_ste)):
#                 if i == id_ste[k]:
#                     id = np.append(id, i)

# id_voiced = np.array([0]*len(ste), dtype=float)
# id_voiced[0] = id[0]-1
# m = 1
# for i in range(1, len(id)):
#     if ThoiLuongKhung*id[i]-ThoiLuongKhung*id[i-1] > 0.2:
#         id_voiced[m] = id[i-1]
#         id_voiced[m+1] = id[i]-1
#         m += 2

# #id_voiced[m] = id[i]
# local_voiced = ThoiLuongKhung*id_voiced
