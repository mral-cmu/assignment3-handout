import sys
import numpy as np
from sklearn.metrics import mean_squared_error

sys.path.append('../')

from quadrotor_simulator_py.quadrotor_planning import MuellerTrajectory

def compare_coefficients(student_soln, correct_soln, eps):
    assert(np.max(abs(student_soln-correct_soln)) < eps)

def test_mueller_trajectory():
    eps = 1e-3

    T = 2
    x0 = np.array([1.0, 0.0, 0.0])
    xf = np.array([0.0, 0.0, 0.0])
    mp = MuellerTrajectory(x0, xf, T)
    c = mp.coefficients
    correct_c = np.array([ 1., 0., 0., -1.25, 0.9375, -0.1875])
    compare_coefficients(c, correct_c, eps)

    x0 = np.array([0.2, 0.4, 0.6])
    xf = np.array([2.0, 0.2, 0.4])
    mp = MuellerTrajectory(x0, xf, T)
    c = mp.coefficients
    correct_c = np.array([0.2, 0.4, 0.3, 1.1, -0.9875, 0.2125])
    compare_coefficients(c, correct_c, eps)

    x0 = np.array([-0.2, 0.1, 0.2])
    xf = np.array([0.7, 0.3, 0.8])
    mp = MuellerTrajectory(x0, xf, T)
    c = mp.coefficients
    correct_c = np.array([-0.2, 0.1, 0.1, 0.725, -0.60625, 0.13125])
    compare_coefficients(c, correct_c, eps)

    print("Mueller Trajectory coefficients correct")

test_mueller_trajectory()
