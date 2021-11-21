from scipy.io.wavfile import read
from scipy.signal.windows import hann
from scipy.fftpack import rfft
import matplotlib.pyplot as plt
from os.path import dirname, join, abspath
from numpy.lib.scimath import log10

# Đọc file
file_name = "voice.wav"
file_path = join(dirname(abspath(__file__)), file_name)

frequency, signal = read(file_path)
print("Frequency : ", frequency)
print("Signal : ", signal)

# apply a Hanning window
window = hann(1024)
signal = signal[0:1024] * window

#  Fast Fourier Transform(FFT), lấy trị tuyệt đối
mags = abs(rfft(signal))
# convert to dB
mags = 20 * log10(mags)
# normalise to 0 dB max
mags -= max(mags)

# plot
plt.plot(mags)
# label the axes
plt.ylabel("Magnitude (dB)")  # Cường độ âm thanh
plt.xlabel("Frequency Bin")  # Tần số
# set the title
plt.title("Voice Sample")
plt.show()
