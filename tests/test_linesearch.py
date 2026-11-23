import numpy as np
import pytest

from mdolib.linesearch import backtracking, bracketing_pinpointing
from mdolib.testfuncs import (
    bean,
    f_ls,
    grad_bean,
    grad_f_ls,
    grad_rosenbrock,
    rosenbrock,
)
from mdolib.utils import Counted

X0_LS = np.array([-1.25, 1.25])
P_LS = np.array([4.0, 0.75])


def _central_fd(f, x, h=1e-6):
    return np.array([(f(x + h * e) - f(x - h * e)) / (2 * h) for e in np.eye(len(x))])


@pytest.mark.parametrize(
    "f, grad, x",
    [
        (f_ls, grad_f_ls, X0_LS),
        (bean, grad_bean, np.array([-1.0, 2.0])),
        (rosenbrock, grad_rosenbrock, np.array([-1.2, 1.0, 0.7, 1.3, -0.4])),
    ],
)
def test_gradients_match_finite_differences(f, grad, x):
    assert np.allclose(grad(x), _central_fd(f, x), atol=1e-6)


def _strong_wolfe(f, grad, x, p, alpha, mu1, mu2):
    phi_0, dphi_0 = f(x), grad(x) @ p
    sufficient = f(x + alpha * p) <= phi_0 + mu1 * alpha * dphi_0
    curvature = abs(grad(x + alpha * p) @ p) <= -mu2 * dphi_0
    return sufficient and curvature


@pytest.mark.parametrize("alpha_init", [1.2, 0.05])
@pytest.mark.parametrize("mu2", [0.9, 0.1, 1e-3])
def test_bracketing_pinpointing_satisfies_strong_wolfe(alpha_init, mu2):
    alpha, _ = bracketing_pinpointing(f_ls, grad_f_ls, X0_LS, P_LS, alpha_init=alpha_init, mu2=mu2)
    assert _strong_wolfe(f_ls, grad_f_ls, X0_LS, P_LS, alpha, 1e-4, mu2)


def test_bracketing_pinpointing_on_bean():
    x, p = np.array([-1.0, 2.0]), np.array([-1.0, -1.0])
    alpha, _ = bracketing_pinpointing(bean, grad_bean, x, p, alpha_init=1.2)
    assert _strong_wolfe(bean, grad_bean, x, p, alpha, 1e-4, 0.9)


def test_backtracking_small_mu1():
    alpha, _ = backtracking(f_ls, grad_f_ls, X0_LS, P_LS, alpha_init=1.2, mu1=1e-4, rho=0.7)
    assert f_ls(X0_LS + alpha * P_LS) <= f_ls(X0_LS) + 1e-4 * alpha * grad_f_ls(X0_LS) @ P_LS


@pytest.mark.xfail(
    strict=True,
    reason="known bug (4.7 review): Armijo test uses the slope at the trial point, not at alpha=0",
)
def test_backtracking_large_mu1_satisfies_sufficient_decrease():
    mu1 = 0.5
    alpha, _ = backtracking(f_ls, grad_f_ls, X0_LS, P_LS, alpha_init=1.2, mu1=mu1, rho=0.7)
    assert f_ls(X0_LS + alpha * P_LS) <= f_ls(X0_LS) + mu1 * alpha * grad_f_ls(X0_LS) @ P_LS


def test_counted():
    g = Counted(f_ls)
    g(X0_LS)
    g(X0_LS)
    assert g.n == 2
