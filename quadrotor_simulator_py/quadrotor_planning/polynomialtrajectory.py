import numpy as np

# Represents single axis polynomial trajectory
class PolynomialTrajectory:

    coefficients = None
    T = None

    def __init__(self, coefficients=None, T=None):
        """ Stores coefficients in the following form:
        p(t) = coefficients[0] + coefficients[1] * t + ... + 
               coefficients[n-1]*t^(n-1)
        
        Args:
            coefficients: 1xn numpy array representing the coefficients
                          for a single axis trajectory
            T: scalar input for duration of the trajectory
        """

        self.coefficients = coefficients
        self.T = T

    def derivative(self, order=0):
        """ returns the derivative of the coefficients specified by the given order.
        For example: 
            - order 0, return same coefficients
            - order 1, return first derivative
            - order 2, return second derivative
            - ...and so on
        
        Args: 
            order: scalar input representing desired derivative for the coefficients
        
        Output:
            coeffs: 1 x (n-order) numpy array of coefficients, which may
                    be evaluated to obtain the values of the derivative 
                    equal to order.
        """

        # TODO: Assignment 3, Problem 1.2

        temp_coeffs = np.zeros(len(self.coefficients.tolist())-order)
        return temp_coeffs

    def evaluate(self, time, order):
        """ Takes the derivative of the coefficients specified by the input
            `order` and then evaluates them for time `time`.
        
        Args:
            order: order of the derivative to take of the coefficients
            time: time at which the derivative of the coefficients are evaluated
        
        Output:
            value: scalar value representing the evaluation of the polynomial
                   coefficients taken at time time.
        """

        # TODO: Assignment 3, Problem 1.2

        value = 0.0
        return value

    # Generate reference up to order at a given time
    def get_ref(self, time, order):
        """ Returns the references up to the derivative specified
            by order for the time specified by time.
        
        Example: get_ref(1, 4) will return a 1x5 np array consisting
                 of position, velocity, acceleration, jerk, snap
        
        Args:
            time: time at which to evaluate the polynomial up to the
                  derivative specified by order
            order: derivative to evaluate the polynomial
        """

        # TODO: Assignment 3, Problem 1.2

        ref = np.zeros(order+1)
        return ref
