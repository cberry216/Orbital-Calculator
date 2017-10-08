from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

from satellite import *

class OrbitPlotter:
	"""Class the represent a 3D orbit plotter"""

	def __init__(self, satellite):
		"""__init__: constructor for ThreeDimOrbitPlotter
		:param satellite: satellite's orbit that will be plotted"""
		self.satellite = satellite
		self.fig = plt.figure(1)
		self.ax_3d = self.fig.add_subplot(221, projection="3d", aspect=.8)
		self.ax_2d_xy = self.fig.add_subplot(222, aspect=1)
		self.ax_2d_xz = self.fig.add_subplot(224, aspect=1)

		self.ax_2d_xz.set_xlim([self.satellite.planet.radius * -1.5,
		                        self.satellite.planet.radius * 1.5])
		self.ax_2d_xz.set_ylim([self.satellite.planet.radius * -1.5,
		                        self.satellite.planet.radius * 1.5])

		self.plot_all_3d()
		self.plot_all_2d()

	def get_orbit_xyz(self):
		"""get_orbit_xyz: returns a triple of the x, y, and z coordinates
		along an orbits plot with steps of 1 degree
		:return: Array, Array, Array"""
		radius_vectors = []

		for i in range(0, 360):
			radius_vectors.append(self.satellite.get_radius_vector_at_angle(i))

		return list(map(lambda x: x.i, radius_vectors)), list(map(lambda x:
		                                                          x.j,
		                                                          radius_vectors)), list(map(lambda x: x.k, radius_vectors))


	def plot_planet_3d(self, alpha=0.25, color='green'):
		"""plot_planet: plots a sphere with a radius equal to the planets
		radius
		:return: None
		"""
		u = np.linspace(0, 2 * np.pi, 100)
		v = np.linspace(0, np.pi, 100)

		x = self.satellite.planet.radius * np.outer(np.cos(u), np.sin(v))
		y = self.satellite.planet.radius * np.outer(np.sin(u), np.sin(v))
		z = self.satellite.planet.radius * np.outer(np.ones(np.size(u)), np.cos(v))

		self.ax_3d.plot_surface(x, y, z, alpha=alpha, color=color)

	def plot_planet_2d(self, alpha=0.25, color="green"):
		"""plot_planet_2d: plots the circular planet on a given 2d subplot
		:return: None"""
		planet_xy = plt.Circle((0, 0), self.satellite.planet.radius,
		                       alpha=alpha, color=color)
		planet_xz = plt.Circle((0, 0), self.satellite.planet.radius,
		                       alpha=alpha, color=color)
		self.ax_2d_xy.add_artist(planet_xy)
		self.ax_2d_xz.add_artist(planet_xz)


	def plot_orbit_3d(self, color="blue"):
		"""plot_orbit: plots the satellite orbit as a 3D ellipse
		:return: None"""
		x, y, z = self.get_orbit_xyz()

		self.ax_3d.plot_wireframe(x, y, z, color=color)

	def plot_orbit_2d(self):
		"""plot_orbit_2d_xy: plot the orbit of the planet with steps of 1
		degree
		:return: None"""
		x, y, z = self.get_orbit_xyz()

		self.ax_2d_xy.plot(x, y)
		self.ax_2d_xz.plot(x, z)

	def plot_current_pos_3d(self):
		"""plot_current_pos: plots a line from the center of the planet to
		the satellite's current positon"""
		self.ax_3d.plot([0, self.satellite.radius.i], [0, self.satellite.radius.j],
		                [0, self.satellite.radius.k],
		        color="red")

	def plot_current_pos_2d(self):
		self.ax_2d_xy.plot([0, self.satellite.radius.i], [0,
		                                                  self.satellite.radius.j])
		self.ax_2d_xz.plot([0, self.satellite.radius.i], [0,
			                                              self.satellite.radius.k])

	def plot_all_3d(self):
		"""plot_all_3d: plots the planet, orbit, and current position in
		three dimensions"""
		self.plot_planet_3d()
		self.plot_orbit_3d()
		self.plot_current_pos_3d()

	def plot_all_2d(self):
		"""plot_all_2d: plots the planet, orbit, and current position in 2
		dimensions"""
		self.plot_planet_2d()
		self.plot_orbit_2d()
		self.plot_current_pos_2d()




"""
orbit1 = OrbitPlotter(Satellite(Vector(7e6,0,0), Vector(0,7793.526006824358,0)))
orbit2 = OrbitPlotter(Satellite(Vector(7e6 * math.cos(degrees_to_radians(30)), 0,
                        7e6 * math.sin(degrees_to_radians(30))), Vector(0,
		                                                         7793.526006824358, 0)))
		                                                         
orbit3 = OrbitPlotter(Satellite(Vector(5526561.204884966, 
2975753.1382319974, 3190761.599333277), Vector(-2674.140099825787, 
7108.970352105472, -1543.9155064851902)))
"""