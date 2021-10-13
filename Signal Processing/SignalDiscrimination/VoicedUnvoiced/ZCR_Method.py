import numpy as np


def ZCR(Khung, N):
    Frame_Quantity, Frame_Length = np.shape(Khung)
    zrc = np.array([0]*Frame_Quantity)
    for i in range(0, Frame_Quantity):
        x = Khung[i]
        for j in range(0, len(x)-1):
            if(x[j]*x[j+1] < 0):
                zrc[i] += 1

    zrc = zrc/N
    zrc = zrc/np.max(zrc)

    zrc_signal = np.array([0]*Frame_Quantity*Frame_Length, dtype=float)
    l = 0
    for i in range(0, len(zrc)):
        zrc_signal[l:l+Frame_Length] = zrc[i]
        l += Frame_Length

    return zrc, zrc_signal
