import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sound
from numpy import pi, sin
from scipy.fft import fft

# plot magnitue spectrum of signal using FFT
# generate signal
# in Hz
Fs = 10000
# in Hz
F1 = 1000
# in Hz
F2 = 2000
# in Hz
F3 = 3000
# in seconds
duration = 2
# number of signal samples for plotting
nSamples = 100

t = np.arange(0, duration, 1/Fs)
y = 3*sin(2*pi*F1*t)+2*sin(2*pi*F2*t)+1*sin(2*pi*F3*t)

# signal of 2 frequencies
# sound.play(y, Fs)
# sound.wait()
# sound.stop()


# normalize signal magnitude
max_value = max(abs(y))
y = y/max_value

# create time base
t = np.arange(1/Fs, len(y)/Fs, 1/Fs)
plt.subplot(2, 1, 1)
plt.plot(t[0: nSamples], y[0: nSamples], 'k', 'LineWidth', 1)
plt.title('Signal waveform')
plt.xlabel('Time (seconds)')
plt.ylabel('Normalized magnitude')

# plot linear magnitue spectrum of signal
# number of frequency samples
N_FFT = 1024
# get samples of magnitude spectrum
dfty = abs(fft(y, N_FFT))
# k axis
k = np.arange(0, N_FFT)
# frequency axis
w = k*Fs/N_FFT

plt.subplot(2, 1, 2)
# N_FFT/2 => float
plt.plot(w[0: int(N_FFT/2)], dfty[0: int(N_FFT/2)], 'k', 'LineWidth', 1)
plt.title('Linear Magnitude Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.show()
