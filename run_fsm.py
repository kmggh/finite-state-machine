#!/usr/bin/env python
# Copyright (C) 2014 by Ken Guyton.  All Rights Reserved.


"""Run a finite state machine.

Each action is defined by four components:

input_val:  The input read into the action.
last_output:  Valid last outputs (previous outputs) before this action.
output_val:  The output value this action outputs if the above match.
next_state: The name of the next state.
"""

from __future__ import print_function

import fsm
import sys

A_ACTION1 = ('1', (), 'm', 'B')

B_ACTION1 = ('2', ('j', 'm'), 'a', 'B')
B_ACTION2 = ('2', ('a', 'x'), 'j', 'C')
B_ACTION3 = ('1', (), '', 'A')

C_ACTION1 = ('1', (), 'x', 'A')
C_ACTION2 = ('2', (), '', 'B')

INPUT_VALS = ('1', '2', '1', '1', '2', '2', '2', '2', '1', '1', '2')


def create_states():
  """Define states and add the above actions."""

  states = {}
  states['A'] = fsm.State()
  states['A'].add_action(fsm.Action(*A_ACTION1))

  states['B'] = fsm.State()
  states['B'].add_action(fsm.Action(*B_ACTION1))
  states['B'].add_action(fsm.Action(*B_ACTION2))
  states['B'].add_action(fsm.Action(*B_ACTION3))

  states['C'] = fsm.State()
  states['C'].add_action(fsm.Action(*C_ACTION1))
  states['C'].add_action(fsm.Action(*C_ACTION2))

  return states


def dump(state, action):
  """Dump out information on a state and action."""

  print('State {0}'.format(state)),
  print('Action input {0} last_output {1} '.format(action.input_val,
                                                    action.last_output)),
  print('output_val {0} next_state {1}'.format(action.output_val,
                                               action.next_state))


def main():
  states = create_states()

  state = 'A'
  output_val = ''

  for input_val in INPUT_VALS:
    sys.stdout.write('State {0} '.format(state))
    sys.stdout.write('Input {0} '.format(input_val))
    action = states[state].get_action(input_val, output_val)

    if action is None:
      break

    if action.output_val:
      sys.stdout.write('Output {0}\n'.format(action.output_val))
      output_val = action.output_val
    # Else we just keep the old output_val for next time.

    state = action.next_state

  print('Done')


if __name__ == '__main__':
  main()
