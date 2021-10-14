from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sounddevice as sound
import numpy as np
import STE_Method
import ZCR_Method
import Frame_Method
import VU_Method
import G_Method
import math


def PlotVU(file, lab, index):
    file_path = join(dirname(dirname(abspath(__file__))),
                     "TrainingSignal", file)

    Fs, signal = read(file_path)

    signal = signal / 32767
    print(">> Fs : ", Fs)
    print(">> Signal : ", signal)

    # sound.play(signal, Fs)
    # sound.wait()

    Frame_Time = 0.02
    Frame_Length = int(Frame_Time*Fs)
    Frame_Quantity = math.floor(len(signal)/Frame_Length)

    Frames = Frame_Method.Frame_Split(Frame_Quantity, Frame_Length, signal)

    ste, ste_signal = STE_Method.STE(Frames)
    zcr, zcr_signal = ZCR_Method.ZCR(Frames, len(signal))

    ste = G_Method.g(ste, 0.121)
    zcr = G_Method.g(zcr, 0.16)
    vu, vu_signal = VU_Method.vu(ste, zcr, Frames)

    plt.figure(index)
    t = np.linspace(0, len(signal)/Fs, len(signal), dtype=float)
    t1 = np.linspace(0, len(ste_signal)/Fs, len(ste_signal), dtype=float)
    t2 = np.linspace(0, len(zcr_signal)/Fs, len(zcr_signal), dtype=float)
    plt.subplot(3, 1, 1)
    plt.plot(t, signal)
    plt.plot(t1, ste_signal)
    plt.plot(t2, zcr_signal)
    plt.plot(t1, vu_signal)
    plt.legend(["Signal", "STE", "ZRC", "VU"])
    plt.xlabel("Thoi gian")
    plt.ylabel("Bien do")
    plt.title("Tin hieu vao "+file)

    plt.subplot(3, 1, 2)
    plt.plot(t, signal)
    plt.xlabel("Thoi gian")
    plt.ylabel("Bien do")
    plt.title("Phan doan am huu thanh va vo thanh")
    for i in range(0, len(vu)-1):
        if vu[i] + vu[i+1] == 1:
            plt.plot([(i+1)*Frame_Time, (i+1)*Frame_Time], [-1, 1], "-b")

    plt.subplot(3, 1, 3)
    plt.plot(t, signal)

    plt.xlabel("Thoi gian")
    plt.ylabel("Bien do")
    for x in lab:
        plt.plot([x, x], [-1, 1], "-r")
