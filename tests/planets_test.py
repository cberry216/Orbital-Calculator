import unittest
import planets

class PlanetsTest(unittest.TestCase):
	""" Test Class for planets.py"""

	def test_planets(self):
		# Sun
		self.assertEqual(planets.Planets.Sun.mu, 1.32712e20)
		self.assertEqual(planets.Planets.Sun.radius, 6.957e8)
		self.assertEqual(planets.Planets.Sun.r_soi, 0)
		self.assertEqual(planets.Planets.Sun.vel_esc, 617600)

		# Mercury
		self.assertEqual(planets.Planets.Mercury.mu, 2.2032e13)
		self.assertEqual(planets.Planets.Mercury.radius, 2.4397e6)
		self.assertEqual(planets.Planets.Mercury.r_soi, 1.117e8)
		self.assertEqual(planets.Planets.Mercury.vel_esc, 4217)

		# Venus
		self.assertEqual(planets.Planets.Venus.mu, 3.2486e14)
		self.assertEqual(planets.Planets.Venus.radius, 6.0518e6)
		self.assertEqual(planets.Planets.Venus.r_soi, 6.163e8)
		self.assertEqual(planets.Planets.Venus.vel_esc, 10360)

		# Earth
		self.assertEqual(planets.Planets.Earth.mu, 3.986e14)
		self.assertEqual(planets.Planets.Earth.radius, 6.378137e6)
		self.assertEqual(planets.Planets.Earth.r_soi, 9.245e8)
		self.assertEqual(planets.Planets.Earth.vel_esc, 11180)

		# Mars
		self.assertEqual(planets.Planets.Mars.mu, 4.2828e13)
		self.assertEqual(planets.Planets.Mars.radius, 3.3962e6)
		self.assertEqual(planets.Planets.Mars.r_soi, 5.178e8)
		self.assertEqual(planets.Planets.Mars.vel_esc, 5032)

		# Jupiter
		self.assertEqual(planets.Planets.Jupiter.mu, 1.26687e17)
		self.assertEqual(planets.Planets.Jupiter.radius, 7.1492e7)
		self.assertEqual(planets.Planets.Jupiter.r_soi, 4.82e10)
		self.assertEqual(planets.Planets.Jupiter.vel_esc, 59568)

		# Saturn
		self.assertEqual(planets.Planets.Saturn.mu, 3.7931e16)
		self.assertEqual(planets.Planets.Saturn.radius, 6.0268e7)
		self.assertEqual(planets.Planets.Saturn.r_soi, 5.46e10)
		self.assertEqual(planets.Planets.Saturn.vel_esc, 35500)

		# Uranus
		self.assertEqual(planets.Planets.Uranus.mu, 5.794e15)
		self.assertEqual(planets.Planets.Uranus.radius, 2.5559e7)
		self.assertEqual(planets.Planets.Uranus.r_soi, 5.18e10)
		self.assertEqual(planets.Planets.Uranus.vel_esc, 21300)

		# Neptune
		self.assertEqual(planets.Planets.Neptune.mu, 6.8351e15)
		self.assertEqual(planets.Planets.Neptune.radius, 2.4764e7)
		self.assertEqual(planets.Planets.Neptune.r_soi, 8.680e10)
		self.assertEqual(planets.Planets.Neptune.vel_esc, 23500)

		# Pluto
		self.assertEqual(planets.Planets.Pluto.mu, 8.7e11)
		self.assertEqual(planets.Planets.Pluto.radius, 1.187e6)
		self.assertEqual(planets.Planets.Pluto.r_soi, 3.291e10)
		self.assertEqual(planets.Planets.Pluto.vel_esc, 1210)