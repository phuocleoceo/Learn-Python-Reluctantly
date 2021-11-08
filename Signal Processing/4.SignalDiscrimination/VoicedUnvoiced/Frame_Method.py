import numpy as np


def Frame_Split(Frame_Quantity, Frame_Length, signal):
    Frames = np.zeros((Frame_Quantity, Frame_Length), dtype=float)
    l = 0
    for i in range(0, Frame_Quantity):
        Frames[i] = signal[l:l+Frame_Length]
        l += Frame_Length
    return Frames
