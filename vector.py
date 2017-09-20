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
		:return"""


