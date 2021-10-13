import numpy as np


def find_threshold(ste):
    HistSTE, index_STE = np.histogram(ste, round(len(ste)))

    maxHistSTE1 = 0
    maxHistSTE2 = 0
    maxIndex1 = 0
    maxIndex2 = 0
    for i in range(1, len(HistSTE)-1):
        pre = i-1
        nex = i+1
        while(HistSTE[i] == HistSTE[nex]):
            nex += 1
        if HistSTE[i] > HistSTE[pre] and HistSTE[i] > HistSTE[nex]:
            if(maxIndex1 == 0):
                maxHistSTE1 = HistSTE[i]
                maxIndex1 = 1
            else:
                maxHistSTE2 = HistSTE[i]
                maxIndex2 = 1
                break
        i = nex

    maxHistSTE1 = index_STE[maxIndex1]
    maxHistSTE2 = index_STE[maxIndex2]
    W = 1e10
    threshhold = (W*maxHistSTE1+maxHistSTE2)/(W+1)
    return threshhold


# HistSTE, index_STE = np.histogram(ste, round(len(ste)))
# max2 = 0
# max2Index = 0
# max1 = HistSTE[0]
# max1Index = 0
# for i in range(0, len(HistSTE)):
#     if HistSTE[i] > max1:
#         max2 = max1
#         max2Index = max1Index
#         max1 = HistSTE[i]
#         max1Index = i
#     if HistSTE[i] < max1 and HistSTE[i] > max2:
#         max2 = HistSTE[i]
#         max2Index = i

# max1 = index_STE[max1Index]
# max2 = index_STE[max2Index]
# W = 5
# NguongChung = (W*max1+max2)/(W+1)
# print(NguongChung)
