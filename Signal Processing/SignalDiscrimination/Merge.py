from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sounddevice as sound
import numpy as np

file_path = join(dirname(abspath(__file__)), "TrainingSignal", "studio_M1.wav")

fs, signal = read(file_path)

signal = signal / max(abs(signal))
assert min(signal) >= -1 and max(signal) <= 1
print(">> Fs : ", fs, "Hz")
print(">> len(signal) : ", len(signal), "samples")
print(">> Signal : ", signal)

# sound.play(signal, fs)
# sound.wait()

# plt.plot(signal)
# plt.ylabel("Amplitude")
# plt.xlabel("Samples")
# plt.show()

sampsPerMilli = int(fs / 1000)
millisPerFrame = 20
sampsPerFrame = sampsPerMilli * millisPerFrame
nFrames = int(len(signal) / sampsPerFrame)

print(">> Samples/Millisecond : ", sampsPerMilli)
print(">> Samples/[", millisPerFrame, "ms]frame : ", sampsPerFrame)
print(">> Number of frames : ", nFrames)

# STE
STEs = []                                      # list of short-time energies
for k in range(nFrames):
    startIdx = k * sampsPerFrame
    stopIdx = startIdx + sampsPerFrame
    window = np.zeros(signal.shape)
    window[startIdx:stopIdx] = 1               # rectangular window
    STE = sum((signal ** 2) * (window ** 2))
    STEs.append(STE)
# fc = 20
# a = np.exp(-fc * 2 * np.pi / fs)
# STEs = []
# for n in range(len(signal)):
#     if n == 0:
#         STEs.append(a * 0 + signal[n] ** 2)           # base-case
#     else:
#         STEs.append(a * STEs[n - 1] + signal[n] ** 2)


# ZRC
DC = np.mean(signal)
newSignal = signal - DC
print("DC : ", DC)
print("mean(newSignal) : ", np.mean(newSignal))

ZRCs = []
for i in range(nFrames):
    startIdx = i * sampsPerFrame
    stopIdx = startIdx + sampsPerFrame
    s = newSignal[startIdx:stopIdx]
    ZCC = 0
    for k in range(1, len(s)):
        ZCC += 0.5 * abs(np.sign(s[k]) - np.sign(s[k - 1]))
    ZRCs.append(ZCC)


plt.subplot(2, 1, 1)
plt.plot(STEs)
plt.title("Short-Time Energy")
plt.ylabel("ENERGY")
plt.xlabel("FRAME")

plt.subplot(2, 1, 2)
plt.plot(ZRCs)
plt.title("Short-Time Zero Crossing Rate")
plt.ylabel("ZRC")
plt.xlabel("FRAME")

plt.show()
