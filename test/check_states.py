import sys
import numpy as np
from sklearn.metrics import mean_squared_error

sys.path.append('../')

from quadrotor_simulator_py.quadrotor_control.state import State

def rmse(student, correct, eps=1e-3):
    if np.sqrt(mean_squared_error(student, correct)) < eps:
        return 1.
    return 0.

def check_states(states, correct_states):
    total = 0.
    pos = np.zeros((4, len(states)))
    pos[0,:] = np.array([s.pos[0, 0] for s in states])
    pos[1,:] = np.array([s.pos[1, 0] for s in states])
    pos[2,:] = np.array([s.pos[2, 0] for s in states])
    pos[3,:] = np.array([s.yaw for s in states])

    cpos = np.zeros((4, len(correct_states)))
    cpos[0,:] = np.array([s.pos[0, 0] for s in correct_states])
    cpos[1,:] = np.array([s.pos[1, 0] for s in correct_states])
    cpos[2,:] = np.array([s.pos[2, 0] for s in correct_states])
    cpos[3,:] = np.array([s.yaw for s in correct_states])
    total += rmse(pos, cpos)

    vel = np.zeros((4, len(states)))
    vel[0,:] = np.array([s.vel[0, 0] for s in states])
    vel[1,:] = np.array([s.vel[1, 0] for s in states])
    vel[2,:] = np.array([s.vel[2, 0] for s in states])
    vel[3,:] = np.array([s.dyaw for s in states])

    cvel = np.zeros((4, len(correct_states)))
    cvel[0,:] = np.array([s.vel[0, 0] for s in correct_states])
    cvel[1,:] = np.array([s.vel[1, 0] for s in correct_states])
    cvel[2,:] = np.array([s.vel[2, 0] for s in correct_states])
    cvel[3,:] = np.array([s.dyaw for s in correct_states])
    total += rmse(vel, cvel)

    acc = np.zeros((4, len(states)))
    acc[0,:] = np.array([s.acc[0, 0] for s in states])
    acc[1,:] = np.array([s.acc[1, 0] for s in states])
    acc[2,:] = np.array([s.acc[2, 0] for s in states])
    acc[3,:] = np.array([s.d2yaw for s in states])

    cacc = np.zeros((4, len(correct_states)))
    cacc[0,:] = np.array([s.acc[0, 0] for s in correct_states])
    cacc[1,:] = np.array([s.acc[1, 0] for s in correct_states])
    cacc[2,:] = np.array([s.acc[2, 0] for s in correct_states])
    cacc[3,:] = np.array([s.d2yaw for s in correct_states])
    total += rmse(acc, cacc)

    return total


