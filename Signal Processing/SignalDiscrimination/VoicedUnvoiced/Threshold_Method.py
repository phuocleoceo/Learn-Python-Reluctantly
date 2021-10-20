from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import numpy as np
import math
import Frame_Method
import STE_Method
import ZCR_Method


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


def FindT(lab, lab_label, file):
    file_path = join(dirname(abspath(__file__)), "TinHieuHuanLuyen", file)
    Fs, signal = read(file_path)
    signal = signal / 32767
    U = []
    V = []
    for i in range(0, len(lab_label)):
        n = [int(lab[i]*Fs), int(lab[i+1]*Fs)]
        if lab_label[i] == 0:
            U.append(n)
        else:
            V.append(n)

    STE_U = np.array([0]*len(U), dtype=float)
    ZCR_U = np.array([0]*len(U), dtype=float)
    for i in range(0, len(U)):
        STE_U[i] = np.sum(signal[U[i][0]:U[i][1]]**2)
        x = signal[U[i][0]:U[i][1]]
        for j in range(0, len(x)-1):
            if(x[j]*x[j+1] < 0):
                ZCR_U[i] += 1
    ZCR_U = ZCR_U/len(signal)
    STE_U = STE_U/np.max(STE_U)
    ZCR_U = ZCR_U/np.max(ZCR_U)

    STE_V = np.array([0]*len(V), dtype=float)
    ZCR_V = np.array([0]*len(V), dtype=float)
    for i in range(0, len(V)):
        STE_V[i] = np.sum(signal[V[i][0]:V[i][1]]**2)
        x = signal[V[i][0]:V[i][1]]
        for j in range(0, len(x)-1):
            if(x[j]*x[j+1] < 0):
                ZCR_V[i] += 1
    ZCR_V = ZCR_V/len(signal)
    STE_V = STE_V/np.max(STE_V)
    ZCR_V = ZCR_V/np.max(ZCR_V)

    T_STE = threshold(STE_U, STE_V)
    T_ZCR = threshold(ZCR_U, ZCR_V)
    return T_STE, T_ZCR
