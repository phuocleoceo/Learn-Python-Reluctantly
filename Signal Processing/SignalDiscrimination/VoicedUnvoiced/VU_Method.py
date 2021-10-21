import numpy as np


def vu(ste, zcr, Frames):
    Frame_Quantity, Frame_Length = np.shape(Frames)
    vu = np.array([1 if ste[i]-zcr[i] > 0 else 0 for i in range(0, len(ste))])

    N = 2
    sta = np.array([0]*len(vu), dtype=float)
    for i in range(0, len(sta), N):
        sta[i:i+N] = np.mean(vu[i:i+N])
    vu = np.array([1 if sta[i] >= 0.5 else 0 for i in range(0, len(sta))])

    vu_signal = np.array([0]*Frame_Quantity*Frame_Length, dtype=float)
    l = 0
    for i in range(0, len(ste)):
        vu_signal[l:l+Frame_Length] = vu[i]
        l += Frame_Length
    return vu, vu_signal
