import math
import numpy as np


class Pizza(object):

    def __init__(self, config, matrix):
        self.rows = config[0]
        self.cols = config[1]
        self.min_ingredients = config[2]
        self.max_total = config[3]
        self.matrix = matrix

    def get_grid(self):
        return self.grid

    def print_config(self):
        print(self.rows, self.cols, self.min_ingredients, self.max_total)

    def divide(self):
        result = []
        step = int(math.sqrt(self.max_total))
        for i in range(0, self.rows, step):
            result.append([sub[i:i + step] for sub in self.get_grid()[i:i + step]])
        return result
