""" planets.py - module to house the planet class along with each
planet in the Sol system
"""

big_G = 6.67408e-11 #in m^3/(kg s^2)

class Planet:
	"""Class to represent a planet orbiting the Sun """
	
	def __init__(self, mu, radius, r_soi, vel_esc):
		"""
		__init__: constructor for Planet object
		Parameters:
			mu: the gravitational parameter of planet in m^3/s^2
			radius: radius of planet in kilometer (this is the distance
					from center of planet to crust)
			r_soi: radius of the sphere of influence of planet
			vel_esc: escape velocity from surface of the planet in m/s
		"""
		self.mu = mu
		self.radius = radius
		self.r_soi = r_soi
		self.vel_esc = vel_esc

###################################################################
#			    			Planet Object                         #
###################################################################
class Planets():
	""" Data comes from NASA fact sheet online and personal forumla sheet"""
	Sun 	= Planet(1.32712e20, 6.957e8, 0, 617600)
	Mercury = Planet(2.2032e13, 2.4397e6, 1.117e8, 4217)
	Venus	= Planet(3.2486e14, 6.0518e6, 6.163e8, 10360)
	Earth	= Planet(3.986e14, 6.378137e6, 9.245e8, 11180)
	Mars	= Planet(4.2828e13, 3.3962e6, 5.178e8, 5032)
	Jupiter = Planet(1.26687e17, 7.1492e7, 4.820e10, 59568)
	Saturn  = Planet(3.7931e16, 6.0268e7, 5.460e10, 35500)
	Uranus	= Planet(5.794e15, 2.5559e7, 5.180e10, 21300)
	Neptune = Planet(6.8351e15, 2.4764e7, 8.680e10, 23500)
	Pluto	= Planet(8.700e11, 1.187e6, 3.291e10, 1210)