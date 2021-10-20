from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import numpy as np
import math


file1 = "studio_M1.wav"
file_chuan1 = [0, 0.87, 2.06, 2.73]
file_lab1 = [0, 1, 0]

file2 = "studio_F1.wav"
file_chuan2 = [0, 0.68, 2.15, 2.86]
file_lab2 = [0, 1, 0]

file3 = "phone_M1.wav"
file_chuan3 = [0, 0.46, 3.52, 4.15]
file_lab3 = [0, 1, 0]

file4 = "phone_F1.wav"
file_chuan4 = [0, 0.53, 2.75, 3.23]
file_lab4 = [0, 1, 0]


def STE(Khung):
    SoLuongKhung, DoDaiKhung = np.shape(Khung)
    ste = np.array([0]*SoLuongKhung, dtype=float)
    for i in range(0, SoLuongKhung):
        ste[i] = np.sum(Khung[i]**2)
    ste = (ste-np.min(ste))/(np.max(ste)-np.min(ste))
    return ste


def Hanlde(file):
    # Đọc file
    file_path = join(dirname(dirname(abspath(__file__))),
                     "TrainingSignal", file)

    Fs, TinHieu = read(file_path)
    TinHieu = TinHieu / 32767

    ThoiLuongKhung = 0.02  # 20-25ms
    DoDaiKhung = int(ThoiLuongKhung*Fs)  # 1 khung gồm bnhieu tín hiệu
    SoLuongKhung = math.floor((2.06-0.87)*Fs/DoDaiKhung)

    Khung = np.zeros((SoLuongKhung, DoDaiKhung), dtype=float)
    temp = int(0.87*Fs)
    for i in range(0, SoLuongKhung):
        Khung[i] = TinHieu[temp:temp+DoDaiKhung]
        temp += DoDaiKhung
    print(STE(Khung))
    return STE(Khung)

    # ste = STE_Module.STE(Khung)
STE = Hanlde(file1)
print(min(STE))
print(max(STE))
