"""
22/12/2021: Day_002 - Part 1

--- Day 2: Dive! ---
Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2
Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

"""

import utils
import pandas as pd

if __name__ == '__main__':

    # Read in as a df
    moves_df = pd.read_csv('Vehicle_Movements.txt', sep=' ', names=['direction', 'distance'])

    # Total Movement forward
    forward_move = moves_df[moves_df['direction'] == 'forward']['distance'].sum()

    # Total Movement down
    downwards_move = moves_df[moves_df['direction'] == 'down']['distance'].sum()

    # Total Movement Up
    up_move = moves_df[moves_df['direction'] == 'up']['distance'].sum()

    # Total Vertical Movement
    vertical_move = downwards_move - up_move

    print(f'The vertical position is {vertical_move}m and the horizon position is {forward_move}m')
    print(f'Therefore the answer is {vertical_move*forward_move}')

