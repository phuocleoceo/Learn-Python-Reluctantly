import numpy as np


def g(f):
    fmin = np.min(f)
    fmax = np.max(f)
    T = (fmin+fmax)/3
    return np.array([(x-T)/(fmax-T) if x >= T else (x-T)/(T-fmin) for x in f])
