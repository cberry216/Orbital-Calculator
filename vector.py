"""vector.py - module to store the vector class"""

import math
from decimal import Decimal


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
        return '%.4E i + %.4E j + %.4Ek ' % (Decimal(self.i), Decimal(
            self.j), Decimal(self.k))

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j and self.k == other.k

    def __truediv__(self, other):
        # if type(other) != type(int()) or type(other) != type(float):
        #	raise TypeError("Cannot divide vector by non-numeric value")
        return Vector(self.i / other, self.j / other, self.k / other)

    def __mul__(self, other):
        return Vector(self.i * other, self.j * other, self.k * other)

    def __rmul__(self, other):
        return Vector(self.i * other, self.j * other, self.k * other)

    def __sub__(self, other):
        return Vector(self.i - other.i, self.j - other.j, self.k - other.k)

    def __round__(self, n=7):
        return Vector(round(self.i, n), round(self.j, n), round(self.k, n))

    def __abs__(self):
        return self.magnitude()

    def __add__(self, delta_v):
        return Vector(self.i + delta_v.i, self.j + delta_v.j, self.k + delta_v.k)
