from bresenham import bresenham
import numpy as np

class CollisionChecker:

    def __init__(self, grid):
       self.grid = grid 

    def has_collision(self, p0, p1):
        x0 = p0[0]
        y0 = p0[1]

        x1 = p1[0]
        y1 = p1[1]

        intersections = list(bresenham(y0, x0, y1, x1))

        for point in intersections:
            if self.grid[point[0], point[1], 0] <= 0.5:
                return True

        return False
