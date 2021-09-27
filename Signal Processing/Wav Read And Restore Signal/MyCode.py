from os.path import dirname, join, abspath
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sounddevice as sound
import numpy as np

# Đọc file
file_name = "voice.wav"
file_path = join(dirname(abspath(__file__)), file_name)
# Tuple
frequency, signal = read(file_path)
print("Frequency : ", frequency)
print("Signal : ", signal)

plt.subplot(2, 1, 1)
plt.plot(signal)
# Nhãn cột
plt.ylabel("Amplitude")  # Biên độ
plt.xlabel("samples")  # Mẫu
# Tiêu đề
plt.title("Sample")

# T = 1/F
duration = len(signal)/frequency
print("Total Sample : ", len(signal))
print("Total seconds : ", duration)
# Các giá trị cách đều nhau a->b , step c
timeArr = np.arange(0, duration, 1/frequency)
plt.subplot(2, 1, 2)
plt.plot(timeArr, signal)
plt.xlabel("seconds")
plt.ylabel("Amplitude")
plt.title("Second")

plt.show()

# Khôi phục tín hiệu
#sound.play(signal, frequency)
#sound.play(signal, frequency/2)
sound.play(signal, frequency*2)
sound.wait()
sound.stop()

# f/2 : chậm hơn 2 lần , f*2 : nhanh hơn 2 lần

# https://www.youtube.com/watch?v=3sbFipfyqiM


# print(np.arange(1, 10, 3))
# print(np.linspace(1, 10, 3))
