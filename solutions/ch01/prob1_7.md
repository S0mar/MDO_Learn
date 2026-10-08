# Problem 1.7

> System: quadcopter drone designed for maximum level-flight speed.

Problem statement: see book, Ch. 1.

## System description

a quadcopter with an aerodynamicaly shaped shell.

## Objective

minimize the aerodynamic drag coefficent Cl of the quadcopter.

## Design variables (with bounds and units)

distance of the rotorblades relative to the core of the frame [50mm, 150mm].
diameter of the shell [60mm, 130mm].
radius of the nose [20mm, 30mm].
length of the tail [40mm, 100mm]

## Constraints

lift constraint Cd stays constant at 1.4 (just a guess exact number not important)
weight under 1 kg

## Parameters (fixed)

power = 100 W
number of rotors = 4
weight without shell = 700 g
areal weight of the shell = 300g /m2

## Problem statement (standard form)

minimize Cd
by varying:
50mm <= dist of the rotorblades <= 150mm
60mm <= d shell <= 130mm
20mm <= r nose <= 30mm
40mm <= l tail <= 100mm
subject to:
Cd = 1.4
m <= 1kg

## Problem classification

Design variables: continuous
Constraints: Constrained
Smoothness: Continuous (just my guess, hard to know)
Linearity: Nonlinear
Modality: Multimodal
Convexity: Nonconvex
Stochasticity: Deterministic (the same input returns the same output)

Algorithm of choice: 
Convex? no
Discrete? no
Differntiable? yes
Unconstrained? no
Mutlimodal? yes
--> SQP with multistart

Order: Second
Search: Local
Algorithm: Mathematical
Function evaluation: Direct
Stocasticity: Deterministic
Time dependance: Static

## Critique

looks good to me.
