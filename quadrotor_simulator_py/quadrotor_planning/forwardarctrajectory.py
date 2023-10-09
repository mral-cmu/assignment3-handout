import numpy as np

from numpy import arctan2 as atan2
from numpy import arcsin as asin
from numpy import cos as cos
from numpy import sin as sin

from . import PolynomialTrajectory
from quadrotor_simulator_py.quadrotor_control.state import State
from quadrotor_simulator_py.utils.pose import Pose
from quadrotor_simulator_py.utils.quaternion import Quaternion
from quadrotor_simulator_py.utils.rotation3 import Rotation3


class ForwardArcTrajectory:

    T = 0.0
    coeffs = []
    initialized = False

    def __init__(self, curr_ref, cmd, T):
        """ Calculates the 9th order forward arc motion primitive coefficients
        
        Args:
            curr_ref is a state object for where to sample the trajectory
            cmd is a 3x1 numpy array consisting of [vel_x, omega, vel_z]
            T is the primitive duration
        
        Output:
            coeffs: 4x9 world frame coefficients
        """

        self.T = T
        coeffs_world_frame = np.zeros((4,9))
        self.coeffs = coeffs_world_frame
        self.initialized = True

    def get_ref(self, t):
        """ Returns reference as State() for a multi-axis trajectory.
            The multi-axis trajectory contains single axis trajectories
            for x, y, z, and yaw. These should be derived by querying
            self.coeffs, which stores the coefficients 4x9 numpy matrix.
        
        Args:
            t: time at which the reference should be generated.
       
        Output:
            s: State() instance populated with references
        """

        s = State()
        return s
