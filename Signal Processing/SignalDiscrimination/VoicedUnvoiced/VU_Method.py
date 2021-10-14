import numpy as np


def vu(ste, zcr, Frames):
    Frame_Quantity, Frame_Length = np.shape(Frames)
    vu = np.array([1 if ste[i]-zcr[i] >= 0 else 0 for i in range(0, len(ste))])

    vu_signal = np.array([0]*Frame_Quantity*Frame_Length, dtype=float)
    l = 0
    for i in range(0, len(ste)):
        vu_signal[l:l+Frame_Length] = vu[i]
        l += Frame_Length
    # N = 5
    # sta = np.array([0]*len(vu))
    # l = 0
    # for i in range(0, len(vu)):
    #     sta[i] = np.sum(vu[l:l+N])/N
    #     l += N
    # vu = np.array([1 if sta[i] >= 0.5 else 0 for i in range(0, len(sta))])
    return vu, vu_signal
