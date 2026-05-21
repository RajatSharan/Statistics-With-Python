import numpy as nm
import seaborn as sea
import matplotlib.pyplot as py

ln=nm.random.lognormal(3.,1.,100)
sea.histplot(ln,kde=True)

py.show()

sea.histplot(nm.log(ln),kde=True)
py.show()