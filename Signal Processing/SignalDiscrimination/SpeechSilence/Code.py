from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sounddevice as sound
import numpy as np
import math
import STE_Module


def Hanlde(file, file_chuan, STT):
    # Vẽ Figure
    plt.figure(STT)

    # Đọc file
    file_path = join(dirname(dirname(abspath(__file__))),
                     "TrainingSignal", file)

    Fs, TinHieu = read(file_path)

    # Chuẩn hoá về -1 1
    TinHieu = TinHieu / 32767
    print(">> Fs : ", Fs, "Hz")
    print(">> len(TinHieu) : ", len(TinHieu), "samples")
    print(">> TinHieu : ", TinHieu)

    # sound.play(TinHieu, Fs)
    # sound.wait()

    NguongChung = 0.003
    ThoiLuongKhung = 0.02  # 20-25ms
    DoDaiKhung = int(ThoiLuongKhung*Fs)  # 1 khung gồm bnhieu tín hiệu
    # bỏ đi khung cuối cùng bị dư ra
    SoLuongKhung = math.floor(len(TinHieu)/DoDaiKhung)

    # Ma trận không chứa các khung tín hiệu
    Khung = np.zeros((SoLuongKhung, DoDaiKhung), dtype=float)
    temp = 0
    for i in range(0, SoLuongKhung):
        Khung[i] = TinHieu[temp:temp+DoDaiKhung]
        temp += DoDaiKhung

    ste = STE_Module.STE(Khung)

    # STE biểu diễn cho toàn tín hiệu
    ste_wave = np.array([0]*(DoDaiKhung*SoLuongKhung), dtype=float)
    temp = 0
    for i in range(0, len(ste)):
        # for j in range(temp, temp + DoDaiKhung):
        #     ste_wave[j] = ste[i]
        ste_wave[temp:temp+DoDaiKhung] = ste[i]
        temp += DoDaiKhung

    a = np.array([0]*len(ste))
    for i in range(0, len(ste)):
        if ste[i] > NguongChung:
            a[i] = 1
        else:
            a[i] = 0

    NguongKhoangLang = int(300/(ThoiLuongKhung*1000))
    for i in range(0, len(a)-NguongKhoangLang):
        if a[i] == 1 and a[i+NguongKhoangLang] == 1:
            a[i:i+NguongKhoangLang] = 1

    a_wave = np.array([0]*(DoDaiKhung*SoLuongKhung), dtype=float)
    temp = 0
    for i in range(0, len(ste)):
        a_wave[temp:temp+DoDaiKhung] = a[i]
        temp += DoDaiKhung

        # Biểu diễn tín hiệu và năng lượng theo thời gian
    t = np.linspace(0, len(TinHieu)/Fs, len(TinHieu), dtype=float)
    t1 = np.linspace(0, len(ste_wave)/Fs, len(ste_wave), dtype=float)
    plt.subplot(2, 1, 1)
    plt.plot(t, TinHieu)
    plt.plot(t1, ste_wave)
    plt.plot(t1, a_wave)
    plt.legend(["Tin hieu", "STE", "A"])
    plt.xlabel("Thoi gian")
    plt.ylabel("Bien do")
    plt.title("Tin hieu vao "+file)

    plt.subplot(2, 1, 2)
    plt.title("Phan doan tieng noi va khoang lang")
    plt.xlabel("Thoi gian")
    plt.ylabel("Bien do")
    plt.plot(t, TinHieu)
    for i in range(0, len(a)-1):
        if (a[i] == 0 and a[i+1] == 1) or (a[i] == 1 and a[i+1] == 0):
            plt.plot([(i+1)*ThoiLuongKhung, (i+1) *
                     ThoiLuongKhung], [-1, 1], "-b")

    for x in file_chuan:
        plt.plot([x, x], [-1, 1], "-r")
