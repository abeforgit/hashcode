import numpy as np

"""
Utilities for parsing the input files
"""

from .pizza import Pizza


class Parser(object):

    def __init__(self, filepath):
        self.path = filepath

    def make_pizza(self):
        with open(self.path) as file:
            nums = {
                "T": 1,
                "M": 0
            }
            grid = [list(line.rstrip('\n')) for line in file]
            config = [int(num) for num in grid.pop(0) if num.isnumeric()]

            for index, line in enumerate(grid):
                grid[index] = ([nums[char] for char in line])
            matrix = np.matrix(grid)

        return Pizza(config, matrix)



