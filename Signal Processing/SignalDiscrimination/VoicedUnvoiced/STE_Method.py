import numpy as np


def STE(Khung):
    SoLuongKhung, DoDaiKhung = np.shape(Khung)
    ste = np.array([0]*SoLuongKhung)
    for i in range(0, SoLuongKhung):
        ste[i] = np.sum(Khung[i]**2)
    ste = ste/np.max(ste)

    ste_mau = np.array([0]*SoLuongKhung*DoDaiKhung, dtype=float)
    temp = 0
    for i in range(0, len(ste)):
        ste_mau[temp:temp+DoDaiKhung] = ste[i]
        temp += DoDaiKhung

    return ste, ste_mau
