# Problem 4.1

Answer true or false and justify your answer.

## a. Gradient-based optimization requires the function to be continuous and infinitely differentiable.

false. infinite differentiability is not required. a gradient of the function can be obtained through the finite difference method. a analytic derrivative might be faster to compute but that requires differentiability (first ans second order information) but not infinite differentiability. continutiy is prefered for stability but not required.

## b. Gradient-based methods perform a local search.

true. a global search guarantees that the global optimum is found. this is not the case for gradient based methods

## c. Gradient-based methods are only effective for problems with one minimum.

false. they are also effective in problems with multiple minima. a mutli start approach will detect strong local minima.

## d. The dot product of $\nabla f$ with a unit vector $p$ yields the slope of the $f$ along the direction of $p$.

true. see definition in formula 4.6.  $\nabla f$ has to be transposed for the dot product to work.something similar can also be done with the hessian (4.13)

## e. The Hessian of a unimodal function is positive definite or positive semidefinite everywhere.

false. for example the neagtive definite plot shown on the right in Fig. 4.11 is unimodal but the hessian is negative definite at the maximum. however if a unimodal function has a strong or a weak minium then we can say that the hessian is positive definite or positve semidefinite everywhere.

## f. Each column $j$ of the Hessian quantifies the rate of change of component $j$ of the gradient vector with respect to all coordinate directions $i$.

true. exaclty this is stated on page 86 when describing hessians

## g. If the function curvature at a point is zero in some direction, that point cannot be a local minimum.

false. if the slope is 0 in one direction the point is not a minimum (4.19). the curvature H at a minimum must be positive or zero (positive semi definite). so the eigenvalues of H at the minimum x must be greater than or equal to 0. these conditions are however not sufficient (only nessesary). if the curvature is 0 we dont know if it is the point is a minimum (unless we check the third order term). this kind of minimum is called a weak minimum. at a strong minimum the curvature is positive in all directions (all eigenvalues are greater than 0, H is positive difinite). the gradient being 0 and H being positive definite are the sufficient optimality conditions.

## h. A globalization strategy in a gradient-based algorithm ensures convergence to the global minimum.

false. globalization only means making an algorithm robust enough to converge to a local minimum from any starting point

## i. The goal of the line search is to find the minimum along a given direction.

false. the goal of a line search is forst to find a search direction and then determining how far to go in that direction. the length of that step is not nessecarily on the optimum along that line. the goal is to find a point that is "good enough".

## j. For minimization, the line search must always start in a descent direction.

true. this guarantees that f is reduced in that step as stated on page 98. while the line search should not spend too much time finding the optimum along the search direction it should still make sure that the next point is lower than the current one.

## k. The direction in the steepest-descent algorithm for a given iteration is orthogonal to the direction of the previous iteration.

true. but only if we assume exact linesearch so we have the optimal value $\alpha$ for each iteration (page 112 and 113). because at the optimal $\alpha$ the gradient in the search direction is 0 and therefore the steepest gradient for the next iteration has to be orthogonal to the previous one.

## l. Newton's method is not affected by problem scaling.

true. as stated in page 121 newtons method is scale invariant. this means the number of steps until convergence is not influenced by scaling the variables.

## m. Quasi-Newton methods approximate the function Hessian by using gradients.

true. the computation of the hessian can get very expensive with many variables. so in quasi newton methods we use gradients from past iterations to build an approximated hessian. this requires less computation at the cost of lower accuracy of the hessian.

## n. Newton's method is a good choice among gradient-based methods because it uses exact second-order information and therefore converges well from any starting point.

false. for example not every step results in a function decrease. it can also overshoot the minimum in the search direction. the curvature form the hessisan provides a useful starting point for the step lenght but refining it using line search is reccomended. and even if both of these things are accounted for, computing the exact hessian (second order information) is very inefficient. but it is a better choice than steepest decent. 

## o. The trust-region method does not require a line search.

false. a line search can still be used when minimizing the model within the trust region. 
