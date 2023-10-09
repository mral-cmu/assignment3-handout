import sys
import numpy as np
import matplotlib.pyplot as plt
import pickle

sys.path.append('../')

from plot_states import plot
from check_states import check_states

from quadrotor_simulator_py.quadrotor_control.state import State
from quadrotor_simulator_py.quadrotor_planning import FlatSpaceTrajectory

def test1_flat_space_trajectory_get_ref():
    T = 2

    s0 = State()
    sf = State()

    s0.pos[0,0] = 1.
    s0.pos[1,0] = 2.
    s0.pos[2,0] = 1.
    s0.yaw = 3.14/4

    s0.vel[0,0] = 0.5
    s0.vel[1,0] = 0.2
    s0.vel[2,0] = 0.1

    sf.pos[0, 0] = 3.0
    sf.pos[1, 0] = 3.0
    sf.pos[2, 0] = 1.5
    sf.yaw = 3.14/2

    sf.vel[0,0] = 0.0
    sf.vel[1,0] = 0.4
    sf.vel[2,0] = 0.0

    flat_space_traj = FlatSpaceTrajectory(s0, sf, T)

    times = np.linspace(0, T, 100*T)
    states = []

    with open('../data/flat_space_traj1.pkl', 'rb') as file:
        correct = pickle.load(file)


    for idx in range(0, len(times)):
        time = times[idx]
        states.append(flat_space_traj.get_ref(time))
    plot(times, states, correct['states'])

    if check_states(states, correct['states']) == 3:
        print("Flat Space Trajectory 1 get_ref function correct")
    else:
        print("Flat Space Trajectory 1 get_ref function failed")


def test2_flat_space_trajectory_get_ref():
    T = 2

    s0 = State()
    sf = State()

    s0.pos[0,0] = 1.0
    s0.vel[0,0] = 1.0
    sf.pos[0, 0] = 3.0
    sf.vel[0,0] = 1.0
    sf.acc[0,0] = 0.0

    flat_space_traj = FlatSpaceTrajectory(s0, sf, T)

    times = np.linspace(0, T, 100*T)
    states = []

    with open('../data/flat_space_traj2.pkl', 'rb') as file:
        correct = pickle.load(file)

    for idx in range(0, len(times)):
        time = times[idx]
        states.append(flat_space_traj.get_ref(time))

    plot(times, states, correct['states'])

    if check_states(states, correct['states']) == 3:
        print("Flat Space Trajectory 2 get_ref function correct")
    else:
        print("Flat Space Trajectory 2 get_ref function failed")

test1_flat_space_trajectory_get_ref()
test2_flat_space_trajectory_get_ref()
