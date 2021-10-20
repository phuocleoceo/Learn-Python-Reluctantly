import matplotlib.pyplot as plt
import Threshold_Method
import Plot_Method
import numpy as np

file1 = "studio_M1.wav"
lab1 = [0.87, 0.94, 1.26, 1.33, 1.59, 1.66, 1.78, 1.82, 2.06]
lab1_label = [0, 1, 0, 1, 0, 1, 0, 1]

file2 = "studio_F1.wav"
lab2 = [0.68, 0.70, 1.10, 1.13, 1.22, 1.27,
        1.65, 1.70, 1.76, 1.79, 1.86, 1.92, 2.15]
lab2_label = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

file3 = "phone_M1.wav"
lab3 = [0.46, 1.39, 1.50, 1.69, 1.79,
        2.78, 2.86, 2.93, 3.10, 3.29, 3.45, 3.52]
lab3_label = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

file4 = "phone_F1.wav"
lab4 = [0.53, 1.14, 1.21, 1.35, 1.45, 1.60, 1.83,
        2.20, 2.28, 2.35, 2.40, 2.52, 2.66, 2.73, 2.75]
lab4_label = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

T_STE1, T_ZCR1 = Threshold_Method.FindT(lab1, lab1_label, file1)
T_STE2, T_ZCR2 = Threshold_Method.FindT(lab2, lab2_label, file2)
T_STE3, T_ZCR3 = Threshold_Method.FindT(lab3, lab3_label, file3)
T_STE4, T_ZCR4 = Threshold_Method.FindT(lab4, lab4_label, file4)

T_STE = np.mean([T_STE1, T_STE2, T_STE3, T_STE4])
T_ZCR = np.mean([T_ZCR1, T_ZCR2, T_ZCR3, T_ZCR4])
print("T_STE : ", T_STE, " , ", "T_ZCR : ", T_ZCR)
# Plot_Method.PlotVU(file1, lab1, 1, lab1_label, T_STE, T_ZCR)
# Plot_Method.PlotVU(file2, lab2, 2, lab2_label, T_STE, T_ZCR)
# Plot_Method.PlotVU(file3, lab3, 3, lab3_label, T_STE, T_ZCR)
# Plot_Method.PlotVU(file4, lab4, 4, lab4_label, T_STE, T_ZCR)
# plt.show()
