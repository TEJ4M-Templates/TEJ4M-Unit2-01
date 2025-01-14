#!/usr/bin/env python3
"""
Created by: Mr. Coxall
Created on: Sept 2020
This is "Turing Machine" program that accepts the state machine rules
    and the initial "tape" and then runs
"""

import time
from Tape import Tape
from TuringMachine import TuringMachine

# state machine
#                    ↓ current state
#                         ↓ value read
#                                 ↓ state you become
#                                       ↓ value to write to Tape
#                                            ↓ direction to move
state_machine = {("init","0"):("init", "1", "R"),
                 ("init","1"):("init", "0", "R"),
                 ("init"," "):("final"," ", "N"),
                }

# initial tape
#                  ↓ initial tape values
t = TuringMachine("010011001 ", 
                  initial_state = "init",
                  final_states = {"final"},
                  transition_function = state_machine)

print("Input on Tape:\n              " + t.get_tape())
print("              ▲" + "\n")

original_tape = t.get_tape()

while not t.final():
    t.step()

print("\nResult of the Turing machine calculation:")
print("Original tape: " + original_tape)
print("Final tape   : " + t.get_tape())

print("\nDone.")
