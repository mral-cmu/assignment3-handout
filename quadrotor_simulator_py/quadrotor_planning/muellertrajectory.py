import numpy as np
from quadrotor_simulator_py.quadrotor_planning.polynomialtrajectory import PolynomialTrajectory


class MuellerTrajectory(PolynomialTrajectory):
    def __init__(self, x0, xf, T):
        """ Calculates the coefficients of the 5th order
        polynomial trajectory given fixed starting position,
        velocity, and acceleration as well as duration, T.
        The coefficients should be stored as self.coefficients.
        
        The polynomial is written as c0 + c1*t + ... c5*t^5.
        The input to the function are constraints and duration.
        The output of the function are coefficients for a single-axis
        polynomial trajectory.
        
        Reference: https://doi.org/10.1109/TRO.2015.2479878

        Args:
            x0: 1x3 numpy array consisting of starting position, velocity, and acceleration
            xf: 1x3 numpy array consisting of position, velocity, and acceleration at time T
            T: duration of the trajectory
        
        Output:
            coefficients: 1x6 numpy array of coefficients
        """

        # TODO: Assignment 3, Problem 1.1

        self.T = T
        self.coefficients = np.zeros(6)
