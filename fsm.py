#!/usr/bin/env python
# Copyright (C) 2014 by Ken Guyton.  All Rights Reserved.

"""A simple finite state machine for a particular problem."""


class Action(object):
  """An action for a particular input for a state."""

  def __init__(self, input_val, last_output, output_val, next_state):
    """Initialize the particular action.

    Args:
      input_val: str. This action occurs if the input is this particular
        value.
      last_output: tuple of str.  And this action occurs if the last
        output value (printed) was in this tuple.  Can be empty ().
      output_val: str.  If the two conditions are met, output this value.
        Can be an empty str.
      next_state:  str.  The name of the next state to proceed to.
    """

    self.input_val = input_val
    self.last_output = last_output
    self.output_val = output_val
    self.next_state = next_state

  def read(self, input_val, last_output):
    """Read an input and evaluate it.  If  matches, set other values.

    Args:
      input_val: str. The input value into this action.
      last_output: str. The last value printed.

    Returns:
      A bool which is True if the input val matches the input_val of this
      action.  AND if there is a last_output tuple of values, if the
      last_output is one of those.  If the last_output tuple is empty,
      then any last_output value is okay if the input_val matches.
    """

    if input_val == self.input_val:
      if self.last_output:
        return last_output in self.last_output
      else:
        return True
    else:
      return False


class State(object):
  """Represent a state that can have a number of actions."""

  def __init__(self):
    """Initialize the actions list."""

    self.actions = []

  def add_action(self, action):
    """Add an action to this state.

    Args:
      action: An Action object.
    """

    self.actions.append(action)

  def get_action(self, input_val, last_output):
    """Retrieve an action that matches the input value and last output.

    Args:
      input_val: str. The input value into this action.
      last_output: str. The last value printed.
    Returns:
      The first action object that has matching parameters.  If no action
      matches, returns None.
    """

    for action in self.actions:
      if action.read(input_val, last_output):
        return action

    return None
