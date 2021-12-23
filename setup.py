import os

for i in range(4, 26):
    directory = f'Day_{i:003}'
    os.mkdir(directory)

    with open(directory + '/part1.py', 'w') as fp:
        pass

    with open(directory + '/part2.py', 'w') as fp:
        pass
