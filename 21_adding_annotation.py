import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(0,10)
y = x ^ 2
z = x ^ 3
t = x ^ 4

#labeling axes and title
plt.title("Graph Drawing")
plt.xlabel("Time")
plt.ylabel("Distance")

plt.plot(x,y)

#annotate
plt.annotate(xy=[2,1], s="Second Entry")
plt.annotate(xy=[4,6], s="Third Entry")

plt.plot(x,z)
plt.plot(x,t)

#plot lagend
plt.legend(['Race 1','Race 2','Race 3'], loc=1)

plt.style.use('fast')
plt.plot(x,z)
plt.show()