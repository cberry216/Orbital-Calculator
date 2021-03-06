"""satellite.py - module to house the class for a satellite using vectors
and satellites using single units for any planet in the solar system"""

from planet import Earth
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

    def __init__(self, radius, velocity, planet=Earth):
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
                self.get_angular_momentum_vector())
                / self.planet.mu) - (self.radius / self.radius.magnitude())

    def get_angular_momentum(self):
        """get_angular_momentum: returns the angular momentum of the orbit
        in m^2 / s
        :return: float"""
        return self.get_angular_momentum_vector().magnitude()

    def get_specific_energy(self):
        """get_specigic_energy: returns the specific energy of the orbi
        :return: float"""
        return (self.velocity.magnitude() ** 2 / 2) - (self.planet.mu / self.radius.magnitude())

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
        return self.get_semimajor_axis() * (1 - self.get_eccentricity())

    def get_radius_apoapsis(self):
        """get_radius_apoapsis: returns the radius of the satellite at the
        apoapsis
        :return: float"""
        return self.get_semimajor_axis() * (1 + self.get_eccentricity())

    def get_inclination(self):
        """get_inclination: returns tha angle of inclination of the orbit in degrees
        :return: float"""
        return radians_to_degrees(math.acos(Vector(0, 0, 1).dot_product(
            self.get_angular_momentum_vector())/self.get_angular_momentum()))

    def get_true_anomaly(self):
        """get_true_anomaly: returns the position of the satellite along its orbit in degrees
        :return: float"""
        if self.radius.magnitude() == round(self.get_radius_periapsis(), 0):
            return 0
        try:
            true = radians_to_degrees(math.acos((1 / self.get_eccentricity()) *
                                                ((self.get_orbital_parameter()
                                                / self.radius.magnitude()) - 1)))
        except ValueError:
            true = 0
        return true

    def get_elevation_angle(self):
        """get_elevation_angle: return the elevation angle of the satellite
        (i.e. the angle between the velocity vector and the local horizontal plane in degrees
        :return: float"""

        try:
            elev = radians_to_degrees(math.acos(self.get_angular_momentum() / (self.radius.magnitude() * self.velocity.magnitude())))
        except ValueError:
            elev = 0
        return elev

    def get_nodes_vector(self):
        """get_nodes_vector: returns the vector that points between the
        ascending and descending node
        :return: Vector"""
        return Vector(0, 0, 1).cross_product(self.get_angular_momentum_vector())

    def get_longitude_of_ascending_node(self):
        """get_longitude_of_ascending_node: returns the angle where the
        satellite passes from below the reference plane to above the
        reference plane in degrees.
        :return: float"""
        line_of_nodes = self.get_nodes_vector()
        if self.get_inclination() == 0:
            return "n/a"
        if line_of_nodes.j >= 0:
            return radians_to_degrees(math.acos((Vector(1, 0, 0).dot_product(
                line_of_nodes)) / line_of_nodes.magnitude()))
        else:
            return 360 - radians_to_degrees(math.acos((Vector(1, 0, 0).dot_product(
                line_of_nodes)) / line_of_nodes.magnitude()))

    def get_argument_of_periapsis(self):
        """get_argument_of_periapsis: returns the argument of periapsis of
        the orbit in degrees
        :return: float"""
        eccn_vector = self.get_eccentricity_vector()
        node_vector = self.get_nodes_vector()
        if node_vector.magnitude() == 0:
            return "n/a"
        if eccn_vector.k >= 0:
            return radians_to_degrees(math.acos((node_vector.dot_product(
                eccn_vector))/(node_vector.magnitude() *
                               eccn_vector.magnitude())))
        else:
            return radians_to_degrees(2 * math.pi - math.acos((node_vector.dot_product(
                eccn_vector))/(node_vector.magnitude() *
                               eccn_vector.magnitude())))

    def get_radius_at_angle(self, anomaly):
        """get_radius_at_angle: returns the magnitude of the radius at the
        given angle
        :param anomaly: the angle at which the orbir is at in degrees
        :return: float"""
        return self.get_orbital_parameter() / (1 + (self.get_eccentricity()
                                                    * math.cos(
            degrees_to_radians(anomaly))))

    def get_radius_vector_at_angle(self, anomaly):
        """get_radius_vector_at_angle: returns the radius vector when the
        orbit is at the specified angle. The vector formula used is:
        r = <r_x, r_y, r_z> =
            <r * cos(θ) * cos(i),
             r * sin(θ),
             r * cos(θ) * sin(i) >
        :param anomaly: angle at which the orbit is at in degrees
        :return: Vector"""
        new_radius = self.get_radius_at_angle(anomaly)
        inc = self.get_inclination()
        return Vector(new_radius * math.cos(degrees_to_radians(anomaly)) *
                      math.cos(degrees_to_radians(inc)),
                      new_radius * math.sin(degrees_to_radians(anomaly)),
                      new_radius * math.cos(degrees_to_radians(
                          anomaly)) * math.sin(degrees_to_radians(inc)))

    def get_velocity_at_radius(self, new_radius):
        """get_velocity_at_radius: return the velocity of the satellite at
        the given radius
        :param new_radius: radius of the orbit
        :return: float"""
        return math.sqrt(2 * (self.get_specific_energy() + (self.planet.mu /
                                                            new_radius)))

    def get_velocity_at_angle(self, anomaly):
        """get_velocity_at_angle: returns the velocity magnitude of the
        orbit at the specified angle
        :param anomaly: the angle at which the orbit is at in degrees
        :return: float"""
        return math.sqrt(2 * (self.get_specific_energy() + self.planet.mu /
                              self.get_radius_at_angle(anomaly)))

    def get_elevation_angle_at_angle(self, anomaly):
        """get_elevation_angle_at_angle: returns the elevation angle of
        the orbit at the specified angle, which is equal to arccos(h/rv).
        :param anomaly: angle at which the orbit is at in degrees
        :return: float"""
        try:
            elev = radians_to_degrees(math.acos(self.get_angular_momentum() / (
            self.get_radius_at_angle(anomaly) * self.get_velocity_at_angle(
                anomaly))))
        except ValueError:
            elev = 0
        return elev

    def get_parallel_angle_at_angle(self, anomaly):
        """get_parallel_angle_at_angle: returns the angle between the
        velocity vector and the and imaginary line going through the
        satellite and parallel to the eccentricty vector. This angle is
        equal to 180 - (true anamoly) - (zenith angle), the zenith angle
        being equal to 90 - (elevation angle)
        :param anomaly: the angle at which the orbit is at in degrees
        :return: float"""
        return -(anomaly - 90 - self.get_elevation_angle_at_angle(anomaly))

    # def get_semiminor_radius(self):
    #	"""get_semiminor_radius: returns the radius of the orbit when the
    #	satellite is at the semiminor axis
    #	:return: float"""
    #	return math.sqrt((self.get_semimajor_axis() * math.sqrt(1 -
    #
        # self.get_eccentricity() ** 2)) ** 2 +
    #	                 (self.get_semimajor_axis() -
    #	                  self.get_radius_periapsis()) ** 2)

    def get_velocity_vector_at_angle(self, anomaly):
        """get_velocity_vector_at_angle: returns the velocity vector when
        the orbit is at the specified angle
        :param anomaly: angle at which the orbit is at in degrees
        :return: Vector"""
        velocity = self.get_velocity_at_angle(anomaly)
        parallel_ang = degrees_to_radians(self.get_parallel_angle_at_angle(
            anomaly))
        inclination = degrees_to_radians(self.get_inclination())

        return Vector(-1 * velocity * math.cos(inclination) * math.cos(
            parallel_ang), velocity * math.sin(parallel_ang), velocity *
            math.cos(parallel_ang) * math.sin(inclination) * -1)

    def apply_thrust(self, delta_v):
        """apply_thrust: apply a given thrust vector to the current satellite
        :param delta_vector: the thrust vector to apply
        """
        # TODO: Test this function
        self.velocity = self.velocity + delta_v


sat1 = Satellite(Vector(7e6, 0, 0), Vector(0, 7793.526006824358, 0))
sat2 = Satellite(Vector(-5.e5, 7483314.773547883, 0), Vector(
    -7290.176038112294, 0, 0))
sat3 = Satellite(Vector(-3862068.9655172424, 6689299.670610837,
                        0), Vector(-6327.554537779295,
                                   -3166.119940272407, 0))
sat4 = Satellite(Vector(7e6 * math.cos(degrees_to_radians(30)), 0,
                        7e6 * math.sin(degrees_to_radians(30))), Vector(0,
                                                                        7793.526006824358, 0))
