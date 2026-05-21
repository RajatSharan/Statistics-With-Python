import seaborn as sea
import matplotlib.pyplot as py
import numpy as nm

data = [10, 20, 30, 40, 50, 50, 50, 60,120]
sea.histplot(data,kde=True)

py.show()

df=sea.load_dataset('iris')
df.head()




