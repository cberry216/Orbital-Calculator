import math
import unittest

from vector import Vector


class VectorTest(unittest.TestCase):
	""" Test Class for vector.py"""

	def setUp(self):
		self.v1 = Vector(1.0, 2.5, -3.4)
		self.v2 = Vector(-2.4, 3.6, 0.5)

	def test_magnitude(self):
		self.assertEqual(self.v1.magnitude(), math.sqrt(1 + 2.5**2 + 3.4**2))
		self.assertEqual(self.v2.magnitude(), math.sqrt(2.4**2 + 3.6**2 +
		                                                0.5**2))

	def test_dot_product(self):
		self.assertEqual(round(self.v1.dot_product(self.v2), 1), 4.9)
		self.assertEqual(round(self.v2.dot_product(self.v1), 1), 4.9)

	def test_cross_product(self):
		self.assertEqual(self.v1.cross_product(self.v2), Vector(13.49, 7.66,
		                                                        9.6))
		self.assertEqual(self.v2.cross_product(self.v1), Vector(-13.49,
		                                                        -7.66, -9.6))

	def test_equals(self):
		self.assertEqual(self.v1, Vector(1.0, 2.5, -3.4))
		self.assertEqual(self.v2, Vector(-2.4, 3.6, 0.5))

	def test_division(self):
		self.assertEqual(self.v1 / 2, Vector(.5, 1.25, -1.7))
		self.assertEqual(self.v2 / 2, Vector(-1.2, 1.8, 0.25))

	def test_multiplication(self):
		self.assertEqual(self.v1 * 2, Vector(2.0, 5.0, -6.8))
		self.assertEqual(self.v2 * 1.4, Vector(-3.36, 5.04, 0.7))

	def test_subtraction(self):
		self.assertEqual(self.v1 - self.v2, Vector(3.4, -1.1, -3.9))
		self.assertEqual(self.v2 - self.v1, Vector(-3.4, 1.1, 3.9))

	def test_absolute_value(self):
		self.assertEqual(self.v1.__abs__(), self.v1.magnitude())
		self.assertEqual(self.v2.__abs__(), self.v2.magnitude())