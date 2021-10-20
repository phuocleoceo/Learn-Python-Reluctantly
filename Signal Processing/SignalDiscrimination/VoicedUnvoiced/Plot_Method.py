from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sounddevice as sound
import numpy as np
import Frame_Method
import STE_Method
import ZCR_Method
import VU_Method
import G_Method
import math


def PlotVU(file, lab, lab_label, index, Tste=0.12, Tzcr=0.16):
    # file_path = join(dirname(abspath(__file__)), "TinHieuHuanLuyen", file)
    file_path = join(dirname(abspath(__file__)), "TinHieuKiemThu", file)

    Fs, signal = read(file_path)

    signal = signal / 32767
    print(">> Fs : ", Fs, ", Signal : ", signal)
    # sound.play(signal, Fs)
    # sound.wait()

    Frame_Time = 0.02
    Frame_Length = int(Frame_Time*Fs)
    Frame_Quantity = math.floor(len(signal)/Frame_Length)

    Frames = Frame_Method.Frame_Split(Frame_Quantity, Frame_Length, signal)

    ste, ste_signal = STE_Method.STE(Frames)
    zcr, zcr_signal = ZCR_Method.ZCR(Frames, len(signal))

    ste = G_Method.g(ste, Tste)
    zcr = G_Method.g(zcr, Tzcr)
    vu, vu_signal = VU_Method.vu(ste, zcr, Frames)

    plt.figure(index)
    t_signal = np.linspace(0, len(signal)/Fs, len(signal), dtype=float)
    t_ste = np.linspace(0, len(ste_signal)/Fs, len(ste_signal), dtype=float)
    t_zcr = np.linspace(0, len(zcr_signal)/Fs, len(zcr_signal), dtype=float)
    plt.subplot(3, 1, 1)
    plt.plot(t_signal, signal)
    plt.plot(t_ste, ste_signal)
    plt.plot(t_zcr, zcr_signal)
    plt.plot(t_ste, vu_signal)
    plt.legend(["Signal", "STE", "ZCR", "VU"])
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Signal " + file)

    plt.subplot(3, 1, 2)
    plt.plot(t_signal, signal)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Voiced and Unvoiced Discrimination")
    for i in range(0, len(vu)-1):
        if vu[i] + vu[i+1] == 1:
            plt.plot([(i+1)*Frame_Time, (i+1)*Frame_Time], [-1, 1], "-b")
            if vu[i] == 0:
                plt.text((i+1)*Frame_Time, 0.7, "V")
            else:
                plt.text((i+1)*Frame_Time, 0.7, "U")

    plt.subplot(3, 1, 3)
    plt.plot(t_signal, signal)
    plt.title("Lab")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    for i in range(0, len(lab)):
        plt.plot([lab[i], lab[i]], [-1, 1], "-r")
        if i != len(lab) - 1:
            if lab_label[i] == 0:
                plt.text(lab[i], 0.7, "U")
            else:
                plt.text(lab[i], 0.7, "V")
