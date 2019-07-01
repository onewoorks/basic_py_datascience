import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(0,10)
y = x ^ 2

plt.title("Graph Drawing")
plt.xlabel("Time")
plt.ylabel("Distance")

#line color
plt.plot(x,y,'r')
#line type
plt.plot(x,y,'x')
plt.show()