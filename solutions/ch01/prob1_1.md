# Problem 1.1

## a.

false. it arose from single objective problems that had multiple constraints.

## b.

true. the order is conceptual -> preliminary -> final design.

## c.

false. after each run the enginner should take a look at the result and reevaluate the optimization. if there are any new insights like a constraint that can be changed to allow for more designspace near the optimum the optimization should be restarted.

## d.

true? with the design variables you can compute the objective and the constraints.

## e.

true. otherwise there can infinite combinations of variables that yield an optimal solution which results in poor optimizer performance. or even a failed optimization.

## f.

true. unless mutliplying the objective with -1 counts as a modification to the algorithm.

## g.

true. but only if the constraints stay the same and the function is deterministic. with a stochastic funtion this might not be the case.

## h.

false. more constraints can either not change the value. this might be the case if the new constraint is redundand or doesnt cover the optimum. otherwise the constraint can only reduce the size of the design space and thus result in a worse optimum objective value.

## i.

true. C0 has a non continuous derrivative. C2 has a continuous second derrivative.

## j.

False. all convex function are unimodal but not all unimodal are convex.

## k.

false. this is not guaranteed

## l.

True. the algorithm itself is based on mathematical principles. but some values of the parameters in these algorithms might be based on prior experience and not mathematical principles.

## m.

False. surrogate models allow for deterministic algorithms to be used with stochastic models

## n.

False. gradient based algorithms can still find the optimum but there is still a chance that the get stuck in a local minimum. 
