from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import numpy as np
import Frame_Method
import STE_Method
import ZCR_Method
import math


def threshold(f, g):
    Tmin = max(min(f), min(g))
    Tmax = min(max(f), max(g))
    T = (Tmin+Tmax)/2
    i = np.sum(f < T)
    p = np.sum(g > T)
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


def FindT(file, lab, lab_label):
    file_path = join(dirname(abspath(__file__)), "TinHieuHuanLuyen", file)
    Fs, signal = read(file_path)
    signal = signal / max(abs(signal))

    U = []
    V = []
    for i in range(0, len(lab_label)):
        n = [lab[i], lab[i+1]]
        if lab_label[i] == 0:
            U.append(n)
        else:
            V.append(n)

    Frame_Time = 0.02
    Frame_Length = math.floor(Frame_Time*Fs)
    Frame_Quantity = math.floor(len(signal)/Frame_Length)

    Frames = Frame_Method.Frame_Split(Frame_Quantity, Frame_Length, signal)
    ste, ste_signal = STE_Method.STE(Frames)
    zcr, zcr_signal = ZCR_Method.ZCR(Frames, len(signal))

    STE_U = np.array([0]*len(U), dtype=float)
    ZCR_U = np.array([0]*len(U), dtype=float)
    for i in range(0, len(U)):
        start = int(U[i][0]*Fs)
        end = int(U[i][1]*Fs)
        STE_U[i] = np.mean(ste_signal[start:end])
        ZCR_U[i] = np.mean(zcr_signal[start:end])

    STE_V = np.array([0]*len(V), dtype=float)
    ZCR_V = np.array([0]*len(V), dtype=float)
    for i in range(0, len(V)):
        start = int(V[i][0]*Fs)
        end = int(V[i][1]*Fs)
        STE_V[i] = np.mean(ste_signal[start:end])
        ZCR_V[i] = np.mean(zcr_signal[start:end])

    T_STE = threshold(STE_U, STE_V)
    T_ZCR = threshold(ZCR_V, ZCR_U)
    return T_STE, T_ZCR
