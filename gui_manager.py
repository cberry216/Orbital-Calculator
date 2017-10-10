import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit,QLabel

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as \
	FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as \
	NavigationToolbar
import matplotlib.pyplot as plt
from orbit_plotter import *

class Window(QDialog):
	""""""

	def __init__(self, parent=None):
		super(Window, self).__init__(parent)

		self.figure = plt.figure()

		self.canvas = FigureCanvas(self.figure)
		self.canvas.resize(1024,1024)

		# Radius Labels
		self.radius_label1 = QLabel("Radius = ")
		self.radius_label2 = QLabel("i + ")
		self.radius_label3 = QLabel("j + ")
		self.radius_label4 = QLabel("k")

		# Velocity Labels
		self.velocity_label1 = QLabel("Velocity = ")
		self.velocity_label2 = QLabel("i + ")
		self.velocity_label3 = QLabel("j + ")
		self.velocity_label4 = QLabel("k")

		# Radius Inputs
		self.radius_i = QLineEdit(self)
		self.radius_i.move(20, 20)
		self.radius_i.resize(60, 40)

		self.radius_j = QLineEdit(self)
		self.radius_j.move(20, 20)
		self.radius_j.resize(60, 40)

		self.radius_k = QLineEdit(self)
		self.radius_k.move(20, 20)
		self.radius_k.resize(60, 40)

		# Velocity Inputs
		self.velocity_i = QLineEdit(self)
		self.velocity_i.move(20, 20)
		self.velocity_i.resize(60, 40)

		self.velocity_j = QLineEdit(self)
		self.velocity_j.move(20, 20)
		self.velocity_j.resize(60, 40)

		self.velocity_k = QLineEdit(self)
		self.velocity_k.move(20, 20)
		self.velocity_k.resize(60, 40)

		#Delta_V Labels
		self.delta_v_label1 = QLabel("ΔV: ")
		self.delta_v_label2 = QLabel("i + ")
		self.delta_v_label3 = QLabel("j + ")
		self.delta_v_label4 = QLabel("k @ ")
		self.delta_v_label5 = QLabel("°")

		#Delta_V Inputs
		self.delta_v_i = QLineEdit(self)
		self.delta_v_j = QLineEdit(self)
		self.delta_v_k = QLineEdit(self)
		self.delta_v_true_anomaly = QLineEdit(self)

		#Delta_V Button
		self.apply_delta_v_button = QtWidgets.QPushButton("Apply")
		self.apply_delta_v_button.clicked.connect(self.apply_delta_v)

		# Orbital Parameter Outputs
		self.orb_param_left_curr_radius = QLabel("Current Radius: n/a")
		self.orb_param_left_curr_velocity = QLabel("Current Velocity: n/a")
		self.orb_param_left_radius_periapsis = QLabel("Radius Peripasis: n/a")
		self.orb_param_left_velocity_periapsis = QLabel("Velocity @ "
		                                               "Periapsis: n/a")
		self.orb_param_left_radius_apoapsis = QLabel("Radius Apoapsis: n/a")
		self.orb_param_left_velocity_apoapsis = QLabel("Velocity @ Apoapsis:"
		                                               " n/a")
		self.orb_param_left_mean_radius = QLabel("Mean Radius: n/a")
		self.orb_param_left_mean_velocity = QLabel("Mean Velocity: n/a")
		self.orb_param_left_eccentricity = QLabel("Eccentricity: n/a")
		self.orb_param_left_orbital_parameter = QLabel("Orbital Parameter: "
		                                               "n/a")
		self.orb_param_left_true_anomaly = QLabel("True Anomaly: n/a")

		self.orb_param_right_radius_vector = QLabel("Radius Vector: n/a")
		self.orb_param_right_velocity_vector = QLabel("Velocity Vector: n/a")
		self.orb_param_right_eccentricity_vector = QLabel("Eccentricity "
		                                                  "Vector: n/a")
		self.orb_param_right_angular_momentum_vector = QLabel("Angular "
		                                                     "Momentum "
		                                                      "Vector: n/a")
		self.orb_param_right_angular_momentum = QLabel("Angular Momentum: n/a")
		self.orb_param_right_specific_energy = QLabel("Specific Energy: n/a")
		self.orb_param_right_longitude_of_ascending_node = QLabel("Longitude "
		                                                         "of "
		                                                          "Ascending Node: n/a")
		self.orb_param_right_argument_of_periapsis = QLabel("Argument of "
		                                                  "Periapsis: n/a")
		self.orb_param_right_elevation_angle = QLabel("Elevation Angle: n/a")
		self.orb_param_right_inclination = QLabel("Inclination: n/a")

		# Toolbar
		self.toolbar = NavigationToolbar(self.canvas, self)

		# Plot Button
		self.button = QtWidgets.QPushButton('Plot')
		self.button.clicked.connect(self.plot)

		# Layout
		self.vertical_layout = QtWidgets.QVBoxLayout()
		self.vertical_layout.setSpacing(10)

		self.horizontal_layout1 = QtWidgets.QHBoxLayout()
		self.horizontal_layout2 = QtWidgets.QHBoxLayout()

		self.parameters_layout = QtWidgets.QHBoxLayout()
		self.parameters_layout_left = QtWidgets.QVBoxLayout()
		self.parameters_layout_right = QtWidgets.QVBoxLayout()
		self.parameters_layout.addLayout(self.parameters_layout_left)
		self.parameters_layout.addLayout(self.parameters_layout_right)

		self.delta_v_layout = QtWidgets.QHBoxLayout()

		# Radius Layout
		self.horizontal_layout1.addWidget(self.radius_label1)
		self.horizontal_layout1.addWidget(self.radius_i)
		self.horizontal_layout1.addWidget(self.radius_label2)
		self.horizontal_layout1.addWidget(self.radius_j)
		self.horizontal_layout1.addWidget(self.radius_label3)
		self.horizontal_layout1.addWidget(self.radius_k)
		self.horizontal_layout1.addWidget(self.radius_label4)

		# Velocity Layout
		self.horizontal_layout2.addWidget(self.velocity_label1)
		self.horizontal_layout2.addWidget(self.velocity_i)
		self.horizontal_layout2.addWidget(self.velocity_label2)
		self.horizontal_layout2.addWidget(self.velocity_j)
		self.horizontal_layout2.addWidget(self.velocity_label3)
		self.horizontal_layout2.addWidget(self.velocity_k)
		self.horizontal_layout2.addWidget(self.velocity_label4)

		# Parameter Layout
		self.parameters_layout_left.addWidget(self.orb_param_left_curr_radius)
		self.parameters_layout_left.addWidget(self.orb_param_left_curr_velocity)
		self.parameters_layout_left.addWidget(self.orb_param_left_radius_periapsis)
		self.parameters_layout_left.addWidget(self.orb_param_left_velocity_periapsis)
		self.parameters_layout_left.addWidget(self.orb_param_left_radius_apoapsis)
		self.parameters_layout_left.addWidget(self.orb_param_left_velocity_apoapsis)
		self.parameters_layout_left.addWidget(self.orb_param_left_mean_radius)
		self.parameters_layout_left.addWidget(self.orb_param_left_mean_velocity)
		self.parameters_layout_left.addWidget(self.orb_param_left_eccentricity)
		self.parameters_layout_left.addWidget(self.orb_param_left_orbital_parameter)
		self.parameters_layout_left.addWidget(self.orb_param_left_true_anomaly)

		self.parameters_layout_right.addWidget(self.orb_param_right_radius_vector)
		self.parameters_layout_right.addWidget(self.orb_param_right_velocity_vector)
		self.parameters_layout_right.addWidget(self.orb_param_right_eccentricity_vector)
		self.parameters_layout_right.addWidget(self.orb_param_right_angular_momentum_vector)
		self.parameters_layout_right.addWidget(self.orb_param_right_angular_momentum)
		self.parameters_layout_right.addWidget(self.orb_param_right_specific_energy)
		self.parameters_layout_right.addWidget(self.orb_param_right_longitude_of_ascending_node)
		self.parameters_layout_right.addWidget(
			self.orb_param_right_argument_of_periapsis)
		self.parameters_layout_right.addWidget(self.orb_param_right_elevation_angle)
		self.parameters_layout_right.addWidget(self.orb_param_right_inclination)

		self.parameters_layout.addLayout(self.parameters_layout_left)
		self.parameters_layout.addLayout(self.parameters_layout_right)

		# Delta_V Layout
		self.delta_v_layout.addWidget(self.delta_v_label1)
		self.delta_v_layout.addWidget(self.delta_v_i)
		self.delta_v_layout.addWidget(self.delta_v_label2)
		self.delta_v_layout.addWidget(self.delta_v_j)
		self.delta_v_layout.addWidget(self.delta_v_label3)
		self.delta_v_layout.addWidget(self.delta_v_k)
		self.delta_v_layout.addWidget(self.delta_v_label4)
		self.delta_v_layout.addWidget(self.delta_v_true_anomaly)
		self.delta_v_layout.addWidget(self.delta_v_label5)
		self.delta_v_layout.addWidget(self.apply_delta_v_button)

		# Adding All the Layouts
		self.vertical_layout.addWidget(self.toolbar)
		self.vertical_layout.addWidget(self.canvas)
		self.vertical_layout.addLayout(self.horizontal_layout1)
		self.vertical_layout.addLayout(self.horizontal_layout2)
		self.vertical_layout.addWidget(self.button)
		self.vertical_layout.addLayout(self.delta_v_layout)
		self.vertical_layout.addLayout(self.parameters_layout)
		self.vertical_layout.addLayout(self.parameters_layout)
		self.setLayout(self.vertical_layout)

	def plot(self):
		"""plot: gets the values from the QLineEdits and plots the orbit on
		the canvas
		:return: None"""
		radius_i_val = float(self.radius_i.text())
		radius_j_val = float(self.radius_j.text())
		radius_k_val = float(self.radius_k.text())

		velocity_i_val = float(self.velocity_i.text())
		velocity_j_val = float(self.velocity_j.text())
		velocity_k_val = float(self.velocity_k.text())

		satellite = Satellite(Vector(radius_i_val, radius_j_val,
		                             radius_k_val), Vector(velocity_i_val,
		                                                   velocity_j_val, velocity_k_val))

		self.draw_orbit(satellite)

	def apply_delta_v(self):
		"""apply_delta_v: will create a new satellite object with the
		delta-v applied in the current satellites current position
		:return: None"""
		print("Not Implemented")

	def update_parameters(self, satellite):
		"""update_parameters: updates the values stored in the parameters
		labels to reflect the current orbit and satellite
		:param satellite: the given satellite to retrieve orbital parameters from
		:return: None"""
		self.orb_param_left_curr_radius.setText("Current Radius: " + str(
			round(satellite.radius.magnitude(), 7)))
		self.orb_param_left_curr_velocity.setText("Current Velocity: " +
		                                          str(
			                                          round(
				                                          satellite.velocity.magnitude(),
				                                          7)))
		self.orb_param_left_radius_periapsis.setText("Radius Peripasis: " +
		                                             str(
			                                             round(
				                                             satellite.get_radius_periapsis(),
				                                             7)))
		self.orb_param_left_velocity_periapsis.setText("Velocity @ "
		                                               "Periapsis: " + str(
			round(satellite.get_velocity_at_radius(
				satellite.get_radius_periapsis()), 7)))
		self.orb_param_left_radius_apoapsis.setText("Radius Apoapsis: " +
		                                            str(
			                                            round(
				                                            satellite.get_radius_apoapsis(),
				                                            7)))
		self.orb_param_left_velocity_apoapsis.setText(
			"Velocity @ Apoapsis: " + str(
				round(satellite.get_velocity_at_radius(
					satellite.get_radius_apoapsis()), 7)))
		self.orb_param_left_mean_radius.setText("Mean Radius: n/a")
		self.orb_param_left_mean_velocity.setText("Mean Velocity: n/a")
		self.orb_param_left_eccentricity.setText("Eccentricity: " + str(
			round(satellite.get_eccentricity(), 7)))
		self.orb_param_left_orbital_parameter.setText(
			"Orbital Parameter: " + str(
				round(satellite.get_orbital_parameter(), 7)))
		self.orb_param_left_true_anomaly.setText("True Anomaly: " + str(
			round(satellite.get_true_anomaly(), 7)))

		self.orb_param_right_radius_vector.setText("Radius Vector: " + str(
			round(satellite.radius, 7)))
		self.orb_param_right_velocity_vector.setText("Velocity Vector: " +
		                                             str(
			                                             round(
				                                             satellite.velocity, 7)))
		self.orb_param_right_eccentricity_vector.setText("Eccentricity "
		                                                 "Vector: " + str(
			round(satellite.get_eccentricity_vector(), 7)))
		self.orb_param_right_angular_momentum_vector.setText("Angular "
		                                                     "Momentum "
		                                                     "Vector: " +
		                                                     str(
			                                                     round(
				                                                     satellite.get_angular_momentum_vector(), 7)))
		self.orb_param_right_angular_momentum.setText("Angular Momentum: "
		                                              + str(
			round(satellite.get_angular_momentum(), 7)))
		self.orb_param_right_specific_energy.setText("Specific Energy: " +
		                                             str(
			                                             round(
				                                             satellite.get_specific_energy(),
				                                             7)))
		self.orb_param_right_longitude_of_ascending_node.setText("Longitude "
		                                                         "of "
		                                                         "Ascending "
		                                                         "Node: " +
		                                                         str(
			                                                         satellite.get_longitude_of_ascending_node()))
		self.orb_param_right_argument_of_periapsis.setText("Argument of "
		                                                 "Periapsis: " + str(
			satellite.get_argument_of_periapsis()))
		self.orb_param_right_elevation_angle.setText("Elevation Angle: " +
		                                            str(
			                                            round(
				                                            satellite.get_elevation_angle(), 7)))
		self.orb_param_right_inclination.setText("Inclination: " + str(
			round(satellite.get_inclination(), 7)))

	def draw_orbit(self, satellite):
		"""draw_orbit: draws the specified satellite on the parent figure
		:param satellite: orbit to draw
		:return: None"""
		self.update_parameters(satellite)
		self.figure.clear()
		OrbitPlotter(satellite, self.figure)
		self.canvas.draw()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = Window()
	main.show()
	sys.exit(app.exec_())