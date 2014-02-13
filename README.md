Finite State Machine Problem
============================



Ken Guyton
Wed 2014-02-12 17:02:45 -0500



From an email message from Kirk on a finite state machine
problem. 

Here's the input:

Input values:

1, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2


The state machine was a picture but here's my summary of it.

Start = A

A:
in = 1:  print m
goto B

B: 
in = 2 and last printed j or m:  print a
goto B

in = 2 and last printed a or x:  print j
goto C

in = 1: 
goto A

C: 
in = 1:  print x
goto A

in = 2:
goto B

