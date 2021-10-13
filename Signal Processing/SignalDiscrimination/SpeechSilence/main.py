import matplotlib.pyplot as plt
import Code

file1 = "studio_M1.wav"
file_chuan1 = [0, 0.87, 2.06, 2.73]
file2 = "studio_F1.wav"
file_chuan2 = [0, 0.68, 2.15, 2.86]
file3 = "phone_M1.wav"
file_chuan3 = [0, 0.46, 3.52, 4.15]
file4 = "phone_F1.wav"
file_chuan4 = [0, 0.53, 2.75, 3.23]

Code.Hanlde(file1, file_chuan1, 1)
Code.Hanlde(file2, file_chuan2, 2)
Code.Hanlde(file3, file_chuan3, 3)
Code.Hanlde(file4, file_chuan4, 4)
plt.show()
