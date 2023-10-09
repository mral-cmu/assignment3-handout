"""
quadrotor_simulator_py
========

Python-wrapper over Quadrotor Simulator package.
"""

__version__ = "0.0.0"

try:
    from . import quadrotor_model
    from . import quadrotor_planning
    from . import quadrotor_control
except:
    pass

__author__ = "Wennie Tabib"
__email__ = "wtabib@cmu.edu"
