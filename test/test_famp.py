import sys
import copy
import os
import unittest
import numpy as np
import math
import matplotlib.pyplot as plt
import pickle

sys.path.append('../')

from check_states import check_states
from quadrotor_simulator_py.quadrotor_control.state import State
from quadrotor_simulator_py.utils import Rot3
from quadrotor_simulator_py.quadrotor_model import QuadrotorModel
from quadrotor_simulator_py.utils.quaternion import Quaternion
from quadrotor_simulator_py.quadrotor_planning.forwardarctrajectory import ForwardArcTrajectory

def test_forwardarcprimitives():
    with open('../data/famp_states.pkl', 'rb') as file:
        correct = pickle.load(file)

    curr_ref = correct['curr_ref']
    states = []
    for om in np.arange(-1, 1.05, 0.05):
        velx = 1.0
        omega = om
        velz = 0.2

        cmd = np.array([velx, omega, velz]).reshape(3,1)
        T = 2

        famp = ForwardArcTrajectory(curr_ref, cmd, T)
        xs = []
        ys = []
        ref = None
        for t in np.arange(0, T, 0.01):
            ref = famp.get_ref(t)
            xs.append(ref.pos[0,0])
            ys.append(ref.pos[1,0])
        plt.plot(xs, ys)
        states.append(famp.get_ref(T))

    if check_states(states, correct['states']) == 3:
        print('Forward arc motion primitives correct')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.gca().set_aspect('equal')
        plt.show()
    else:
        print('Forward arc motion primitives failure')

test_forwardarcprimitives()
