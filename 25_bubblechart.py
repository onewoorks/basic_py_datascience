import matplotlib.pyplot as plt 
import numpy as np 

x = np.random.rand(40)
y = np.random.rand(40)
z = np.random.rand(40)
colors = np.random.rand(40)

plt.scatter(x,y, s=z*1000, c=colors)
plt.show()
