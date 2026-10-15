# Problem 3.1

Answer true or false and justify your answer.

## a. A model developed to perform well for analysis will always do well in a numerical optimization process.

false. many other aspects of the optimization can still result in a poor design. for example there can be many different local optima where the optimizer can get stuck or take a long time to converge.

## b. Modeling errors have nothing to do with computations.

false. they very much can be. for example in a FEM simulation if the mesh is too fine the results can get close to the lower limit of a floating point number where any changes will get truncated. or a huge stress singularity in an element will form where the solver can also run into trouble.

## c. Explicit and implicit equations can always be written in residual form.

true. explicit examples are trivial. an example of an implicit equation rewritten as a residual is the linear system provided in example 3.1 (page 49, 50) which is rewritten in example 3.2 (page 52)

## d. Subtractive cancellation is a type of roundoff error.

true. as stated on page 56. during subtraction where the two numbers are so close that their diference is below machince precision they cancel out to zero. this can cause problems.

## e. Programming errors can always be eliminated by carefully reading the code.

false. in therory this can be done but is extremly inefficient and time consuming. in practice one should always assume that the code has bugs. bugs can be found by testing the software and finding the cases where it breaks. many insights can be found by seeing the results of a buggy code executionm, way more than could otherwise be found by reading the code over and over.

## f. Quadratic convergence is only better than linear convergence if the asymptotic convergence error constant is less than or equal to one.

false. quadratic is better than linear when both have the same asymptotic convergence error. 

## g. Logarithmic scales are desirable when plotting convergence because they show errors of all magnitudes.

true. with linear scales its hard to see erros in two significant digits. but for a full convergece it makes sense to use log scaling to see the errors at all magnitudes

## h. Newton solvers always require a linear solver.

false. newton solvers solve a linear system which dont have to be solved with a linear solver. newtons mehtod is also commonly used for nonlinear equation solvers.

## i. Some linear iterative solvers can be used to solve nonlinear problems.

true. see newton based solvers

## j. Direct methods allow us to trade between computational cost and precision, whereas iterative methods do not.

false. the opposite is the case. iterative methods continously converge towards the result thus the computation can be stopped half way and we can still retrieve a (less accurate) result. direct methods compute the solution in one iteration. stopping the computation before it finished leaves no usable result. so the computation cannot be resumed later, it has to be restarted. 

## k. Newton's method requires the derivatives of all the state variables with respect to the residuals.

false. the derrivative can also be approximated using the finite differnces method (see eqation 3.25 on page 67).

## l. In the full-space optimization approach, the state variables become design variables, and the governing equations become constraints.

true. in a full space approach the optimizer directly controls the state variables. the governing equations get added to the constraints as equality constraints.
