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

def radians_to_degrees(radians):
	"""radians_to_degrees: returns the number of degrees in the given
	radians
	:param radians: radians to convert
	:return: float"""
	return radians * 180 / math.pi

class Satellite:
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

	def get_eccentricity_vector(self):
		"""get_eccentricity_vector: returns the vector of the eccentricity
		:return: Vector"""
		return (self.velocity.cross_product(
			self.get_angular_momentum_vector())\
		       / self.planet.mu) - (self.radius / self.radius.magnitude())

	def get_angular_momentum(self):
		"""get_angular_momentum: returns the angular momentum of the orbit
		in m^2 / s
		:return: float"""
		return self.get_angular_momentum_vector().magnitude()

	def get_specific_energy(self):
		"""get_specigic_energy: returns the specific energy of the orbi
	 	:return: float"""
		return (self.velocity.magnitude() ** 2 / 2) - (self.planet.mu / \
		                                            self.radius.magnitude())

	def get_eccentricity(self):
		"""get_eccentricity: returns the eccentricity of the orbit
	 	:return: float"""
		return math.sqrt(1 + ((2 * self.get_specific_energy() *
		                      self.get_angular_momentum() ** 2) /
		                 self.planet.mu ** 2))

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
		return radians_to_degrees(math.acos(Vector(0,0,1).dot_product(
			self.get_angular_momentum_vector())/self.get_angular_momentum()))

	def get_true_anomaly(self):
		"""get_true_anomaly: returns the position of the satellite along its orbit in degrees
		:return: float"""
		return radians_to_degrees(math.acos((1/self.get_eccentricity()) * (
			self.get_orbital_parameter() / self.radius.magnitude() - 1)))

	def get_elevation_angle(self):
		"""get_elevation_angle: return the elevation angle of the satellite
		(i.e. the angle between the velocity vector and the local horizontal plane in degrees
		:return: float"""
		return radians_to_degrees(math.acos(self.get_angular_momentum() /
		                                   (self.radius.magnitude() *
		                                    self.velocity.magnitude())))

	def get_elevation_angle_at_angle(self, anamoly):
		"""get_elevation_angle_at_angle: returns the elevation angle of
		the orbit at the specified angle, which is equal to arccos(h/rv).
		:param anamoly: angle at which the orbit is at in degrees
		:return: float"""
		#TODO

	def get_radius_vector_at_angle(self, anamoly):
		"""get_radius_vector_at_angle: returns the radius vector when the
		orbit is at the specified angle
		:param anamoly: angle at which the orbit is at in degrees
		:return: Vector"""
		#TODO

	def get_parallel_angle_at_angle(self, anamoly):
		"""get_parallel_angle_at_angle: returns the angle between the
		velocity vector and the and imaginary line going through the
		satellite and parallel to the eccentricty vector. This angle is
		equal to 180 - (true anamoly) - (zenith angle), the zenith angle
		being equal to 90 - (elevation angle)
		:param anamoly: the angle at which the orbit is at in degrees
		:return: float"""
		#TODO

	def get_velocity_vector_at_angle(self, anamoly):
		"""get_velocity_vector_at_angle: returns the velocity vector when
		the orbit is at the specified angle
		:param anamoly: angle at which the orbit is at in degrees
		:return: Vector"""
		#TODO


#TESTS
sat1 = Satellite(Vector(7e6,0,0), Vector(0,7793.52,0))
sat2 = Satellite(Vector(-5.00184e5, 7.483302e6, 0), Vector(
	-7290.169616546589, 0, 0))
