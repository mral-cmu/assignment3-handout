import sys
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.metrics import mean_squared_error

sys.path.append('../')

from plot_states import plot
from check_states import check_states

from quadrotor_simulator_py.quadrotor_control.state import State
from quadrotor_simulator_py.quadrotor_planning import FlatSpaceTrajectory
from quadrotor_simulator_py.quadrotor_planning import MultiFlatSpaceTrajectoryManager

def test1_multi_flat_space_traj_manager():
    T = 2

    trajmanager = MultiFlatSpaceTrajectoryManager()

    # Takeoff
    s0 = State()
    sf = State()
    s0.pos[2, 0] = 0.0
    sf.pos[2, 0] = 1.0
    flat_space_traj = FlatSpaceTrajectory(s0, sf, T)
    trajmanager.append(flat_space_traj, T)

    # Move +x 2 meters
    s0 = State()
    sf = State()
    s0.pos[2, 0] = 1.0
    sf.pos[0, 0] = 2.0
    sf.pos[2, 0] = 1.0
    flat_space_traj = FlatSpaceTrajectory(s0, sf, T)
    trajmanager.append(flat_space_traj, T)

    # Move +y 2 meters
    s0 = State()
    sf = State()
    s0.pos[2, 0] = 1.0
    s0.pos[0, 0] = 2.0
    sf.pos[0, 0] = 2.0
    sf.pos[1, 0] = 2.0
    sf.pos[2, 0] = 1.0
    flat_space_traj = FlatSpaceTrajectory(s0, sf, T)
    trajmanager.append(flat_space_traj, T)

    # Move -y 2 meters and -x 2 meters
    s0 = State()
    sf = State()
    s0.pos[2, 0] = 1.0
    s0.pos[0, 0] = 2.0
    s0.pos[1, 0] = 2.0
    s0.yaw = 0.0
    sf.pos[0, 0] = 0.0
    sf.pos[1, 0] = 0.0
    sf.pos[2, 0] = 1.0
    flat_space_traj = FlatSpaceTrajectory(s0, sf, T)
    trajmanager.append(flat_space_traj, T)

    # Land
    s0 = State()
    sf = State()
    s0.pos[2, 0] = 1.0
    sf.pos[2, 0] = 0.0
    flat_space_traj = FlatSpaceTrajectory(s0, sf, T)
    trajmanager.append(flat_space_traj, T)

    times = np.linspace(0, 5*T, 5*100*T)
    states = []

    with open('../data/multi_flat_space_traj1.pkl', 'rb') as file:
        correct = pickle.load(file)

    for idx in range(0, len(times)):
        time = times[idx]
        states.append(trajmanager.get_ref(time))
    plot(times, states, correct['states'])

    if check_states(states, correct['states']) == 3:
        print("Multi Flat Space Trajectory Test 1 correct")
    else:
        print("Multi Flat Space Trajectory Test 1 failed")


def test2_multi_flat_space_traj_manager():
    T = 2

    trajmanager = MultiFlatSpaceTrajectoryManager()

    # Takeoff
    s0 = State()
    sf = State()
    s0.pos[2, 0] = 0.0
    sf.pos[2, 0] = 1.0
    flat_space_traj = FlatSpaceTrajectory(s0, sf, T)
    trajmanager.append(flat_space_traj, T)

    # Yaw +90 degrees
    s0 = State()
    sf = State()
    sf.yaw = 3.14/2.0
    s0.pos[2, 0] = 1.0
    sf.pos[2, 0] = 1.0
    flat_space_traj = FlatSpaceTrajectory(s0, sf, T)
    trajmanager.append(flat_space_traj, T)

    # Yaw -90 degrees and land
    s0 = State()
    sf = State()
    s0.yaw = 3.14/2.0
    sf.yaw = 0.0
    s0.pos[2, 0] = 1.0
    sf.pos[2, 0] = 0.0
    flat_space_traj = FlatSpaceTrajectory(s0, sf, T)
    trajmanager.append(flat_space_traj, T)

    times = np.linspace(0, 3*T, 3*100*T)
    states = []

    with open('../data/multi_flat_space_traj2.pkl', 'rb') as file:
        correct = pickle.load(file)

    for idx in range(0, len(times)):
        time = times[idx]
        states.append(trajmanager.get_ref(time))
    plot(times, states, correct['states'])

    if check_states(states, correct['states']) == 3:
        print("Multi Flat Space Trajectory Test 2 correct")
    else:
        print("Multi Flat Space Trajectory Test 2 failed")

test1_multi_flat_space_traj_manager()
test2_multi_flat_space_traj_manager()
