from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sounddevice as sound
import numpy as np
import math
import STE_Method
import ZCR_Method
import Frame_Method
import G_Method


def PlotVU(file, lab, index):
    file_path = join(dirname(dirname(abspath(__file__))),
                     "TrainingSignal", file)

    Fs, signal = read(file_path)

    signal = signal / max(abs(signal))
    assert min(signal) >= -1 and max(signal) <= 1
    print(">> Fs : ", Fs, "Hz")
    print(">> len(signal) : ", len(signal), "samples")
    print(">> Signal : ", signal)

    # sound.play(signal, Fs)
    # sound.wait()

    NguongZCR = 0.8
    NguongSTE = 0.001
    Frame_Time = 0.02  # 20-25ms
    Frame_Length = int(Frame_Time*Fs)
    Frame_Quantity = math.floor(len(signal)/Frame_Length)

    Frames = Frame_Method.Frame_Split(Frame_Quantity, Frame_Length, signal)

    ste, ste_signal = STE_Method.STE(Frames)
    zcr, zcr_signal = ZCR_Method.ZCR(Frames, len(signal))

    plt.figure(index)
    t = np.linspace(0, len(signal)/Fs, len(signal), dtype=float)
    plt.subplot(3, 1, 1)
    plt.plot(t, signal)
    plt.xlabel("Thoi gian")
    plt.ylabel("Bien do")
    plt.title("Tin hieu vao")

    t1 = np.linspace(0, len(ste_signal)/Fs, len(ste_signal), dtype=float)
    t2 = np.linspace(0, len(zcr_signal)/Fs, len(zcr_signal), dtype=float)
    plt.subplot(3, 1, 2)
    plt.plot(t1, ste_signal)
    plt.plot(t2, zcr_signal)
    plt.xlabel("Thoi gian")
    plt.ylabel("Gia tri")
    plt.title("Nang luong va ti le vuot qua khong")

    # ste = G_Method.g(ste)
    # zcr = G_Method.g(zcr)

    # vu = np.array([1 if ste[i]-zcr[i] >= 0 else 0 for i in range(0, len(ste))])

    a = np.array([0]*len(ste))
    for i in range(0, len(ste)):
        if ste[i] > NguongSTE and zcr[i] < NguongZCR:
            a[i] = 1
        else:
            a[i] = 0

    plt.subplot(3, 1, 3)
    plt.plot(t, signal)
    plt.title("Phan doan am huu thanh va vo thanh")
    for i in range(0, len(a)-1):
        if a[i] + a[i+1] == 1:
            plt.plot([(i+1)*Frame_Time, (i+1) *
                     Frame_Time], [-1, 1], "-b")

    for x in lab:
        plt.plot([x, x], [-1, 1], "-r")

    # id = np.array([])
    # for i in range(0, Frame_Quantity):
    #     for j in range(0, len(id_zcr)):
    #         if i == id_zcr[j]:
    #             for k in range(0, len(id_ste)):
    #                 if i == id_ste[k]:
    #                     id = np.append(id, i)

    # id_voiced = np.array([0]*len(ste), dtype=float)
    # id_voiced[0] = id[0]-1
    # m = 1
    # for i in range(1, len(id)):
    #     if Frame_Time*id[i]-Frame_Time*id[i-1] > 0.2:
    #         id_voiced[m] = id[i-1]
    #         id_voiced[m+1] = id[i]-1
    #         m += 2

    # #id_voiced[m] = id[i]
    # local_voiced = Frame_Time*id_voiced
