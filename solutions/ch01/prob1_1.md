# Problem 1.1

## a. MDO arose from the need to consider multiple design objectives.

false. it arose from single objective problems that had multiple constraints.

## b. The preliminary design phase takes place after the conceptual design phase. 

true. the order is conceptual -> preliminary -> final design.

## c. Design optimization is a completely automated process from which designers can expect to get their final design

false. after each run the enginner should take a look at the result and reevaluate the optimization. if there are any new insights like a constraint that can be changed to allow for more designspace near the optimum the optimization should be restarted.

## d. The design variables for a problem consist of all the inputs needed to compute the objective and constraint functions.

true? with the design variables you can compute the objective and the constraints.

## e. The design variables must always be independent of each other.

true. otherwise there can infinite combinations of variables that yield an optimal solution which results in poor optimizer performance. or even a failed optimization.

## f. An optimization algorithm designed for minimization can be used to maximize an objective function without modifying the algorithm.

true. unless mutliplying the objective with -1 counts as a modification to the algorithm.

## g. Compared with the global optimum of a given problem, adding more design variables to that problem results in a global optimum that is no worse than that of the original problem.

true. but only if the constraints stay the same and the function is deterministic. with a stochastic funtion this might not be the case.

## h. Compared with the global optimum objective value of a given problem, adding more constraints sometimes results in a better global optimum.

false. more constraints can either not change the value. this might be the case if the new constraint is redundand or doesnt cover the optimum. otherwise the constraint can only reduce the size of the design space and thus result in a worse optimum objective value.

## i. A function is 𝐶 1 continuous if its derivative varies continuously.

true. C0 has a non continuous derrivative. C2 has a continuous second derrivative.

## j. All unimodal functions are convex.

False. all convex function are unimodal but not all unimodal are convex.

## k. Global search algorithms always converge to the global optimum.

false. this is not guaranteed

## l. Gradient-based methods are largely based on mathematical principles as opposed to heuristics. 

True. the algorithm itself is based on mathematical principles. but some values of the parameters in these algorithms might be based on prior experience and not mathematical principles.

## m. Solving a problem that involves a stochastic model requires a stochastic optimization algorithm. 

False. surrogate models allow for deterministic algorithms to be used with stochastic models

## n.  If a problem is multimodal, it requires a gradient-free optimization algorithm. 

False. gradient based algorithms can still find the optimum but there is still a chance that the get stuck in a local minimum. 
