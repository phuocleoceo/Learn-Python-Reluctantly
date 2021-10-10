import numpy as np


def ZRC(Khung, N):
    SoLuongKhung, DoDaiKhung = np.shape(Khung)
    zrc = np.array([0]*SoLuongKhung)
    for i in range(0, SoLuongKhung):
        x = Khung[i]
        zrc[i] = 0
        for j in range(0, len(x)-1):
            if(x[j]*x[j+1] < 0):
                zrc[i] += 1

    zrc = zrc/N
    zrc = zrc/np.max(zrc)

    zrc_mau = np.array([0]*SoLuongKhung*DoDaiKhung, dtype=float)
    temp = 0
    for i in range(0, len(zrc)):
        zrc_mau[temp:temp+DoDaiKhung] = zrc[i]
        temp += DoDaiKhung

    return zrc, zrc_mau
