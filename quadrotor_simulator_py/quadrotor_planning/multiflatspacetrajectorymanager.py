import numpy as np

from quadrotor_simulator_py.quadrotor_control.state import State
from quadrotor_simulator_py.quadrotor_planning.flatspacetrajectory import FlatSpaceTrajectory


class MultiFlatSpaceTrajectoryManager:
    def __init__(self):
        """
        initializes empty list of FlatSpaceTrajectory (self.trajs)
        initializes empty array of knot times (self.knotts)
        """
        self.trajs = []
        self.knotts = np.array([])

    def append(self, traj, t):
        """ Appends a FlatSpaceTrajectory to list of FlatSpaceTrajectory's
            and manages knotts appropriatesly
        Args:
            traj: FlatSpaceTrajectory
            t: duration of FlatSpaceTrajectory
        """
        # TODO: Assignment 3, Problem 1.4
        pass

    def get_ref(self, t):
        """ Gets reference at time t, where time may be between 0
        and last knot time.
        
        Args:
           t: time between 0 and self.knotts[-1]
        
        Output:
           ref: State() queried at time t
        """

        # TODO: Assignment 3, Problem 1.4

        return State()
