import numpy as np


def STE(Khung):
    SoLuongKhung, DoDaiKhung = np.shape(Khung)
    ste = np.array([0]*SoLuongKhung)
    for i in range(0, SoLuongKhung):
        ste[i] = np.sum(Khung[i, :]**2)
    return ste
