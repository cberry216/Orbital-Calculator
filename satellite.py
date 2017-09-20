"""satellite.py - module to house the class for a satellite using vectors
and satellites using single units for any planet in the solar system"""

from planets import Planets
from vector import Vector
import math 

def degrees_to_radians(degrees):
	"""degrees_to_radians: returns the number of radians in the given
	degrees
	:param degrees: degrees to convert
	:return: float"""
	return degrees * math.pi / 180

def radians_to_degees(radians):
	"""radians_to_degrees: returns the number of degrees in the given
	radians
	:param radians: radians to convert
	:return: float"""
	return radians * 180 / math.pi

class Satellite_Vector:
	"""Class to represent a satellite orbiting a particular planet using
	vectors"""

	def __init__(self, radius, velocity, planet=Planets.Earth):
		"""__init__: constructor for Satellite_Vector object
		Parameters:
			radius: radius vector at which satellite orbits planet in m
			velocity: velocity vector at which satellite is travelling in m/s
			planet: planet which satellite is orbiting (default is
				planet Earth)
		"""
		self.radius = radius
		self.velocity = velocity
		self.planet = planet

	def get_angular_momentum_vector(self):
		"""get_angular_momentum_vector: returns the vector of the specific
		angular momentum of the orbit
		:return: Vector"""
		return self.radius.cross_product(self.velocity)

	def get_angular_momentum(self):
		"""get_angular_momentum: returns the angular momentum of the orbit
		in m^2 / s
		:return: float"""
		return self.get_angular_momentum_vector().magnitude()

	def get_specific_energy(self):
		"""get_specigic_energy: returns the specific energy of the orbi
	 	:return: float"""
		return self.velocity.magnitude() ** 2 / 2 - self.planet.mu / \
		                                            self.radius.magnitude()

	def get_eccentricity(self):
		"""get_eccentricity: returns the eccentricity of the orbit
	 	:return: float"""
		return math.sqrt(1 + (2 * self.get_specific_energy() *
		                      self.get_angular_momentum() ** 2) /
		                 self.planet.mu ** 2)

	def get_orbital_parameter(self):
		"""get_orbital_parameter: returns the orbital parameter of the orbit
	 	:return: float"""
		return self.get_angular_momentum() ** 2 / self.planet.mu

	def get_semimajor_axis(self):
		"""get_semimajor_axis: returns the semimajor axis of the orbit
	 	:return: float"""
		return self.get_orbital_parameter() / (1 - self.get_eccentricity()
		                                       ** 2)

	def get_radius_periapsis(self):
		"""get_radius_periapsis: returns the radius of the satellite at
	 	periapsis
	 	:return: float"""
		return self.get_angular_momentum() ** 2 / (self.planet.mu * (1 +
		                                                             self.get_eccentricity()))

	def get_radius_apoapsis(self):
		"""get_radius_apoapsis: returns the radius of the satellite at the
	 	apoapsis
	 	:return: float"""
		return self.get_semimajor_axis() * (1 + self.get_eccentricity())

	def get_inclination(self):
		"""get_inclination: returns tha angle of inclination of the orbit in degrees
		:return: float"""
		return radians_to_degees(math.acos(Vector(0,0,1).dot_product(
			self.get_angular_momentum_vector())/self.get_angular_momentum()))

	def get_true_anomaly(self):
		"""get_true_anomaly: returns the position of the satellite along its orbit in degrees
		:return: float"""
		return radians_to_degees(math.acos((1/self.get_eccentricity()) * (
			self.get_orbital_parameter() / self.radius.magnitude() - 1)))

	def get_elevation_angle(self):
		"""get_elevation_angle: return the elevation angle of the satellite
		(i.e. the angle between the velocity vector and the local horizontal plane in degrees
		:return: float"""
		return radians_to_degees(math.acos(self.get_angular_momentum() /
		                                   (self.radius.magnitude() *
		                                    self.velocity.magnitude())))


	# def get_angular_momentum(self):
	# 	"""get_angular_momentum: returns the vector that is the specific
	# 	angular momentum of the orbit
	# 	:return: vector"""
	# 	return self.radius.cross_product(self.velocity)
	#
	# def get_angular_momentum_magnitude(self):
	# 	"""get_angular_momentum_magnitude: returns the magnitude of the
	# 	angular momentum vector in m^2 / s
	# 	:return: float"""
	# 	return self.get_angular_momentum().magnitude()
	#
	# def get_inclination(self):
	# 	"""get_inclination: returns the inclination of the orbit in degrees
	# 	:return: float"""
	# 	return math.acos(Vector(0,0,1).dot_product(
	# 		self.get_angular_momentum()) / self.get_angular_momentum_magnitude())
	#
	# def get_line_of_nodes(self):
	# 	"""get_line_of_nodes: returns the line of nodes vectors
	# 	:return: vector"""
	# 	return Vector(0,0,1).cross_product(self.get_angular_momentum())
	#
	# def get_line_of_nodes_magnitude(self):
	# 	"""get_line_of_nodes_magnitude: returns the magnitude of the line of nodes in m
	# 	:return: float"""
	# 	return self.get_line_of_nodes().magnitude()
	#
	# def get_longitude_of_ascending_node(self):
	# 	"""get_longitude_of_ascending_node: returns the angle at which the
	# 	ascending node occurs in degrees
	# 	:return: float"""
	# 	line_of_nodes = self.get_line_of_nodes()
	# 	if line_of_nodes.j
