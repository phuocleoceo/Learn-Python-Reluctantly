import matplotlib.pyplot as plt
import Plot_Method

file1 = "studio_M1.wav"
lab1 = [0.94, 1.26, 1.33, 1.59, 1.66, 1.78, 1.82, 2.06]
file2 = "studio_F1.wav"
lab2 = [0.70, 1.10, 1.13, 1.22, 1.27,
        1.65, 1.70, 1.76, 1.79, 1.86, 1.92, 2.15]
file3 = "phone_M1.wav"
lab3 = [0.46, 1.39, 1.50, 1.69, 1.79,
        2.78, 2.86, 2.93, 3.10, 3.29, 3.45, 3.52]
file4 = "phone_F1.wav"
lab4 = [0.53, 1.14, 1.21, 1.35, 1.45, 1.60, 1.83,
        2.20, 2.28, 2.35, 2.40, 2.52, 2.66, 2.73, 2.75]

Tste = 0.12
Tzcr = 0.16
# Plot_Method.PlotVU(file1, lab1, 1, Tste, Tzcr)
Plot_Method.PlotVU(file2, lab2, 2, Tste, Tzcr)
# Plot_Method.PlotVU(file3, lab3, 3, Tste, Tzcr)
# Plot_Method.PlotVU(file4, lab4, 4, Tste, Tzcr)
plt.show()
