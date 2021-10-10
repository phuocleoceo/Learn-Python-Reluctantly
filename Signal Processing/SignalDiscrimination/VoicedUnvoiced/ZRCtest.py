from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sounddevice as sound
import numpy as np

file_path = join(dirname(dirname(abspath(__file__))),
                 "TrainingSignal", "studio_M1.wav")

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

# ZRC
DC = np.mean(signal)
newSignal = signal - DC
print("DC : ", DC)
print("mean(newSignal) : ", np.mean(newSignal))

ZRC = []
for i in range(nFrames):
    startIdx = i * sampsPerFrame
    stopIdx = startIdx + sampsPerFrame
    s = newSignal[startIdx:stopIdx]
    ZCC = 0
    for k in range(1, len(s)):
        ZCC += 0.5 * abs(np.sign(s[k]) - np.sign(s[k - 1]))
    ZRC.append(ZCC)

plt.plot(ZRC)
plt.title('Short-Time Zero Crossing Counts')
plt.ylabel('ZCC')
plt.xlabel('FRAME')
plt.show()
