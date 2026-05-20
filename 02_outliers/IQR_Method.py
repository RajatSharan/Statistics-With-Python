import numpy as np
import seaborn as sea
import matplotlib.pyplot as plt

dataset=[11,10,12,14,12,15,14,13,15,102,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]

#IQR
#1 Sort the data
#2 calculation Q1(25%) and Q3(75%)
#3 IQR(Q3-Q1)
#4 Find the Lower Fence(Q1-1.5(iqr))
#5 Find the Upper Fence(Q3+1.5(iqr))


dataset=sorted(dataset)
Q1,Q3=np.percentile(dataset,[25,75])
iqr=Q3-Q1
lower_fence=Q1-1.5*iqr
upper_fence=Q3+1.5*iqr
outliers =[]

for value in dataset:
    if value<lower_fence or value>upper_fence:
        outliers.append(value)
        
print("outliers:",outliers)
sea.boxplot(x=dataset)
plt.show()



