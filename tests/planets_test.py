import unittest
from planet import *


class PlanetsTest(unittest.TestCase):
    """ Test Class for planet.py"""

    def test_planets(self):
        # Sun
        self.assertEqual(Sun.mu, 1.32712e20)
        self.assertEqual(Sun.radius, 6.957e8)
        self.assertEqual(Sun.r_soi, 0)
        self.assertEqual(Sun.vel_esc, 617600)

        # Mercury
        self.assertEqual(Mercury.mu, 2.2032e13)
        self.assertEqual(Mercury.radius, 2.4397e6)
        self.assertEqual(Mercury.r_soi, 1.117e8)
        self.assertEqual(Mercury.vel_esc, 4217)

        # Venus
        self.assertEqual(Venus.mu, 3.2486e14)
        self.assertEqual(Venus.radius, 6.0518e6)
        self.assertEqual(Venus.r_soi, 6.163e8)
        self.assertEqual(Venus.vel_esc, 10360)

        # Earth
        self.assertEqual(Earth.mu, 3.986e14)
        self.assertEqual(Earth.radius, 6.378137e6)
        self.assertEqual(Earth.r_soi, 9.245e8)
        self.assertEqual(Earth.vel_esc, 11180)

        # Mars
        self.assertEqual(Mars.mu, 4.2828e13)
        self.assertEqual(Mars.radius, 3.3962e6)
        self.assertEqual(Mars.r_soi, 5.178e8)
        self.assertEqual(Mars.vel_esc, 5032)

        # Jupiter
        self.assertEqual(Jupiter.mu, 1.26687e17)
        self.assertEqual(Jupiter.radius, 7.1492e7)
        self.assertEqual(Jupiter.r_soi, 4.82e10)
        self.assertEqual(Jupiter.vel_esc, 59568)

        # Saturn
        self.assertEqual(Saturn.mu, 3.7931e16)
        self.assertEqual(Saturn.radius, 6.0268e7)
        self.assertEqual(Saturn.r_soi, 5.46e10)
        self.assertEqual(Saturn.vel_esc, 35500)

        # Uranus
        self.assertEqual(Uranus.mu, 5.794e15)
        self.assertEqual(Uranus.radius, 2.5559e7)
        self.assertEqual(Uranus.r_soi, 5.18e10)
        self.assertEqual(Uranus.vel_esc, 21300)

        # Neptune
        self.assertEqual(Neptune.mu, 6.8351e15)
        self.assertEqual(Neptune.radius, 2.4764e7)
        self.assertEqual(Neptune.r_soi, 8.680e10)
        self.assertEqual(Neptune.vel_esc, 23500)

        # Pluto
        self.assertEqual(Pluto.mu, 8.7e11)
        self.assertEqual(Pluto.radius, 1.187e6)
        self.assertEqual(Pluto.r_soi, 3.291e10)
        self.assertEqual(Pluto.vel_esc, 1210)
