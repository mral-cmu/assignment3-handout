import numpy as np

from quadrotor_simulator_py.quadrotor_control.state import State
from quadrotor_simulator_py.quadrotor_planning.muellertrajectory import MuellerTrajectory
from quadrotor_simulator_py.utils.rotation3 import Rotation3


class FlatSpaceTrajectory:

    def __init__(self, s0, sf, T):
        self.T = T
        self.trajs = []

        x0s = self.state_to_arrays(s0)
        xfs = self.state_to_arrays(sf)
        if len(x0s) == 4 and len(xfs) == 4:
            for i in range(0, 4):
                self.trajs.append(MuellerTrajectory(x0s[i, :], xfs[i, :], T))
            self.T = T
        else:
            raise Exception(
                "FlatSpaceTrajectory Failure! len(x0s) == xfs == 4")

    def state_to_arrays(self, s):
        xs = np.zeros((4,3))
        for i in range(0,3):
            xs[i,:] = np.array([s.pos[i,0], s.vel[i,0], s.acc[i,0]])
        xs[3,:] = np.array([s.yaw, s.dyaw, s.d2yaw])
        return xs

    def get_ref(self, t):
        """ Returns reference as State() for a multi-axis trajectory.
            The multi-axis trajectory contains single axis trajectories
            for x, y, z, and yaw. These should be derived by querying
            self.trajs, which stores the coefficients as a list of 
            1xn numpy arrays.
        
        Args:
            t: time at which the reference should be generated.
       
        Output:
            s: State() instance populated with references
        """

        # TODO: Assignment 3, Problem 1.3
        s = State()

        return s
