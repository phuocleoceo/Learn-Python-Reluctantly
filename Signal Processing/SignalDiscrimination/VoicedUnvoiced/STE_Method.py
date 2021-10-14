import numpy as np


def STE(Frames):
    Frame_Quantity, Frame_Length = np.shape(Frames)
    ste = np.array([0]*Frame_Quantity)
    for i in range(0, Frame_Quantity):
        ste[i] = np.sum(Frames[i]**2)

    ste = ste/np.max(ste)

    ste_signal = np.array([0]*Frame_Quantity*Frame_Length, dtype=float)
    l = 0
    for i in range(0, len(ste)):
        ste_signal[l:l+Frame_Length] = ste[i]
        l += Frame_Length

    return ste, ste_signal
