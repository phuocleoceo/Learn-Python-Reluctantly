import numpy as np
import math


def ACF(signal: np.ndarray, F_min: float = None, F_max: float = None, Fs: float = None) -> np.ndarray:
    if F_min == None or F_max == None:
        l = 0
        r = len(signal)
    else:
        Tmin = 1 / F_max
        Tmax = 1 / F_min
        l = math.floor(Tmin * Fs)
        r = math.floor(Tmax * Fs)

    signal = signal / max(abs(signal))
    N = len(signal)
    xx = np.array([0]*N)
    for n in range(0, N):
        if n == 0 or (n >= l and n <= r):
            for m in range(0, N-n):
                xx[n] += signal[m] * signal[m+n]

    xx = xx/xx[0]
    return xx


def find_F0(signal: np.ndarray, Fs: float) -> float:
    '''
        Tìm F0 của của một frame

        Input:
            - signal: dữ liệu biên độ samples của một frame
            - Fs : tần số của file âm thanh (file .wav)
        Output: Tần số F0 của frame
    '''
    F_min = 70
    F_max = 450
    Tmin = 1 / F_max
    Tmax = 1 / F_min
    l = math.floor(Tmin * Fs)
    r = math.floor(Tmax * Fs)

    xx = ACF(signal, F_min, F_max, Fs)

    # Cực đại cục bộ
    max_magnitude = 0
    idx = -1
    for i in range(l, r):
        if xx[i] > xx[i-1] and xx[i] > xx[i+1] and xx[i] > max_magnitude:
            idx = i
            max_magnitude = xx[i]

    # idx = lag
    # độ trễ : từ điểm đầu (cao nhất) -> cực đại cục bộ bao nhiêu sample
    # độ trễ / fs(số mẫu 1 giây) -> thời gian 1 chu kì = T0
    # F0 = 1 / T0
    F0 = 1 / (idx / Fs)

    if F0 < F_min and F0 > F_max:
        F0 = 0

    return F0
