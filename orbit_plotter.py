from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

from satellite import *

sat1 = Satellite(Vector(7e6, 0, 0), Vector(0, 0, -7793.526006824358))
print(sat1.get_inclination())

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


#Plotting Sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = sat1.planet.radius * np.outer(np.cos(u), np.sin(v))
y = sat1.planet.radius * np.outer(np.sin(u), np.sin(v))
z = sat1.planet.radius * np.outer(np.ones(np.size(u)), np.cos(v))


#Plotting Orbit
radius_vectors = []

for i in range(0, 360):
	radius_vectors.append(sat1.get_radius_vector_at_angle(i))

for i in radius_vectors:
	print(i)

ax.plot_surface(x, y, z, alpha=0.5, color="green")
ax.plot([0,sat1.radius.i], [0,sat1.radius.j], [0,sat1.radius.k], color="red")
ax.plot_wireframe(list(map(lambda x: x.i, radius_vectors)),
                  list(map(lambda x: x.j, radius_vectors)),
                  list(map(lambda x: x.k, radius_vectors)))

plt.show()
