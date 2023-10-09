# Quadrotor Motion Planning

Goals: In this assignment, you will implement motion planners that may
be used by a quadrotor.

### Academic Integrity
1. Do not publicly share your solution (using GitHub or otherwise)
2. Collaboration is encouraged but you should write final code on your own.

## 0. Setup
Download the assignment.

```
git clone git@github.com:mral-cmu/assignment3-handout.git
cd assignment3-handout
git lfs install
git lfs pull
```

Note: if the above command results in a Permission denied (public key)
error, then try setting up an SSH key in your Github account using the
instructions
[here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

If the cloning still does not work, use

```
git clone https://github.com/mral-cmu/assignment3-handout.git
```

Copy the `quadrotor_control`, `quadrotor_model`, and `utils`
directories from assignment 1 into `quadrotor_simulator_py`. This
assignment will refer to some of the classes defined in the prior
homework assignment (e.g., state.py which was given to you). You do
not need to have solved the previous assignment in order to do well on
this assignment.

```
cp -r /path/to/assignment1-handout/quadrotor_simulator_py/* assignment3-handout/quadrotor_simulator_py/
```

Next, you can either use the python environment you used for assignment 1 or
create a new one.

```
python3.8 -m venv .venv
```

Source the environment

```
source .venv/bin/activate
```

You will need to install the following dependencies:

```
pip install bresenham numpy matplotlib scikit-learn
```

## 1. 5th Order Polynomial Trajectory (40 points)
In this part of the homework you will implement the 5th order
polynomial trajectory with fixed initial and endpoint constraints
(i.e., position, velocity, and acceleration) as described in
[https://doi.org/10.1109/TRO.2015.2479878](https://doi.org/10.1109/TRO.2015.2479878).
You will also implement functions to evaluate the trajectories for a
particular derivative at a given time.

### 1.1 Coefficients for single axis trajectory (10 points)
You will write the single axis trajectory in `muellertrajectory.py`.
To test your solution, you can run `test/test_mueller_trajectory.py`.

### 1.2 Evaluating a single axis trajectory (10 points)
In this portion of the assignment you will implement the following
functions in `polynomialtrajectory.py`.

`derivative`, which returns the derivative of the coefficients
specified by order.

`evaluate`, which takes the derivative of the coefficients specified
by the input `order` and then evaluates them for time `time`.

`get_ref`, which returns the references up to the derivative
specified by order for the time specified by time.

To test your solution, you can run `test/test_polynomial_trajectory.py`.

### 1.3 Obtaining references for multi-axis trajectories (10 points)
You will need to implement the function `get_ref` in
`flatspacetrajectory.py`.  To test your solution, you can run
`test/test_flat_space_trajectory.py`. If your solution is correct, you should see the following output:

![Position](img/pos.png)

![Velocity](img/vel.png)

![Acceleration](img/acc.png)

![Yaw](img/yaw.png)

### 1.4 Managing multiple multi-axis trajectories (10 points)
Managing multiple multi-axis trajectories can be challenging, because
you need to manage the
To test your solution, you can run `test/test_multiflatspacetrajmanager.py`.

![Position](img/mpos.png)

![Velocity](img/mvel.png)

![Acceleration](img/macc.png)

## 2. Forward Arc Motion Primitives (40 points)
In this part of the homework you will implement the forward arc motion
primitives described in class.  To test your solution, you can run
`test/test_famp.py`. If your solution is correct,
you will see something similar to the output below.

![Forward Arc Motion Primitives](img/famp.png)

### 2.1 Coefficients for forward arc motion primitives (30 points)
You will calculate coefficients for the multi-axis forward arc
trajectory (x,y,z,yaw) in the `__init__` function of
`forwararctrajectory.py`.

### 2.2 Obtaining reference (10 points)
Derive the reference as a `State()` object in the `get_ref`
function of `forwardarctrajectory.py`. You may use functions
or classes from Part 1 of this assignment to make your life easier.

## 3. RRT (20 points)
You will implement a Rapidly Exploring Random Tree in `rrt.py`. A
collision checker is provided to you in `collision_checker.py`.
To test your solution, run `test_rrt.py`.
Your RRT will be displayed in mauve and the path from the start to
end point will be illustrated in cyan.

![Rapidly Exploring Random Tree](img/rrt.png)
