import numpy as np


ste = np.array([5, 3, 2, 10, 20])

# x-2  /18

# ste = (ste-np.min(ste))/(np.max(ste)-np.min(ste))
ste = np.append(ste, 100)
print(ste)
