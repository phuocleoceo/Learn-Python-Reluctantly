import numpy as np


def STE(Khung):
    SoLuongKhung, DoDaiKhung = np.shape(Khung)
    ste = np.array([0]*SoLuongKhung)
    for i in range(0, SoLuongKhung):
        ste[i] = np.sum(Khung[i]**2)

    ste = (ste-np.min(ste))/(np.max(ste)-np.min(ste))
    return ste
