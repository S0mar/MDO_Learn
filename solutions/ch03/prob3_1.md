# Problem 3.1

Answer true or false and justify your answer.

## a. A model developed to perform well for analysis will always do well in a numerical optimization process.

false. many other aspects of the optimization can still result in a poor design. for example the gradients may still be hard to compute because the model is noisy or not smooth. in some cases the model may fail from extreme inputs.

## b. Modeling errors have nothing to do with computations.

true. modeling errors come form idealizations of the mathematical models. they can affect the accuracy of the outcome. modeling errors affect how vaild the answer is.

## c. Explicit and implicit equations can always be written in residual form.

true. explicit examples are trivial. an example of an implicit equation rewritten as a residual is the linear system provided in example 3.1 (page 49, 50) which is rewritten in example 3.2 (page 52). one examples: explicit f(x) = 0 becomes r(x) = f(x) - u = 0 in residual form. impicit: Au = b becomes r(x) = Au - b = 0.

## d. Subtractive cancellation is a type of roundoff error.

true. as stated on page 56. during subtraction where the two numbers are so close that their diference is below machince precision they cancel out to zero. this can cause problems. more generally subtraction amplifies the roundoff in the operands. so not only subtractions below machine precision are affected.

## e. Programming errors can always be eliminated by carefully reading the code.

false. one should always assume that the code has bugs. bugs can be found by testing the software and finding the cases where it breaks. many insights can be found by seeing the results of a buggy code executionm, way more than could otherwise be found by reading the code over and over.

## f. Quadratic convergence is only better than linear convergence if the asymptotic convergence error constant is less than or equal to one.

false. as long as 0 < yk < 1 quadractic converges and beats linear.

## g. Logarithmic scales are desirable when plotting convergence because they show errors of all magnitudes.

true. with linear scales its hard to see errors in two significant digits. but for a full convergence it makes sense to use log scaling to see the errors at all magnitudes

## h. Newton solvers always require a linear solver.

true. linear solver is required (page 74).

## i. Some linear iterative solvers can be used to solve nonlinear problems.

true. see for example gauss-seidel solvers. fixed point iteration sovlers can be adapted to solve nonlinear problems.

## j. Direct methods allow us to trade between computational cost and precision, whereas iterative methods do not.

false. the opposite is the case. iterative methods continously converge towards the result thus the computation can be stopped half way and we can still retrieve a (less accurate) result. direct methods compute the solution in one iteration. stopping the computation before it finished leaves no usable result. so the computation cannot be resumed later, it has to be restarted. 

## k. Newton's method requires the derivatives of all the state variables with respect to the residuals.

false. the explicit equations/functions of the derrivatives are not required. the derrivative can also be approximated using the secant method (see eqation 3.25 on page 67). however a derrivative function or an appoximate derrivative is always required.

## l. In the full-space optimization approach, the state variables become design variables, and the governing equations become constraints.

true. in a full space approach the optimizer directly controls the state variables. the governing equations get added to the constraints as equality constraints.
