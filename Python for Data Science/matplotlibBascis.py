"""
Matplotlib : a library used to create graphs, charts, and figures. 

pyplot : the module used to create plots.
"""
import matplotlib.pyplot as plt
import pandas as pd

s=pd.Series([18,42,9,32,81,64,3])

s.plot(kind='bar')
# plot() :
# used to create a plot from the data in a Pandas Series or DataFrame.
plt.savefig('Python for Data Science/result_img/plt.png')
# X axis : index
# Y axis : data
