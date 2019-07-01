from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt 

chart = plt.figure()
chart3d = chart.add_subplot(111, projection='3d')

X,Y,Z = axes3d.get_test_data(0.08)

chart3d.plot_wireframe(X,Y,Z, color='ryb', rstride=15, cstride=10)
plt.show()