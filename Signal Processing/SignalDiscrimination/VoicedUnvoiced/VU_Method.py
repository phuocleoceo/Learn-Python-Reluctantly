import numpy as np


def vu(ste, zcr):
    vu = np.array([1 if ste[i]-zcr[i] >= 0 else 0 for i in range(0, len(ste))])
    return vu
