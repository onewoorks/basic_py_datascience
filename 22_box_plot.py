import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df= pd.DataFrame(np.random.randn(10,5), columns = ['A','B','C','D','E'])
df.plot.box(grid='True')

plt.boxplot(df)
plt.show()