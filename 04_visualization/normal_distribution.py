#normal distribution

import numpy as nm
import seaborn as sea
import matplotlib.pyplot as py

s=nm.random.normal(0.5,0.2,100)
print(s)
sea.histplot(s,kde=True)
py.show()
