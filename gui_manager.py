import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QLabel

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

        self.current_satellite = None

        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        self.canvas.resize(2048, 2048)

        # Style Radio Buttons
        self.style_radio_simple = QtWidgets.QRadioButton("Simple")
        self.style_radio_advanced = QtWidgets.QRadioButton("Advanced")

        self.style_radio_simple.clicked.connect(self.change_layout_simple)
        self.style_radio_advanced.clicked.connect(self.change_layout_advanced)

        self.style_radio_advanced.toggle()

        ################ Advanced Layout ##############
        # Radius Labels
        self.radius_label1 = QLabel("Radius: ")
        self.radius_label2 = QLabel("i + ")
        self.radius_label3 = QLabel("j + ")
        self.radius_label4 = QLabel("k m")

        # Velocity Labels
        self.velocity_label1 = QLabel("Velocity: ")
        self.velocity_label2 = QLabel("i + ")
        self.velocity_label3 = QLabel("j + ")
        self.velocity_label4 = QLabel("k m/s")

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
        ###############################################

        ####################### Simple Layout #######################
        # Radius Label
        #self.radius_simple_label1 = QLabel("Radius Periapsis: ")
        #self.radius_simple_label2 = QLabel("m ")

        # Radius Input
        #self.radius_simple_input = QLineEdit(self)

        # Velocity Label
        #self.velocity_simple_label1 = QLabel("Velocity Periapsis: ")
        #self.velocity_simple_label2 = QLabel("m/s")

        # Velocity Input
        #self.velocity_simple_input = QLineEdit(self)

        # Simple Plot Button
        #self.plot_simple = QtWidgets.QPushButton("Plot")
        # self.plot_simple.clicked.connect(self.plot_simple_orbit)
        #############################################################

        # Change Position Label
        self.change_pos_label1 = QLabel("Position ")
        self.change_pos_label2 = QLabel("° ")

        # Change Position Inputs
        self.chang_pos_input = QLineEdit(self)

        # Change Position Button
        self.chang_pos_button = QtWidgets.QPushButton("Change Position")
        self.chang_pos_button.clicked.connect(self.change_position)

        ####################### Advanced Layout #######################
        # Advanced Delta_V Labels
        self.delta_v_label1 = QLabel("ΔV: ")
        self.delta_v_label2 = QLabel("i + ")
        self.delta_v_label3 = QLabel("j + ")
        self.delta_v_label4 = QLabel("k m/s ")

        # Advanced Delta_V Inputs
        self.delta_v_i = QLineEdit(self)
        self.delta_v_j = QLineEdit(self)
        self.delta_v_k = QLineEdit(self)

        # Advanced Delta_V Button
        self.apply_delta_v_button = QtWidgets.QPushButton("Apply")
        self.apply_delta_v_button.clicked.connect(self.apply_delta_v)
        ###############################################################

        ######################## Simple Layout ########################
        # Simple Delta_V Labels
        #self.delta_v_simple_label1 = QLabel("ΔV: ")
        #self.delta_v_simple_label2 = QLabel("m/s")

        # Simple Delta_V Input
        #self.delta_v_simple_input = QLineEdit(self)

        # Simple Delta_v Button
        #self.delta_v_apply_simple = QtWidgets.QPushButton("Apply")
        # self.delta_v_apply_simple.clicked.connect(self.apply_delta_v_simple)
        ###############################################################

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
        self.master_horizontal_layout = QtWidgets.QVBoxLayout()
        self.master_horizontal_layout_simple = QtWidgets.QVBoxLayout()

        self.canvas_vertical_layout = QtWidgets.QVBoxLayout()

        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setSpacing(10)

        self.vertical_layout_simple = QtWidgets.QVBoxLayout()
        self.vertical_layout_simple.setSpacing(10)

        self.change_style_radio_layout = QtWidgets.QHBoxLayout()

        ############### Advanced Layout #################
        self.horizontal_layout1 = QtWidgets.QHBoxLayout()
        self.horizontal_layout2 = QtWidgets.QHBoxLayout()
        #################################################

        #################### Simple Layout #####################
        #self.simple_vertical_layout = QtWidgets.QVBoxLayout()
        #self.simple_horizontal_layout = QtWidgets.QHBoxLayout()
        ########################################################

        self.parameters_layout = QtWidgets.QHBoxLayout()
        self.parameters_layout_left = QtWidgets.QVBoxLayout()
        self.parameters_layout_right = QtWidgets.QVBoxLayout()
        self.parameters_layout.addLayout(self.parameters_layout_left)
        self.parameters_layout.addLayout(self.parameters_layout_right)

        self.change_pos_layout = QtWidgets.QHBoxLayout()
        self.delta_v_layout = QtWidgets.QHBoxLayout()
        self.delta_v_simple_layout = QtWidgets.QHBoxLayout()

        # Canvas Layout
        self.canvas_vertical_layout.addWidget(self.toolbar)
        self.canvas_vertical_layout.addWidget(self.canvas)

        # Change Style Radio Layout
        self.change_style_radio_layout.addWidget(self.style_radio_simple)
        self.change_style_radio_layout.addWidget(self.style_radio_advanced)

        #################### Advanced Layout ######################
        # Advanced Radius Layout
        self.horizontal_layout1.addWidget(self.radius_label1)
        self.horizontal_layout1.addWidget(self.radius_i)
        self.horizontal_layout1.addWidget(self.radius_label2)
        self.horizontal_layout1.addWidget(self.radius_j)
        self.horizontal_layout1.addWidget(self.radius_label3)
        self.horizontal_layout1.addWidget(self.radius_k)
        self.horizontal_layout1.addWidget(self.radius_label4)

        # Advanced Velocity Layout
        self.horizontal_layout2.addWidget(self.velocity_label1)
        self.horizontal_layout2.addWidget(self.velocity_i)
        self.horizontal_layout2.addWidget(self.velocity_label2)
        self.horizontal_layout2.addWidget(self.velocity_j)
        self.horizontal_layout2.addWidget(self.velocity_label3)
        self.horizontal_layout2.addWidget(self.velocity_k)
        self.horizontal_layout2.addWidget(self.velocity_label4)
        ###########################################################

        ##################### Simple Layout #######################
        # self.simple_horizontal_layout.addWidget(self.radius_simple_label1)
        # self.simple_horizontal_layout.addWidget(self.radius_simple_input)
        # self.simple_horizontal_layout.addWidget(self.radius_simple_label2)
        # self.simple_horizontal_layout.addWidget(self.velocity_simple_label1)
        # self.simple_horizontal_layout.addWidget(self.velocity_simple_input)
        # self.simple_horizontal_layout.addWidget(self.velocity_simple_label2)

        # self.simple_vertical_layout.addLayout(self.simple_horizontal_layout)
        # self.simple_vertical_layout.addWidget(self.plot_simple)
        ###########################################################

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

        # Change Position Layout
        self.change_pos_layout.addWidget(self.change_pos_label1)
        self.change_pos_layout.addWidget(self.chang_pos_input)
        self.change_pos_layout.addWidget(self.change_pos_label2)
        self.change_pos_layout.addWidget(self.chang_pos_button)

        ################### Advanced Layout #####################
        # Delta_V Layout
        self.delta_v_layout.addWidget(self.delta_v_label1)
        self.delta_v_layout.addWidget(self.delta_v_i)
        self.delta_v_layout.addWidget(self.delta_v_label2)
        self.delta_v_layout.addWidget(self.delta_v_j)
        self.delta_v_layout.addWidget(self.delta_v_label3)
        self.delta_v_layout.addWidget(self.delta_v_k)
        self.delta_v_layout.addWidget(self.delta_v_label4)
        self.delta_v_layout.addWidget(self.apply_delta_v_button)
        #########################################################

        #################### Simple Layout ######################
        # self.delta_v_simple_layout.addWidget(self.delta_v_simple_label1)
        # self.delta_v_simple_layout.addWidget(self.delta_v_simple_input)
        # self.delta_v_simple_layout.addWidget(self.delta_v_simple_label2)
        # self.delta_v_simple_layout.addWidget(self.delta_v_apply_simple)
        #########################################################

        ####################### Advanced Layout #######################
        self.vertical_layout.addLayout(self.change_style_radio_layout)
        self.vertical_layout.addLayout(self.horizontal_layout1)
        self.vertical_layout.addLayout(self.horizontal_layout2)
        self.vertical_layout.addWidget(self.button)
        self.vertical_layout.addLayout(self.change_pos_layout)
        self.vertical_layout.addLayout(self.delta_v_layout)
        self.vertical_layout.addLayout(self.parameters_layout)
        # self.vertical_layout.addLayout(self.parameters_layout)

        # Adding to Master Layout
        self.master_horizontal_layout.addLayout(self.vertical_layout)
        self.master_horizontal_layout.addLayout(self.canvas_vertical_layout)
        ###############################################################

        ########################### Simple Layout #############################
        # self.vertical_layout_simple.addLayout(self.change_style_radio_layout)
        # self.vertical_layout_simple.addLayout(self.simple_vertical_layout)
        # self.vertical_layout_simple.addLayout(self.change_pos_layout)
        # self.vertical_layout_simple.addLayout(self.delta_v_simple_layout)
        # self.vertical_layout_simple.addLayout(self.parameters_layout)
        # self.vertical_layout_simple.addLayout(self.parameters_layout)

        # Adding the Simple Master Layout
        # self.master_horizontal_layout_simple.addLayout(
        # self.vertical_layout_simple)
        # self.master_horizontal_layout_simple.addLayout(
        # self.canvas_vertical_layout)
        #######################################################################

        self.setLayout(self.master_horizontal_layout)

    def change_layout_simple(self):
        """change_layout_simple: changes the layout of the application to a
        simplified form
        :return: None"""
        # TODO
        print("Not implemented")

    def change_layout_advanced(self):
        """change_layout_advanced: changes the layout of the application to
        a simplified form
        :return: None"""
        print("Not Implemented")
        self.setLayout(self.master_horizontal_layout)

    def plot(self):
        """plot: gets the values from the QLineEdits and plots the orbit on
        the canvas ***ADVANCED MODE***
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
        self.current_satellite = satellite
        self.draw_orbit(self.current_satellite)

    def plot_simple_orbit(self):
        """plot_simple_orbit: retrieves the values from the line edits in
        simple form and plots the orbit ***SIMPLE MODE***
        :return: None"""
        # TODO
        print("Not implemented")
        radius_i_val = float(self.radius_simple_input.text())
        velocity_j_val = float(self.velocity_simple_input.text())

        satellite = Satellite(Vector(radius_i_val, 0, 0), Vector(0,
                                                                 velocity_j_val, 0))
        self.current_satellite = satellite
        self.draw_orbit(satellite)

    def apply_delta_v(self):
        """apply_delta_v: will create a new satellite object with the
        delta-v applied in the current satellites current position
        ***ADVANCED MODE***
        :return: None"""
        if self.current_satellite == None:
            raise TypeError("Must apply delta-V on a pre-existing "
                            "satellite.")  # TODO: Pop-up window
            return None

        velocity_i_val = float(0 if self.delta_v_i.text() == '' else self.delta_v_i.text())
        velocity_j_val = float(0 if self.delta_v_j.text() == '' else self.delta_v_j.text())
        velocity_k_val = float(0 if self.delta_v_k.text() == '' else self.delta_v_k.text())

        self.current_satellite.apply_thrust(Vector(velocity_i_val, velocity_j_val, velocity_k_val))
        self.change_position()
        self.draw_orbit(self.current_satellite)

    def apply_delta_v_simple(self):
        """apply_delta_v_simple: will create a new satellite object with the
        delta-v applied at the periapsis ***SIMPLE MODE***
        :return: None"""
        # TODO
        print("Not implemented")

    def change_position(self):
        """change_position: creates and plots a new orbit with a new current position
        :return: None"""
        print("Not implemented")
        true_anomaly = float(0 if self.chang_pos_input.text() == '' else self.chang_pos_input.text())

        satellite = Satellite(
            self.current_satellite.get_radius_vector_at_angle(true_anomaly),
            self.current_satellite.get_velocity_vector_at_angle(true_anomaly))

        self.current_satellite = satellite
        self.draw_orbit(self.current_satellite)

    def draw_orbit(self, satellite):
        """draw_orbit: draws the specified satellite on the parent figure
        :param satellite: orbit to draw
        :return: None"""
        self.update_parameters(satellite)
        self.figure.clear()
        OrbitPlotter(satellite, self.figure)
        self.canvas.draw()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())
