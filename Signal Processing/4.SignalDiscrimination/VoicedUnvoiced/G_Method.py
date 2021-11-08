import numpy as np


def g(f, T):
    fmin = np.min(f)
    fmax = np.max(f)
    return np.array([(x-T)/(fmax-T) if x >= T else (x-T)/(T-fmin) for x in f])
