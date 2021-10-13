from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from math import log


class Wave:
    def __init__(self, nameFile="studio_male.wav"):
        self.Fs, self.data = wavfile.read(nameFile)  # đọc file dữ liệu đầu vào

    @property
    def times(self):  # trả về mảng thời gian t
        return np.arange(0, len(self.data)/self.Fs, 1/self.Fs)

    @property
    def framerate(self):  # trả về tần số lấy mẫu
        return self.Fs

    @property
    def amplitudes(self):  # trả về mảng biên độ của tín hiệu
        return self.data

    def STE(self, data=None, N=0.025):  # tính STE
        if data is None:
            data = self.data

        N = N * self.Fs
        step = int(N // 4)
        E = np.zeros(len(data) + 1)

        for i in range(1, len(data) + 1):
            E[i] = E[i - 1] + data[i - 1]**2

        ste = []
        t = []  # thời gian tương ứng với các giá trị STE
        for i in range(1, len(E), step):
            start = int(i - N//2 + 1)  # vị trí bắt đầu của khung
            end = int(i + N//2)  # vị trí kết thúc của khung

            ste.append(E[min(len(E) - 1, end)] - E[max(1, start) - 1])
            t.append((i - 1)/self.Fs)

        ste = np.array(ste)
        t = np.array(t)

        return [t, ste]

    def PlotSTE(self):
        t, ste = self.STE()
        T = 1e9
        # plt.plot(self.times, self.amplitudes/max(self.amplitudes), '#2b80ffe0')
        # plt.plot([0, t[-1]], [T, T], '#ff792be8')
        plt.plot(t, ste, '#ff0000')
        plt.show()

    def DetectSpeechSilent(self, T, minLenSilent=0.3):  # hàm tách khoảng lặng âm thanh
        silent = []  # mảng chứa index STE của các vùng khoảng lặng
        speech = []  # mảng chứa index STE của các vùng tiếng nói
        tmpSi = []  # mảng chứa index STE vùng khoảng lặng tạm thời
        t, ste = self.STE()

        timeStep = 1/self.Fs  # chu kì :))

        isFirstSilentRegion = True
        for i in range(len(ste)):  # tách khoảng lặng
            if ste[i] < T:
                tmpSi.append(i)
            else:
                if len(tmpSi) != 0 and t[tmpSi[-1]] - t[tmpSi[0]] + timeStep >= minLenSilent or isFirstSilentRegion == True:
                    silent.append(np.array(tmpSi))
                isFirstSilentRegion = False
                tmpSi = []

        if len(tmpSi) > 0:
            silent.append(np.array(tmpSi))

        if len(silent) > 0:  # tách khoảng tiếng nói
            pre = 0
            for i in range(0, len(silent)):
                for j in range(pre, silent[i][0]):
                    speech.append(j)
                pre = silent[i][-1]

        if len(silent) > 0:
            for i in range(silent[-1][-1], len(ste)):
                speech.append(i)

        speech = np.array(speech)

        return [silent, speech]

    def DetectOverlapSTE(self, silent, speech):
        t, ste = self.STE()

        Tmax = 0
        Tmin = max(ste)

        for i in silent:
            for j in i:
                Tmax = max(Tmax, ste[j])
        for i in speech:
            Tmin = min(Tmin, ste[i])

        f = []  # mảng chứa STE của vùng lặng trong overlap
        for i in silent:
            for j in i:
                if ste[j] > Tmin and ste[j] < Tmax:
                    f.append(ste[j])
        g = []  # mảng chứa STE của vùng tiếng nói trong overlap
        for i in speech:
            if ste[i] > Tmin and ste[i] < Tmax:
                g.append(ste[j])

        f = np.array(f)
        g = np.array(g)

        return [f, g, Tmin, Tmax]

    def STEThreshold(self, T=1e9):
        silent, speech = self.DetectSpeechSilent(T)

        f, g, Tmin, Tmax = self.DetectOverlapSTE(silent, speech)

        if len(f) == 0 or len(g) == 0:
            print("Break")
            return T

        Tmid = (Tmax + Tmin)/2

        i = len([i for i in f if i < Tmid])
        p = len([i for i in g if i > Tmid])
        j = -1
        q = -1
        while i != j or p != q:
            value = sum([max(i - Tmid, 0) for i in f])/len(f) - \
                sum([max(Tmid - i, 0) for i in g])/len(g)
            if value > 0:
                Tmin = Tmid
            else:
                Tmax = Tmid
                Tmid = (Tmax + Tmin)/2
                j = i
                q = p
                i = len([i for i in f if i < Tmid])
                p = len([i for i in g if i > Tmid])

        return Tmid

    def SpeechSilentDiscrimination(self, N=0.025):
        step = int(N * self.Fs // 4)
        T = self.STEThreshold()
        f, g = self.DetectSpeechSilent(T)

        f = [i * step for i in f]

        g = [g * step for i in g]

        silent = []
        speech = []
        for i in f:
            silent.append(self.data[i[0]: i[-1] + 1])

        if len(f) > 0:
            pre = f[0][-1] + 1
            for i in range(1, len(f)):
                speech.append(self.data[pre: f[i][0]])
                pre = f[i][-1]

        return [silent, speech]

    def PlotSpeechSilentDiscrimination(self):
        n = self.times
        T = self.STEThreshold()
        f, g = self.DetectSpeechSilent(T)

        t, ste = self.STE()

        fig, [plt1, plt2] = plt.subplots(2, 1)

        for i in f:
            start, end = i[0], i[-1]

            plt1.plot([t[start], t[start]], [0, max(ste)], '#00ca06e0')
            plt1.plot([t[end], t[end]], [0, max(ste)], '#d87bff')

            plt2.plot([t[start], t[start]], [-1, 1], '#00ca06e0')
            plt2.plot([t[end], t[end]], [-1, 1], '#d87bff')

            print(t[start], t[end], end=" ")

        print()

        plt1.plot([0, n[-1]], [T, T], '#ff792be8')
        plt1.plot(t, ste, '#2b80ffe0')

        data = self.amplitudes

        plt2.plot(n, data/max(data), '#2b80ffe0')
        plt2.plot(t, ste/max(ste), '#ff0000')

        plt.show()

    def ZCR(self, data, N=0.025):  # hàm tính ZCR
        N = N * self.Fs
        step = int(N // 4)

        sign = np.zeros(len(data) + 1)

        for i in range(1, len(data) + 1):
            sign[i] = 1 if data[i - 1] >= 0 else -1

        tmp = np.zeros(len(data) + 1)
        for i in range(1, len(data) + 1):
            tmp[i] = abs(sign[i] - sign[i - 1])

        for i in range(1, len(data) + 1):
            tmp[i] = tmp[i - 1] + tmp[i]

        zcr = []
        n = []
        for i in range(1, len(tmp), step):
            start = int(i - N//2 + 1)  # vị trí bắt đầu của khung
            end = int(i + N//2)  # vị trí kết thúc của khung

            zcr.append(tmp[min(end, len(tmp) - 1)] - tmp[max(1, start) - 1])
            n.append((i - 1)/self.Fs)

        return [np.array(n), np.array(zcr)]

    def PlotZCR(self, data):
        t = np.arange(0, len(data)/self.Fs, 1/self.Fs)
        n, zcr = self.ZCR(data=data)
        plt.plot(t, data/max(data), '#2b80ffe0')
        plt.plot(n, zcr, '#ff0000')
        plt.show()

    def g(self, f):  # hàm chuẩn hóa
        fmin = min(f)
        fmax = max(f)
        T = (fmin + fmax)/3
        res = [(i - T)/(fmax - T) if i >= T else (i - T)/(T - fmin) for i in f]
        return np.array(res)

    def VU(self, data):

        nzcr, zcr = self.ZCR(data=data)
        nste, ste = self.STE(data=data)

        zcr = self.g(zcr)
        ste = self.g(ste)

        vu = np.array(
            [1 if ste[i] - zcr[i] >= 0 else 0 for i in range(len(ste))])

        N = 20

        tmp = np.zeros(len(vu) + 1)
        for i in range(1, len(vu) + 1):
            tmp[i] = tmp[i - 1] + vu[i - 1]

        sta = np.zeros(len(vu))
        for i in range(0, len(vu)):
            sta[i] = (tmp[min(i + N//2, len(tmp) - 2) + 1] -
                      tmp[max(0, i - N//2) + 1])/N

        vu = np.array([1 if sta[i] >= 0.5 else 0 for i in range(len(sta))])
        return [nste, vu]

    def PlotVU(self, data):
        n, vu = self.VU(data)

        t = np.arange(0, len(data)/self.Fs, 1/self.Fs)
        plt.plot(t, data/max(data), '#2b80ffe0')
        plt.plot(n, vu, '#ff0000')
        plt.show()


def main():
    name = ['44.1kHz.wav', '44.1kHz_female.wav', 'lab_female.wav', 'lab_male.wav',
            'phone_female.wav', 'phone_male.wav', 'studio_female.wav', 'studio_male.wav']
    for i in name:
        key = input()
        if key == "no":
            break
        print(i)
        wave = Wave(i)
        wave.PlotSpeechSilentDiscrimination()
        # silent, speech = wave.SpeechSilentDiscrimination()
        # for j in speech:
        # 	key = input()
        # 	if key == "no":
        # 		break
        # 	wave.PlotZCR(data = j)
        # 	wave.PlotSpeechSilentDiscrimination()


if __name__ == '__main__':
    main()
