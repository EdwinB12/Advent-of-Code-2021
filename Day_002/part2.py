"""
22/12/2021: Day_002 - Part 2

--- Part Two ---
Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine manual and discover that the process is actually slightly more complicated.

In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.
Again note that since you're on a submarine, down and up do the opposite of what you might expect: "down" means aiming in the positive direction.

Now, the above example does something different:

forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
down 5 adds 5 to your aim, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
up 3 decreases your aim by 3, resulting in a value of 2.
down 8 adds 8 to your aim, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

"""

import utils
import pandas as pd
import matplotlib.pyplot as plt


class SubMarine:

    def __init__(self):
        self.x = 0
        self.z = 0
        self.aim = 0
        self.x_history = []
        self.z_history = []
        self.aim_history = []
        self.command_history = []
        self.value_history = []

    def down(self, value):
        self.aim += value
        self.update_histories(command='down', value=value)

    def up(self, value):
        self.aim += -value
        self.update_histories(command='up', value=value)

    def forward(self, value):
        self.x += value
        self.z += (self.aim * value)
        self.update_histories(command='forward', value=value)

    def update_histories(self, command, value):
        self.x_history.append(self.x)
        self.z_history.append(self.z)
        self.aim_history.append(self.aim)
        self.command_history.append(command)
        self.value_history.append(value)

    def summary(self):
        print(f'X position is {self.x}')
        print(f'Z position is {self.z}')
        print(f'Aim position is {self.aim}')

    def answer(self):
        print(f'The answer is {self.z * self.x}')

    def plot_x(self):
        plt.plot(self.x_history)
        plt.show()

    def plot_z(self):
        plt.plot(self.z_history)
        plt.show()


if __name__ == '__main__':

    # Read in as a df
    moves_df = pd.read_csv('Vehicle_Movements.txt', sep=' ', names=['direction', 'value'])
    print(len(moves_df))
    submarine = SubMarine()

    for direction, value in zip(moves_df['direction'], moves_df['value']):

        if direction == 'forward':
            submarine.forward(value)
        elif direction == 'up':
            submarine.up(value)
        elif direction == 'down':
            submarine.down(value)
        else:
            raise ValueError(f'Direction must be one of "forward", "up" or "down". {direction} is not accepted')

    submarine.summary()
    submarine.answer()






