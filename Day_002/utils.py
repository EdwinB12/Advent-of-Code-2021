"""
Day 002 Utilities
"""


def read_depths():
    # Convert txt file into a list. Note the blank space has to be stripped off every line with rstrip
    with open('Vehicle_Movements.txt') as f:
        return [depth.rstrip() for depth in f.readlines()]
