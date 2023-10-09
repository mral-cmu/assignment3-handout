import sys
import copy
import os
import unittest
import numpy as np
import math
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from bresenham import bresenham

sys.path.append('../')

from quadrotor_simulator_py.quadrotor_control.state import State
from quadrotor_simulator_py.utils import Rot3
from quadrotor_simulator_py.quadrotor_model import QuadrotorModel
from quadrotor_simulator_py.utils.quaternion import Quaternion
from quadrotor_simulator_py.quadrotor_planning.rrt import RRT
from quadrotor_simulator_py.quadrotor_planning.collision_checker import CollisionChecker

def run_rrt_test(start, end, plot=True):
    grid = mpimg.imread('../data/map.png')
    rrt = RRT(start, end, grid)
    collision_checker = CollisionChecker(grid)
    end_node = rrt.run()

    for key in rrt.tree:
        parent = rrt.tree[key].position
        children = rrt.tree[key].children
        for i in range(0, len(children)):
            c = rrt.tree[children[i]].position
            xs = [parent[0], c[0]]
            ys = [parent[1], c[1]]

            if plot:
                plt.plot(xs, ys, 'm')

    assert(end_node.idx != end_node.parent_idx)

    success = 1.0
    while end_node.idx != end_node.parent_idx:
        c = end_node.position
        p = rrt.tree[end_node.parent_idx].position
        if collision_checker.has_collision(c, p):
            success = 0.0

        xs = [p[0], c[0]]
        ys = [p[1], c[1]]
        end_node = rrt.tree[end_node.parent_idx]

        if plot:
            plt.plot(xs, ys, 'c', linewidth=3)

    if plot:
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.gca().set_aspect('equal')
        plt.imshow(grid)
        plt.plot(start[0], start[1], 'r+')
        plt.plot(end[0], end[1], 'b+')
        plt.show()
    return success

success = 0.0
start = np.array([250, 250])
end = np.array([120, 100])
success += run_rrt_test(start, end, True)

start = np.array([100, 120])
end = np.array([150, 220])
success += run_rrt_test(start, end, False)
print('RRT succeeded ' + str(int(success)) + ' out of 2 tests')
