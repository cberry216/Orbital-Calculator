from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

true_anaomlies = np.linspace(0,359, 360)


ax.plot_wireframe(X, Y, Z)

plt.show()