"""Test functions and their analytic gradients (Ch 4, written for Prob. 4.7)."""

import numpy as np


def f_ls(x):
    """Two-variable function of the line search examples (Ex. 4.8 / 4.9), section 4.3."""
    return (0.1 * x[0] ** 6 - 1.5 * x[0] ** 4 + 5 * x[0] ** 2
            + 0.1 * x[1] ** 4 + 3 * x[1] ** 2 - 9 * x[1] + 0.5 * x[0] * x[1])


def grad_f_ls(x):
    """Gradient of the two-variable function of the line search examples (Ex. 4.8 / 4.9), section 4.3."""
    return np.array([0.6 * x[0] ** 5 - 6 * x[0] ** 3 + 10 * x[0] + 0.5 * x[1],
                     0.4 * x[1] ** 3 + 6 * x[1] - 9 + 0.5 * x[0]])


def bean(x):
    """Bean function (Ex. 4.11 in the book's numbering)."""
    return (1 - x[0]) ** 2 + (1 - x[1]) ** 2 + 0.5 * (2 * x[1] - x[0] ** 2) ** 2

def grad_bean(x):
    """Gradient of the bean function (Ex. 4.11 in the book's numbering)."""
    return np.array([-2 * (1 - x[0]) - 2 * x[0] * (2 * x[1] - x[0] ** 2),
                     -2 * (1 - x[1]) + 2 * (2 * x[1] - x[0] ** 2)])


def rosenbrock(x):
    """n-dimensional Rosenbrock (D.1.2); x* = (1, ..., 1), f* = 0."""
    x = np.asarray(x, dtype=float)
    return np.sum(100 * (x[1:] - x[:-1] ** 2) ** 2 + (1 - x[:-1]) ** 2)

def grad_rosenbrock(x):
    """Gradient of the n-dimensional Rosenbrock (D.1.2); x* = (1, ..., 1), f* = 0."""
    x = np.asarray(x, dtype=float)
    grad = np.zeros_like(x)
    grad[0] = -400 * x[0] * (x[1] - x[0] ** 2) - 2 * (1 - x[0])
    for i in range(1, len(x) - 1):
        grad[i] = 200 * (x[i] - x[i - 1] ** 2) - 400 * x[i] * (x[i + 1] - x[i] ** 2) - 2 * (1 - x[i])
    grad[-1] = 200 * (x[-1] - x[-2] ** 2)
    return grad
