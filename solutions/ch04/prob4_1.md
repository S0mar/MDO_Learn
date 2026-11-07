# Problem 4.1

Answer true or false and justify your answer.

## a. Gradient-based optimization requires the function to be continuous and infinitely differentiable.

false. infinite differentiability is not required. a analytic derrivative might be faster to compute but that requires differentiability (first and second order information) but not infinite differentiability.

## b. Gradient-based methods perform a local search.

true. a global search guarantees that the global optimum is found. this is not the case for gradient based methods as they only use local information.

## c. Gradient-based methods are only effective for problems with one minimum.

false. they are also effective in problems with multiple minima. a mutli start approach will detect strong local minima but that does not guarantee that the global minimum will be found.

## d. The dot product of $\nabla f$ with a unit vector $p$ yields the slope of the $f$ along the direction of $p$.

true. see definition in formula 4.6.  $\nabla f$ has to be transposed for the dot product to work.something similar can also be done with the hessian (4.13).

## e. The Hessian of a unimodal function is positive definite or positive semidefinite everywhere.

false. it can also be indefinite. on for a unimodal funciton with points where the hessian is indefinite ist the rosenbrock function

## f. Each column $j$ of the Hessian quantifies the rate of change of component $j$ of the gradient vector with respect to all coordinate directions $i$.

true. exaclty this is stated on page 86 when describing hessians

## g. If the function curvature at a point is zero in some direction, that point cannot be a local minimum.

false. if the slope is nonzero in one direction the point is not a minimum (4.19). the curvature H at a minimum must be positive or zero (positive semi definite). so the eigenvalues of H at the minimum x must be greater than or equal to 0. these conditions are however not sufficient (only nessesary). if the curvature is 0 we dont know if it is the point is a minimum (unless we check the third order term). this kind of minimum is called a weak minimum. at a strong minimum the curvature is positive in all directions (all eigenvalues are greater than 0, H is positive difinite). the gradient being 0 and H being positive definite are the sufficient optimality conditions.

## h. A globalization strategy in a gradient-based algorithm ensures convergence to the global minimum.

false. globalization only means making an algorithm robust enough to converge to a local minimum from any starting point

## i. The goal of the line search is to find the minimum along a given direction.

false. the goal of a line search is how far to go in a specified search direction. the length is not nessecarily on the optimum along that line. the goal is to find a point that is "good enough".

## j. For minimization, the line search must always start in a descent direction.

true. this guarantees that f is reduced in that step as stated on page 98. the sufficient-decrease condition ensures that the next point is always lower than the last.

## k. The direction in the steepest-descent algorithm for a given iteration is orthogonal to the direction of the previous iteration.

false. only if we assume exact linesearch and we have the optimal value $\alpha$ for each iteration is the statement true (page 112 and 113). because at the optimal $\alpha$ the gradient in the search direction is 0 and therefore the steepest gradient for the next iteration has to be orthogonal to the previous one. for non exact line search (Wolfe) the next search direction is not guaranteed to be orthogonal.

## l. Newton's method is not affected by problem scaling.

true. as stated in page 121 newtons method is scale invariant. this means the number of steps until convergence is not influenced by scaling the variables. however step lenghts, trust region radii, tolerances for convergence are still scale dependent.

## m. Quasi-Newton methods approximate the function Hessian by using gradients.

true. the computation of the hessian can get very expensive with many variables. so in quasi newton methods we use gradients from past iterations to build an approximated hessian. the hessian is updated each iteration using the secant condition. this requires less computation at the cost of lower accuracy of the hessian.

## n. Newton's method is a good choice among gradient-based methods because it uses exact second-order information and therefore converges well from any starting point.

false. for example not every step results in a function decrease as the hessian can be indefinite or negative definite when the current point is far form a solution. it can also overshoot the minimum in the search direction. the curvature form the hessisan provides a useful starting point for the step lenght but refining it using line search is reccomended. and even if both of these things are accounted for, computing the exact hessian (second order information) is very inefficient. but it is a better choice than steepest decent. 

## o. The trust-region method does not require a line search.

true. step acceptance is decided by the actual reduction / predicted reduction =  r value. step lenght and direction are decided are not decided by line search. line search CAN be used in trust-region methods but it is not required
