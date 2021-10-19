import numpy as np


def threshold(f, g):
    Tmin = max(min(f), min(g))
    Tmax = min(max(f), max(g))
    T = (Tmin+Tmax)/2
    i = len(np.argwhere(f < T))
    p = len(np.argwhere(g > T))
    j = -1
    q = -1
    while i != j or p != q:
        if 1/len(f)*np.sum([max(n-T, 0) for n in f])-1/len(g)*np.sum([max(T-n, 0) for n in g]) > 0:
            Tmin = T
        else:
            Tmax = T
        T = (Tmin+Tmax)/2
        j = i
        q = p
        i = np.sum(f < T)
        p = np.sum(g > T)
    return T
