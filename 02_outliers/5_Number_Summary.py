import numpy as np

import matplotlib.pyplot as py

dataset=[11,10,12,14,12,15,14,13,15,102,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]

Q1,Q3=np.percentile(dataset,[25,75])

print(Q1,Q3)

py.show()