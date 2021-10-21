import matplotlib.pyplot as plt
import numpy as np
import Plot_Method
import Threshold_Method

file1_train = "studio_M1.wav"
lab1_train = [0.87, 0.94, 1.26, 1.33, 1.59, 1.66, 1.78, 1.82, 2.06]
lab1_tr_label = [0, 1, 0, 1, 0, 1, 0, 1]

file2_train = "studio_F1.wav"
lab2_train = [0.68, 0.70, 1.10, 1.13, 1.22, 1.27,
              1.65, 1.70, 1.76, 1.79, 1.86, 1.92, 2.15]
lab2_tr_label = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

file3_train = "phone_M1.wav"
lab3_train = [0.46, 1.39, 1.50, 1.69, 1.79,
              2.78, 2.86, 2.93, 3.10, 3.29, 3.45, 3.52]
lab3_tr_label = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

file4_train = "phone_F1.wav"
lab4_train = [0.53, 1.14, 1.21, 1.35, 1.45, 1.60, 1.83,
              2.20, 2.28, 2.35, 2.40, 2.52, 2.66, 2.73, 2.75]
lab4_tr_label = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

T_STE1, T_ZCR1 = Threshold_Method.FindT(file1_train, lab1_train, lab1_tr_label)
T_STE2, T_ZCR2 = Threshold_Method.FindT(file2_train, lab2_train, lab2_tr_label)
T_STE3, T_ZCR3 = Threshold_Method.FindT(file3_train, lab3_train, lab3_tr_label)
T_STE4, T_ZCR4 = Threshold_Method.FindT(file4_train, lab4_train, lab4_tr_label)

T_STE = np.mean([T_STE1, T_STE2, T_STE3, T_STE4])
T_ZCR = np.mean([T_ZCR1, T_ZCR2, T_ZCR3, T_ZCR4])
print("T_STE : ", T_STE, " , ", "T_ZCR : ", T_ZCR)

file1_demo = "studio_M2.wav"
lab1_demo = [0.45, 0.48, 0.77, 0.79, 0.88, 0.92, 1.32, 1.37, 1.53, 1.59, 1.93]
lab1_dm_label = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

file2_demo = "studio_F2.wav"
lab2_demo = [0.77, 1.25, 1.27, 1.35, 1.41, 1.76, 1.83, 1.98, 2.06, 2.37]
lab2_dm_label = [1, 0, 1, 0, 1, 0, 1, 0, 1]

file3_demo = "phone_M2.wav"
lab3_demo = [0.53, 1.05, 1.12, 1.24, 1.31, 1.46, 1.68,
             1.97, 2.06, 2.12, 2.17, 2.30, 2.43, 2.50, 2.52]
lab3_dm_label = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

file4_demo = "phone_F2.wav"
lab4_demo = [1.02, 1.88, 1.95, 2.16, 2.25, 2.60, 2.75,
             3.34, 3.38, 3.45, 3.62, 3.80, 3.91, 4.00, 4.04]
lab4_dm_label = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# T_STE = 0.0923
# T_ZCR = 0.1445
# T_STE = 0.12
# T_ZCR = 0.16
# Plot_Method.PlotVU(file1_demo, lab1_demo, lab1_dm_label, 1, T_STE, T_ZCR)
# Plot_Method.PlotVU(file2_demo, lab2_demo, lab2_dm_label, 2, T_STE, T_ZCR)
# Plot_Method.PlotVU(file3_demo, lab3_demo, lab3_dm_label, 3, T_STE, T_ZCR)
# Plot_Method.PlotVU(file4_demo, lab4_demo, lab4_dm_label, 4, T_STE, T_ZCR)
# plt.show()
