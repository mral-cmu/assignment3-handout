import sys
import numpy as np
import matplotlib.pyplot as plt

from quadrotor_simulator_py.quadrotor_control.state import State

def plot(times, states, correct_states):
    labels = ['x', 'y', 'z']

    fig, axs = plt.subplots(3)
    x = np.array([s.pos[0, 0] for s in states])
    y = np.array([s.pos[1, 0] for s in states])
    z = np.array([s.pos[2, 0] for s in states])

    cx = np.array([s.pos[0, 0] for s in correct_states])
    cy = np.array([s.pos[1, 0] for s in correct_states])
    cz = np.array([s.pos[2, 0] for s in correct_states])

    pos = np.vstack((x, y, z))
    cpos = np.vstack((cx, cy, cz))
    for i in range(0, 3):
        axs[i].plot(times, pos[i, :], linewidth=4)
        axs[i].plot(times, cpos[i, :])
        axs[i].set_ylabel(labels[i])
    plt.suptitle('Position')
    axs[0].legend(['Student Soln.', 'Ground Truth'])
    plt.show()

    fig, axs = plt.subplots(3)
    xd = np.array([s.vel[0, 0] for s in states])
    yd = np.array([s.vel[1, 0] for s in states])
    zd = np.array([s.vel[2, 0] for s in states])
    vel = np.vstack((xd, yd, zd))

    xd = np.array([s.vel[0, 0] for s in correct_states])
    yd = np.array([s.vel[1, 0] for s in correct_states])
    zd = np.array([s.vel[2, 0] for s in correct_states])
    cvel = np.vstack((xd, yd, zd))

    for i in range(0, 3):
        axs[i].plot(times, vel[i, :], linewidth=4)
        axs[i].plot(times, cvel[i, :])
        axs[i].set_ylabel(labels[i])
    plt.suptitle('Velocity')
    axs[0].legend(['Student Soln.', 'Ground Truth'])
    plt.show()

    fig, axs = plt.subplots(3)
    xdd = np.array([s.acc[0, 0] for s in states])
    ydd = np.array([s.acc[1, 0] for s in states])
    zdd = np.array([s.acc[2, 0] for s in states])
    acc = np.vstack((xdd, ydd, zdd))

    xdd = np.array([s.acc[0, 0] for s in correct_states])
    ydd = np.array([s.acc[1, 0] for s in correct_states])
    zdd = np.array([s.acc[2, 0] for s in correct_states])
    cacc = np.vstack((xdd, ydd, zdd))
    for i in range(0, 3):
        axs[i].plot(times, acc[i, :], linewidth=4)
        axs[i].plot(times, cacc[i, :])
        axs[i].set_ylabel(labels[i])
    plt.suptitle('Acceleration')
    axs[0].legend(['Student Soln.', 'Ground Truth'])
    plt.show()

    fig, axs = plt.subplots(3)
    y = np.array([s.yaw for s in states])
    yd = np.array([s.dyaw for s in states])
    ydd = np.array([s.d2yaw for s in states])
    yaw = np.vstack((y, yd, ydd))

    y = np.array([s.yaw for s in correct_states])
    yd = np.array([s.dyaw for s in correct_states])
    ydd = np.array([s.d2yaw for s in correct_states])
    cyaw = np.vstack((y, yd, ydd))
    labels = ['$\psi$', '$\dot{\psi}$', '$\ddot{\psi}$']
    for i in range(0, 3):
        axs[i].plot(times, yaw[i, :], linewidth=4)
        axs[i].plot(times, cyaw[i, :])
        axs[i].set_ylabel(labels[i])
    plt.suptitle('Yaw and derivatives')
    axs[0].legend(['Student Soln.', 'Ground Truth'])
    plt.show()

