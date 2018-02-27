class Pizza(object):

    def __init__(self, config, grid):
        self.rows = config[0]
        self.cols = config[1]
        self.min_ingredients = config[2]
        self.max_total = config[3]
        self.grid = grid

    def get_grid(self):
        return self.grid

    def print_config(self):
        print(self.rows, self.cols, self.min_ingredients, self.max_total)
