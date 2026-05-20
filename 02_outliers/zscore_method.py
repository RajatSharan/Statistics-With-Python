import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea

dataset = [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]

plt.hist(dataset)

plt.show()

#ZScore
def detect_outliners(data):
    outliner=[]
    threshold=3
    mean = np.mean(data)
    std=np.std(data)
    for i in data:
        z_score=(i-mean)/std
        if np.abs(z_score)>threshold:
            outliner.append(i)
    return outliner

print(detect_outliners(dataset))

