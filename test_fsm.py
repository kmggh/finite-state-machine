#!/usr/bin/env python
# Copyright (C) 2014 by Ken Guyton.  All Rights Reserved.


"""Test a finite state machine."""

import fsm
import unittest

INPUT_VAL = '1'
LAST_OUTPUT = ('a', 'x')
OUTPUT_VAL = 'j'
NEXT_STATE = 'C'

LAST_OUTPUT2 = ('j', 'm')
OUTPUT_VAL2 = 'a'
NEXT_STATE2 = 'B'


class TestAction(unittest.TestCase):
  def setUp(self):
    self.action = fsm.Action(INPUT_VAL, LAST_OUTPUT, OUTPUT_VAL, NEXT_STATE)

  def test_create(self):
    self.assertNotEqual(self.action, None)
    self.assertEqual(self.action.output_val, 'j')
    self.assertEqual(self.action.next_state, 'C')

  def test_read(self):
    self.assertTrue(self.action.read('1', 'a'))
    self.assertTrue(self.action.read('1', 'x'))

    self.assertFalse(self.action.read('1', 'y'))
    self.assertFalse(self.action.read('2', 'a'))
    self.assertFalse(self.action.read('2', 'x'))

  def test_read_no_last_output(self):
    self.action = fsm.Action(INPUT_VAL, (), OUTPUT_VAL, NEXT_STATE)
    self.assertTrue(self.action.read('1', ''))
    self.assertTrue(self.action.read('1', 'a'))
    self.assertTrue(self.action.read('1', 'x'))
    self.assertTrue(self.action.read('1', 'z'))
    self.assertFalse(self.action.read('2', ''))


class TestState(unittest.TestCase):
  def setUp(self):
    self.action = fsm.Action(INPUT_VAL, LAST_OUTPUT, OUTPUT_VAL, NEXT_STATE)
    self.action2 = fsm.Action(INPUT_VAL, LAST_OUTPUT2, OUTPUT_VAL2,
                              NEXT_STATE2)
    self.state = fsm.State()

  def test_create(self):
    self.assertNotEqual(self.state, None)

  def test_add_actions(self):
    self.state.add_action(self.action)
    self.state.add_action(self.action2)

  def test_read(self):
    self.state.add_action(self.action)
    self.state.add_action(self.action2)

    self.assertEqual(self.state.get_action('1', 'a'), self.action)
    self.assertEqual(self.state.get_action('1', 'm'), self.action2)

    self.assertEqual(self.state.get_action('2', 'a'), None)
    self.assertEqual(self.state.get_action('1', 'z'), None)


if __name__ == '__main__':
  unittest.main()
