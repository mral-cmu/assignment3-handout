import numpy as np
from math import floor

from quadrotor_simulator_py.quadrotor_control.state import State
from quadrotor_simulator_py.quadrotor_planning.collision_checker import CollisionChecker

class Node:

    def __init__(self, parent_idx, position):

        self.parent_idx = parent_idx
        self.idx = position[1] * position[0] + position[0]
        self.position = position
        self.children = []

    def append_child(self, child):
        self.children.append(child.idx)

class RRT:

    def __init__(self, start, end, grid):
        self.collision_checker = CollisionChecker(grid)
        self.start = start
        self.end = end
        self.grid = grid
        self.tree = {}
        self.insert_root_node(start)

    def run(self):
        """ Runs the RRT algorithm until a path is found between the start and
            end positions.
        
        Output:
            node: node representing end position
        """

        # TODO: Assignment 3, Problem 3
        return Node(0, np.array([0,0]))

    def get_idx(self, position):
        x = position[0]
        y = position[1]
        return y * x + x

    def insert_root_node(self, position):
        idx = self.get_idx(position)
        root = Node(idx, position)
        self.tree[idx] = root

    def find_nearest_node(self, position):
        """ Finds the node that has a position closest to the input position

        Args:
            position: 1x2 numpy array
        
        Output:
            node: Node class instance representing node with
                  closest position to input position.
        """

        # TODO: Assignment 3, Problem 3
        return Node(0, np.array([0,0]))

    def insert_node(self, parent_node, position):
        """ Create child node given parent node and position of child node

        Args:
            position: 1x2 numpy array
            parent_node: Node instance that represents parent
        
        Output:
            child_node: Node class instance representing child node
        """

        # TODO: Assignment 3, Problem 3
        return Node(0, np.array([0,0]))

    def sample(self):
        """ Randomly sample from list of existing positions within the
            grid
       
        Output:
            (idx, position): integer index and position pair
                             position represents a 1x2 numpy array
        """
        return (0, np.array([0,0]))
