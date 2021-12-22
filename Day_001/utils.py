"""
Day 001 Utilities
"""


def read_depths():
    # Convert txt file into a list. Note the blank space has to be stripped off every line with rstrip
    with open('depth_measurements.txt') as f:
        return [int(depth.rstrip()) for depth in f.readlines()]
