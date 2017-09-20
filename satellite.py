"""satellite.py - module to house the class for a satellite for any
planet in the solar system"""

from planets import Planets
import math 

def degrees_to_radians(degrees):
	return degrees * math.pi / 180

class Satellite:
	"""Class to represent a satellite orbiting a particular planet"""

	def __init__(self, radius, velocity, inclination, true_anamoly=0,
				 planet=Planets.Earth):
		"""
		__init__: constructor for Satelliate object
		Parameters:
			radius: radius at which satellite orbits planet in m
			velocity: velocity at which satellite is travelling in m/s
			true_anamoly: position in orbit where satellite is
				is currently located in degrees (default is it 
				periapsis)
			inclination: inclation of satellite's orbit in degrees
			planet: planet which satellite is orbiting (default is
				planet Earth)
		"""
		self.radius = radius
		self.velocity = velocity
		self.true_anamoly = true_anamoly
		self.inclination = inclination
		self.planet = planet
		# Following members are calcluated using the get methods

	# def get_angular_momentum(self):
	# 	"""get_angular_momentum: returns the angular momentum of the orbit
	# 	:return: float"""
	# 	return self.radius * self.velocity * math.cos(self.elevation_angle)
	#
	# def get_specific_energy(self):
	# 	"""get_specigic_energy: returns the specific energy of the orbi
	# 	:return: float"""
	# 	return self.velocity ** 2 / 2 - self.planet.mu / self.radius
	#
	# def get_eccentricity(self):
	# 	"""get_eccentricity: returns the eccentricity of the orbit
	# 	:return: float"""
	# 	return math.sqrt(1 + (2 * self.get_specific_energy() *
	# 	                      self.get_angular_momentum() ** 2) /
	# 	                 self.planet.mu ** 2)
	#
	# def get_orbital_parameter(self):
	# 	"""get_orbital_parameter: returns the orbital parameter of the orbit
	# 	:return: float"""
	# 	return self.get_angular_momentum() ** 2 / self.planet.mu
	#
	# def get_semimajor_axis(self):
	# 	"""get_semimajor_axis: returns the semimajor axis of the orbit
	# 	:return: float"""
	# 	return self.get_orbital_parameter() / (1 - self.get_eccentricity()
	# 	                                       ** 2)
	#
	# def get_radius_periapsis(self):
	# 	"""get_radius_periapsis: returns the radius of the satellite at
	# 	periapsis
	# 	:return: float"""
	# 	return self.get_angular_momentum() ** 2 / (self.planet.mu * (1 +
	# 	                                                            self.get_eccentricity()))
	#
	# def get_radius_apoapsis(self):
	# 	"""get_radius_apoapsis: returns the radius of the satellite at the
	# 	apoapsis
	# 	:return: float"""
	# 	return self.get_semimajor_axis() * (1 + self.get_eccentricity())

	def get_specific_energy(self):
		"""get_specigic_energy: returns the specific energy of the orbi
		:return: float"""
		return (self.velocity ** 2 / 2) - (self.planet.mu / self.radius)

	def get_semimajor_axis(self):
		"""get_semimajor_axis: returns the semimajor axis of the orbit
		:return: float"""
		return (-1 * self.planet.mu) / (2 * self.get_specific_energy())
