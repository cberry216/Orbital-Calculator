import unittest
import planet
from satellite import *


class SatelliteTest(unittest.TestCase):
	""" Test Class for satellite.py"""

	def setUp(self):
		self.sat1 = Satellite(Vector(7e6, 0, 0), Vector(0, 7793.526006824358, 0))
		self.sat2 = Satellite(Vector(-5.e5, 7483314.773547883, 0), Vector(
			-7290.176038112294, 0, 0))
		self.sat3 = Satellite(Vector(-3862068.9655172424, 6689299.670610837,
		                             0), Vector(-6327.554537779295,
		                                        -3166.119940272407, 0))

		#Different Orbital Trajectory
		self.sat4 = Satellite(Vector(6062177.826491071, 0,
		                             3499999.9999999995), Vector(0,
		                                                         7793.526006824358, 0))

	def test_degrees_to_radians(self):
		self.assertEqual(degrees_to_radians(0), 0)
		self.assertEqual(degrees_to_radians(90), math.pi / 2)
		self.assertEqual(degrees_to_radians(180), math.pi)
		self.assertEqual(degrees_to_radians(270), 3 * math.pi / 2)
		self.assertEqual(degrees_to_radians(360), 2 * math.pi)

	def test_radians_to_degrees(self):
		self.assertEqual(radians_to_degrees(0), 0)
		self.assertEqual(radians_to_degrees(math.pi / 2), 90)
		self.assertEqual(radians_to_degrees(math.pi), 180)
		self.assertEqual(radians_to_degrees(3 * math.pi / 2), 270)
		self.assertEqual(radians_to_degrees(2 * math.pi), 360)

	def test_init(self):
		self.assertEqual(self.sat1.radius, Vector(7e6,0,0))
		self.assertEqual(self.sat1.velocity, Vector(0,7793.526006824358,0))
		self.assertEqual(self.sat1.planet, planet.Planets.Earth)

		self.assertEqual(self.sat2.radius, Vector(-5e5, 7483314.773547883, 0))
		self.assertEqual(self.sat2.velocity, Vector(
			-7290.176038112294, 0, 0))
		self.assertEqual(self.sat2.planet, planet.Planets.Earth)

		self.assertEqual(self.sat3.radius, Vector(-3862068.9655172424,
		                                          6689299.670610837, 0))
		self.assertEqual(self.sat3.velocity, Vector(-6327.554537779295,
		                                        -3166.119940272407, 0))
		self.assertEqual(self.sat3.planet, planet.Planets.Earth)

		self.assertEqual(self.sat4.radius, Vector(6062177.826491071, 0,
		                                        3499999.9999999995))
		self.assertEqual(self.sat4.velocity, Vector(0, 7793.526006824358, 0))
		self.assertEqual(self.sat4.planet, planet.Planets.Earth)

	def test_get_angular_momentum_vector(self):
		self.assertEqual(self.sat1.get_angular_momentum_vector(),
		                      Vector(0, 0, 54554682047.77051))
		self.assertEqual(self.sat2.get_angular_momentum_vector(),
		                      Vector(0, 0, 54554682047.77051))
		self.assertEqual(self.sat3.get_angular_momentum_vector(),
		                      Vector(0, 0, 54554682047.77051))
		self.assertEqual(self.sat4.get_angular_momentum_vector(),
		                      Vector(-27277341023.88525, 0, 47245740548.75212))

	def test_get_eccentricity_vector(self):
		self.assertAlmostEqual(self.sat1.get_eccentricity_vector(), Vector(
			1/15.0, 0, 0))
		self.assertAlmostEqual(self.sat2.get_eccentricity_vector(), Vector(
			1/15.0, 0, 0))
		self.assertAlmostEqual(self.sat3.get_eccentricity_vector(), Vector(
			1/15.0, 0, 0))
		self.assertAlmostEqual(self.sat4.get_eccentricity_vector(), Vector(
			0.057735026918962595, 0, 0.03333333333333338))

	def test_get_angular_momentum(self):
		self.assertEqual(self.sat1.get_angular_momentum(), 54554682047.77051)
		self.assertEqual(self.sat2.get_angular_momentum(), 54554682047.77051)
		self.assertEqual(self.sat3.get_angular_momentum(), 54554682047.77051)
		self.assertEqual(self.sat4.get_angular_momentum(), 54554682047.77051)

	def test_get_specific_energy(self):
		self.assertAlmostEqual(self.sat1.get_specific_energy(),
		                       -26573333.333333332)
		self.assertAlmostEqual(self.sat2.get_specific_energy(),
		                       -26573333.333333332)
		self.assertAlmostEqual(self.sat3.get_specific_energy(),
		                       -26573333.333333332)
		self.assertAlmostEqual(self.sat4.get_specific_energy(),
		                       -26573333.333333332)

	def test_get_eccentricity(self):
		self.assertAlmostEqual(self.sat1.get_eccentricity(), 1/15.0)
		self.assertAlmostEqual(self.sat2.get_eccentricity(), 1/15.0)
		self.assertAlmostEqual(self.sat3.get_eccentricity(), 1/15.0)
		self.assertAlmostEqual(self.sat4.get_eccentricity(), 1/15.0)

	def test_get_orbital_parameter(self):
		self.assertAlmostEqual(self.sat1.get_orbital_parameter(),
		                       7466666.666666667)
		self.assertAlmostEqual(self.sat2.get_orbital_parameter(),
		                       7466666.666666667)
		self.assertAlmostEqual(self.sat3.get_orbital_parameter(),
		                       7466666.666666667)
		self.assertAlmostEqual(self.sat4.get_orbital_parameter(),
		                       7466666.666666667)

	def test_get_semimajor_axis(self):
		self.assertAlmostEqual(self.sat1.get_semimajor_axis(), 7.5e6)
		self.assertAlmostEqual(self.sat2.get_semimajor_axis(), 7.5e6)
		self.assertAlmostEqual(self.sat3.get_semimajor_axis(), 7.5e6)
		self.assertAlmostEqual(self.sat4.get_semimajor_axis(), 7.5e6)

	def test_get_radius_periapsis(self):
		self.assertAlmostEqual(self.sat1.get_radius_periapsis(), 7e6)
		self.assertAlmostEqual(self.sat2.get_radius_periapsis(), 7e6)
		self.assertAlmostEqual(self.sat3.get_radius_periapsis(), 7e6)
		self.assertAlmostEqual(self.sat4.get_radius_periapsis(), 7e6)

	def test_get_radius_apoapsis(self):
		self.assertAlmostEqual(self.sat1.get_radius_apoapsis(), 8e6)
		self.assertAlmostEqual(self.sat2.get_radius_apoapsis(), 8e6)
		self.assertAlmostEqual(self.sat3.get_radius_apoapsis(), 8e6)
		self.assertAlmostEqual(self.sat4.get_radius_apoapsis(), 8e6)

	def test_get_inclination(self):
		self.assertEqual(self.sat1.get_inclination(), 0)
		self.assertEqual(self.sat2.get_inclination(), 0)
		self.assertEqual(self.sat3.get_inclination(), 0)
		self.assertAlmostEqual(self.sat4.get_inclination(), 30)

	def test_get_true_anamoly(self):
		self.assertEqual(self.sat1.get_true_anomaly(), 0)
		self.assertAlmostEqual(self.sat2.get_true_anomaly(), 93.82255372927428)
		self.assertAlmostEqual(self.sat3.get_true_anomaly(), 120.0)
		self.assertAlmostEqual(self.sat4.get_true_anomaly(), 0)

	def test_get_elevation_angle(self):
		self.assertEqual(self.sat1.get_elevation_angle(), 0)
		self.assertAlmostEqual(self.sat2.get_elevation_angle(),
		                       3.8225537292743184)
		self.assertAlmostEqual(self.sat3.get_elevation_angle(),
		                       3.4179810919120652)
		self.assertAlmostEqual(self.sat4.get_elevation_angle(), 0)

	def test_get_nodes_vector(self):
		self.assertAlmostEqual(self.sat1.get_nodes_vector(), Vector(0, 0, 0))
		self.assertAlmostEqual(self.sat2.get_nodes_vector(), Vector(0, 0, 0))
		self.assertAlmostEqual(self.sat3.get_nodes_vector(), Vector(0, 0, 0))
		self.assertAlmostEqual(self.sat4.get_nodes_vector(), Vector(0,
		                                                            -27277341023.88525, 0))

	def test_get_longitude_of_ascending_node(self):
		self.assertAlmostEqual(self.sat1.get_longitude_of_ascending_node(), 0)
		self.assertAlmostEqual(self.sat1.get_longitude_of_ascending_node(), 0)
		self.assertAlmostEqual(self.sat1.get_longitude_of_ascending_node(), 0)
		self.assertAlmostEqual(self.sat4.get_longitude_of_ascending_node(), 270)

	def test_get_radius_at_angle(self):
		self.assertAlmostEqual(self.sat1.get_radius_at_angle(0), 7e6)
		self.assertAlmostEqual(self.sat1.get_radius_at_angle(
			93.82255372927428), 7.5e6)
		self.assertAlmostEqual(self.sat1.get_radius_at_angle(120), 7724137.931034484)
		self.assertAlmostEqual(self.sat1.get_radius_at_angle(180), 8e6)

		self.assertAlmostEqual(self.sat4.get_radius_at_angle(0), 7e6)
		self.assertAlmostEqual(self.sat4.get_radius_at_angle(
			93.82255372927428), 7.5e6)
		self.assertAlmostEqual(self.sat4.get_radius_at_angle(120), 7724137.931034484)
		self.assertAlmostEqual(self.sat4.get_radius_at_angle(180), 8e6)

	def test_get_radius_vector_at_angle(self):
		self.assertAlmostEqual(self.sat1.get_radius_vector_at_angle(0), Vector(
			7e6,0,0))
		self.assertAlmostEqual(self.sat1.get_radius_vector_at_angle(
			93.82255372927428), Vector(-5e5,7483314.773547883,0))
		self.assertAlmostEqual(self.sat1.get_radius_vector_at_angle(120),
		                       Vector(-3862068.9655172424,
		                              6689299.670610837, 0))
		self.assertAlmostEqual(self.sat1.get_radius_vector_at_angle(180),
		                       Vector(-8e6,0,0))

		self.assertAlmostEqual(self.sat4.get_radius_vector_at_angle(0),
		                       Vector(6062177.826491071, 0,
		                              3499999.9999999995))
		self.assertAlmostEqual(self.sat4.get_radius_vector_at_angle(90),
		                       Vector(0, 7466666.666666667, 0))
		self.assertAlmostEqual(self.sat4.get_radius_vector_at_angle(180),
		                       Vector(-6928203.23027551, 0, -3999999.9999999995))
		self.assertAlmostEqual(self.sat4.get_radius_vector_at_angle(270),
		                       Vector(0, -7466666.666666667, 0))


	def test_get_elevation_angle_at_angle(self):
		self.assertAlmostEqual(self.sat1.get_elevation_angle_at_angle(0), 0)
		self.assertAlmostEqual(self.sat1.get_elevation_angle_at_angle(
			93.82255372927428), 3.8225537292743184)
		self.assertAlmostEqual(self.sat1.get_elevation_angle_at_angle(120),
		                       3.4179810919120652)
		self.assertAlmostEqual(self.sat1.get_elevation_angle_at_angle(180), 0)

		self.assertAlmostEqual(self.sat4.get_elevation_angle_at_angle(0), 0)
		self.assertAlmostEqual(self.sat4.get_elevation_angle_at_angle(
			93.82255372927428), 3.8225537292743184)
		self.assertAlmostEqual(self.sat4.get_elevation_angle_at_angle(120),
		                       3.4179810919120652)
		self.assertAlmostEqual(self.sat4.get_elevation_angle_at_angle(180), 0)

	def test_get_parallel_angle_at_angle(self):
		self.assertAlmostEqual(self.sat1.get_parallel_angle_at_angle(0), 90)
		self.assertAlmostEqual(self.sat1.get_parallel_angle_at_angle(
			93.82255372927428), 0)
		self.assertAlmostEqual(self.sat1.get_parallel_angle_at_angle(120),
		                       -26.582018908087935)
		self.assertAlmostEqual(self.sat1.get_parallel_angle_at_angle(180), -90)

		self.assertAlmostEqual(self.sat4.get_parallel_angle_at_angle(0), 90)
		self.assertAlmostEqual(self.sat4.get_parallel_angle_at_angle(
			93.82255372927428), 0)
		self.assertAlmostEqual(self.sat4.get_parallel_angle_at_angle(120),
		                       -26.582018908087935)
		self.assertAlmostEqual(self.sat4.get_parallel_angle_at_angle(180), -90)

	#def test_get_semiminor_radius(self):
	#	self.assertAlmostEqual(sat1.get_semiminor_radius(), 7.5e6)
	#	self.assertAlmostEqual(sat2.get_semiminor_radius(), 7.5e6)
	#	self.assertAlmostEqual(sat3.get_semiminor_radius(), 7.5e6)

	def test_get_velocity_at_angle(self):
		self.assertAlmostEqual(self.sat1.get_velocity_at_angle(0),
		                       7793.526006824358)
		self.assertAlmostEqual(self.sat1.get_velocity_at_angle(
			93.82255372927428), 7290.176038112294)
		self.assertAlmostEqual(self.sat1.get_velocity_at_angle(120),
		                       7075.469023659272)
		self.assertAlmostEqual(self.sat1.get_velocity_at_angle(180),
		                       6819.335255971313)

		self.assertAlmostEqual(self.sat4.get_velocity_at_angle(0),
		                       7793.526006824358)
		self.assertAlmostEqual(self.sat4.get_velocity_at_angle(
			93.82255372927428), 7290.176038112294)
		self.assertAlmostEqual(self.sat4.get_velocity_at_angle(120),
		                       7075.469023659272)
		self.assertAlmostEqual(self.sat4.get_velocity_at_angle(180),
		                       6819.335255971313)

	def test_get_velocity_vector_at_angle(self):
		self.assertAlmostEqual(self.sat1.get_velocity_vector_at_angle(0),
		                       Vector(
			0, 7793.526006824358, 0))
		self.assertAlmostEqual(self.sat1.get_velocity_vector_at_angle(
			93.82255372927428), Vector(-7290.176038112294, 0, 0))
		self.assertAlmostEqual(self.sat1.get_velocity_vector_at_angle(120),
		                       Vector(-6327.554537779295,-3166.119940272407, 0))
		self.assertAlmostEqual(self.sat1.get_velocity_vector_at_angle(180),
		                       Vector(0, -6819.335255971313, 0))

		self.assertAlmostEqual(self.sat4.get_velocity_vector_at_angle(0),
		                       Vector(0, 7793.526006824358, 0))
		self.assertAlmostEqual(self.sat4.get_velocity_vector_at_angle(180),
		                       Vector(0, -6819.335255971313, 0))
		self.assertAlmostEqual(self.sat4.get_velocity_vector_at_angle(
			93.82255372927428).j, 0)
		self.assertAlmostEqual(self.sat4.get_velocity_vector_at_angle(
			93.82255372927428).magnitude(), self.sat4.get_velocity_at_angle(93.82255372927428))