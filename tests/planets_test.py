import unittest
import planet


class PlanetsTest(unittest.TestCase):
	""" Test Class for planet.py"""

	def test_planets(self):
		# Sun
		self.assertEqual(planet.Planets.Sun.mu, 1.32712e20)
		self.assertEqual(planet.Planets.Sun.radius, 6.957e8)
		self.assertEqual(planet.Planets.Sun.r_soi, 0)
		self.assertEqual(planet.Planets.Sun.vel_esc, 617600)

		# Mercury
		self.assertEqual(planet.Planets.Mercury.mu, 2.2032e13)
		self.assertEqual(planet.Planets.Mercury.radius, 2.4397e6)
		self.assertEqual(planet.Planets.Mercury.r_soi, 1.117e8)
		self.assertEqual(planet.Planets.Mercury.vel_esc, 4217)

		# Venus
		self.assertEqual(planet.Planets.Venus.mu, 3.2486e14)
		self.assertEqual(planet.Planets.Venus.radius, 6.0518e6)
		self.assertEqual(planet.Planets.Venus.r_soi, 6.163e8)
		self.assertEqual(planet.Planets.Venus.vel_esc, 10360)

		# Earth
		self.assertEqual(planet.Planets.Earth.mu, 3.986e14)
		self.assertEqual(planet.Planets.Earth.radius, 6.378137e6)
		self.assertEqual(planet.Planets.Earth.r_soi, 9.245e8)
		self.assertEqual(planet.Planets.Earth.vel_esc, 11180)

		# Mars
		self.assertEqual(planet.Planets.Mars.mu, 4.2828e13)
		self.assertEqual(planet.Planets.Mars.radius, 3.3962e6)
		self.assertEqual(planet.Planets.Mars.r_soi, 5.178e8)
		self.assertEqual(planet.Planets.Mars.vel_esc, 5032)

		# Jupiter
		self.assertEqual(planet.Planets.Jupiter.mu, 1.26687e17)
		self.assertEqual(planet.Planets.Jupiter.radius, 7.1492e7)
		self.assertEqual(planet.Planets.Jupiter.r_soi, 4.82e10)
		self.assertEqual(planet.Planets.Jupiter.vel_esc, 59568)

		# Saturn
		self.assertEqual(planet.Planets.Saturn.mu, 3.7931e16)
		self.assertEqual(planet.Planets.Saturn.radius, 6.0268e7)
		self.assertEqual(planet.Planets.Saturn.r_soi, 5.46e10)
		self.assertEqual(planet.Planets.Saturn.vel_esc, 35500)

		# Uranus
		self.assertEqual(planet.Planets.Uranus.mu, 5.794e15)
		self.assertEqual(planet.Planets.Uranus.radius, 2.5559e7)
		self.assertEqual(planet.Planets.Uranus.r_soi, 5.18e10)
		self.assertEqual(planet.Planets.Uranus.vel_esc, 21300)

		# Neptune
		self.assertEqual(planet.Planets.Neptune.mu, 6.8351e15)
		self.assertEqual(planet.Planets.Neptune.radius, 2.4764e7)
		self.assertEqual(planet.Planets.Neptune.r_soi, 8.680e10)
		self.assertEqual(planet.Planets.Neptune.vel_esc, 23500)

		# Pluto
		self.assertEqual(planet.Planets.Pluto.mu, 8.7e11)
		self.assertEqual(planet.Planets.Pluto.radius, 1.187e6)
		self.assertEqual(planet.Planets.Pluto.r_soi, 3.291e10)
		self.assertEqual(planet.Planets.Pluto.vel_esc, 1210)