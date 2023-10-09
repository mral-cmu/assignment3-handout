import sys
import numpy as np

sys.path.append('../')

from quadrotor_simulator_py.quadrotor_planning import PolynomialTrajectory

def compare_coefficients(student_soln, correct_soln, eps=1e-3):
    assert(np.max(abs(student_soln-correct_soln)) < eps)

def test_polynomial_trajectory_derivative():
    T = 2
    c = np.array([0.2, 0.4, 0.3, 1.1, -0.9875, 0.2125])
    p = PolynomialTrajectory(c, T)

    order0 = np.array([0.2, 0.4, 0.3, 1.1, -0.9875, 0.2125])
    order1 = np.array([0.4, 0.6, 3.3, -3.95, 1.0625])
    order2 = np.array([0.6, 6.6, -11.85, 4.25])
    order3 = np.array([6.6, -23.7, 12.75])
    order4 = np.array([-23.7, 25.5])

    compare_coefficients(p.derivative(0), order0)
    compare_coefficients(p.derivative(1), order1)
    compare_coefficients(p.derivative(2), order2)
    compare_coefficients(p.derivative(3), order3)
    compare_coefficients(p.derivative(4), order4)

    c = np.array([-0.2, 0.1, 0.1, 0.725, -0.60625, 0.13125])
    p = PolynomialTrajectory(c, T)
    order0 = np.array([-0.2, 0.1, 0.1, 0.725, -0.60625, 0.13125])
    order1 = np.array([0.1, 0.2, 2.175, -2.425, 0.65625])
    order2 = np.array([ 0.2, 4.35, -7.275, 2.625])
    order3 = np.array([4.35, -14.55, 7.875])
    order4 = np.array([-14.55, 15.75])

    compare_coefficients(p.derivative(0), order0)
    compare_coefficients(p.derivative(1), order1)
    compare_coefficients(p.derivative(2), order2)
    compare_coefficients(p.derivative(3), order3)
    compare_coefficients(p.derivative(4), order4)

    print("Polynomial Trajectory derivative function correct")

def test_polynomial_trajectory_evaluate():
    T = 2
    c = np.array([0.2, 0.4, 0.3, 1.1, -0.9875, 0.2125])
    p = PolynomialTrajectory(c, T)
    correct = np.array([1.225, 1.4125, -0.4, -4.35, 1.8])
    for i in range(0, 5):
        assert(abs(p.evaluate(1, i)-correct[i]) < 1e-03)

    c = np.array([-0.2, 0.1, 0.1, 0.725, -0.60625, 0.13125])
    p = PolynomialTrajectory(c, T)

    correct = np.array([0.25, 0.70625, -0.10, -2.325, 1.2])
    for i in range(0, 5):
        assert(abs(p.evaluate(1, i)-correct[i]) < 1e-03)

    print("Polynomial Trajectory evaluate function correct")

def test_polynomial_trajectory_get_ref():
    T = 2
    c = np.array([0.2, 0.4, 0.3, 1.1, -0.9875, 0.2125])
    p = PolynomialTrajectory(c, T)
    correct = np.array([1.225, 1.4125, -0.4, -4.35, 1.8])
    assert(np.max(abs(p.get_ref(1, 4) - correct)) < 1e-3)

    c = np.array([-0.2, 0.1, 0.1, 0.725, -0.60625, 0.13125])
    p = PolynomialTrajectory(c, T)
    correct = np.array([0.25, 0.70625, -0.1, -2.325, 1.2])
    assert(np.max(abs(p.get_ref(1, 4) - correct)) < 1e-3)

    print("Polynomial Trajectory get_ref function correct")

test_polynomial_trajectory_derivative()
test_polynomial_trajectory_evaluate()
test_polynomial_trajectory_get_ref()
