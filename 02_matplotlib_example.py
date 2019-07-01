import numpy as np 
import matplotlib.pyplot as plt

#compute the x and y coordinates for points on a sine curve
x = np.arange(0,3 * np.pi, 0.1)
y = np.sin(x)
plt.title("since wave form")

#plot the points using matplotlib
plt.plot(x,y)
plt.show()