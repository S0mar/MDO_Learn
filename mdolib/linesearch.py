"""Line searches from Sec. 4.3 (written for Prob. 4.7): backtracking and bracketing + pinpointing."""

import numpy as np


def backtracking(f, grad, x, p, alpha_init=1.0, mu1=1e-4, rho=0.7):
    """Backtracking line search to satisfy the Armijo condition (sufficient decrease)."""
    
    alpha = alpha_init
    alpha_list = [alpha]
    while f(x + alpha * p) > f(x) + mu1 * alpha * grad(x + alpha * p).dot(p):
        #while the function is aboce the sufficient decrease line, backtrack
        alpha *= rho
        alpha_list.append(alpha)
    return alpha, alpha_list


def _interpolate(alpha_low, alpha_high, phi_low, phi_high, grad_phi_low, grad_phi_high):
    """Cubic interpolation to find the minimum of a function in an interval."""
    betha1 = grad_phi_low + grad_phi_high - 3 * (phi_low - phi_high) / (alpha_low - alpha_high)
    betha2 = np.sign(alpha_high - alpha_low) * np.sqrt(betha1 ** 2 - grad_phi_low * grad_phi_high)
    alpha_p = alpha_high - (alpha_high - alpha_low) * (grad_phi_high + betha2 - betha1) \
        / (grad_phi_high - grad_phi_low + 2 * betha2)
    return alpha_p


def _pinpoint(f, grad, x, p, alpha_low, alpha_high, mu1, mu2):
    """Returns the step length and the pinpointing history [(alpha_low, alpha_high, alpha_p), ...]."""
    phi_0 = f(x)                # function value at the current point
    grad_phi_0 = grad(x).dot(p) # directional derivative at the current point
    phi_low = f(x + alpha_low * p)                # function value at the lower bound
    grad_phi_low = grad(x + alpha_low * p).dot(p) # directional derivative
    phi_high = f(x + alpha_high * p)                # function value at the upper bound
    grad_phi_high = grad(x + alpha_high * p).dot(p) # directional derivative

    history = []  # one entry per pinpointing iteration: interval and trial step
    k = 0
    while True:
        alpha_p = _interpolate(alpha_low, alpha_high, phi_low, phi_high, grad_phi_low, grad_phi_high)
        history.append((alpha_low, alpha_high, alpha_p))  # interval used and trial step found in it
        phi_p = f(x + alpha_p * p)                # function value at the minimum in the inteval        
        grad_phi_p = grad(x + alpha_p * p).dot(p) # directional derivative
        
        if phi_p > phi_0 + mu1 * alpha_p * grad_phi_0 or phi_p > phi_low:
            # if the function value is above the sufficient decrease line or above the lower bound value, then update the upper bound
            alpha_high = alpha_p
            phi_high = phi_p
            grad_phi_high = grad_phi_p
        else:
            if abs(grad_phi_p) <= - mu2 * grad_phi_0:
                # if the directional derivative is low enough we have a good step length
                return alpha_p, history
            elif grad_phi_p * (alpha_high - alpha_low) >= 0:
                # if the directional derivative is positve then update the upper bound to the lower bound
                # positive here means the slope is dereasing towards the lower bound
                alpha_high = alpha_low
                phi_high = phi_low
                grad_phi_high = grad_phi_low
            alpha_low = alpha_p
            phi_low = phi_p
            grad_phi_low = grad_phi_p

        if k > 100:
            raise RuntimeError("Pinpointing failed to converge after 100 iterations.")
        k += 1


def bracketing_pinpointing(f, grad, x, p, alpha_init=1.0, mu1=1e-4, mu2=0.9, sigma=2.0):
    """Returns alpha_star and a history dict:
    {"bracketing": [(alpha_1, alpha_2), ...], "pinpointing": [(alpha_low, alpha_high, alpha_p), ...]}"""
    alpha_1 = 0             # lower bound on the step length
    alpha_2 = alpha_init    # upper bound on the step length (and initial guess)
    
    phi_0 = f(x)                # function value at the current point
    grad_phi_0 = grad(x).dot(p) # directional derivative at the current point
    phi_1 = phi_0               # function value at the lower bound
    first = True

    bracket_history = []  # one entry per bracketing iteration: (alpha_1, alpha_2)

    while True: # infinte loop
        bracket_history.append((alpha_1, alpha_2))
        phi_2 = f(x + alpha_2 * p)                # calculate function value at upper bound
        grad_phi_2 = grad(x + alpha_2 * p).dot(p) # calculate directional derivative at upper bound

        if phi_2 > phi_0 + mu1 * alpha_2 * grad_phi_0 or (not first and phi_2 > phi_1):
            # if the upper bound value is above the min decrease line or above the lower bound value, then pinpoint
            alpha_star, pin_history = _pinpoint(f, grad, x, p, alpha_1, alpha_2, mu1, mu2)
            return alpha_star, {"bracketing": bracket_history, "pinpointing": pin_history}
        if abs(grad_phi_2) <= -mu2 * grad_phi_0:
            # if the directional derivative is low enough we have a good step length
            return alpha_2, {"bracketing": bracket_history, "pinpointing": []}
        elif grad_phi_2 >= 0:
            # if the directional derrivative is positive (and the previous condition was met) then we pinpoint
            alpha_star, pin_history = _pinpoint(f, grad, x, p, alpha_2, alpha_1, mu1, mu2)
            return alpha_star, {"bracketing": bracket_history, "pinpointing": pin_history}
        else:
            # up date lower and upper bounds and continue searching
            alpha_1 = alpha_2
            phi_1 = phi_2
            alpha_2 *= sigma
        first = False
