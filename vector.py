"""vector.py - module to store the vector class"""

import math

class Vector:
	"""Class to represent a 3-Dimensional vector"""

	def __init__(self, i, j, k):
		"""__init__: constructor for Vector class
		:param i: the x-value for the vector
		:param j: the y-value for the vector
		:param k: the z-value for the vector"""
		self.i = i
		self.j = j
		self.k = k

	def magnitude(self):
		"""magnitude: returns the magnitude of the vector
		:return: float"""
		return math.sqrt(self.i ** 2 + self.j ** 2 + self.k ** 2)

	def dot_product(self, other_vector):
		"""dot_product: returns the dot product of the two vectors
		:param other_vector: vector to be dot producted (self.vector (dot)
		other_vector)
		:return: float"""
		return self.i * other_vector.i + self.j * other_vector.j + self.k * \
		                                                           other_vector.k

	def cross_product(self, other_vector):
		"""cross_product: returns the cross product of the two vectors
		:param other_vector: other vector to be cross producted (self.vector X other_vector)
		:return: vector"""
		return Vector(self.j * other_vector.k - self.k * other_vector.j,
		              self.k * other_vector.i - self.i * other_vector.k,
		              self.i * other_vector.j - self.j * other_vector.i)

	def __str__(self):
		return str(self.i) + 'i + ' + str(self.j) + 'j + ' + str(self.k) + 'k'

	def __eq__(self, other):
		return self.i == other.i and self.j == other.j and self.k == other.k

	def __div__(self, other):
		return Vector(self.i / other, self.j / other, self.k/ other)

	def __sub__(self, other):
		return Vector(self.i - other.i, self.j - other.j, self.k - other.k)



