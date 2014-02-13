Finite State Machine Problem
============================



Ken Guyton<br>
Wed 2014-02-12 17:02:45 -0500<br>



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


To Run
------

    ./run_fsm.py


Results
-------

From running it.

    ./run_fsm.py
    State A Input 1 Output m
    State B Input 2 Output a
    State B Input 1 State A Input 1 Output m
    State B Input 2 Output a
    State B Input 2 Output j
    State C Input 2 State B Input 2 Output a
    State B Input 1 State A Input 1 Output m
    State B Input 2 Output a
    Done


