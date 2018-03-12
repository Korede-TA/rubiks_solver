import numpy as np

color_onehots = {
    "blue":     np.array([1, 0, 0, 0, 0, 0]),
    "red":      np.array([0, 1, 0, 0, 0, 0]),
    "white":    np.array([0, 0, 1, 0, 0, 0]),
    "yellow":   np.array([0, 0, 0, 1, 0, 0]),
    "green":    np.array([0, 0, 0, 0, 1, 0]),
    "orange":   np.array([0, 0, 0, 0, 0, 1]),
}

class Color:
    BLUE = color_onehots["blue"]
    RED = color_onehots["red"]
    WHITE = color_onehots["white"]
    YELLOW = color_onehots["yellow"]
    GREEN = color_onehots["green"]
    ORANGE = color_onehots["orange"]

class RubiksCube:
    def __init__(self):
        # preallocate cube
        self._cube = [[[]]*9]*6

    @property
    def cube(self):
        return self._cube

    @cube.setter
    def cube(self, value):
        for i in self._cube:
            for j in i:
                self._cube[i][j] = value[i][j]
        
    def move(self, face, row=None, column=None):
        # move a column or a row on a particular face

        if is not row or is not column:
            # check that row or column values are not None
            return

        pass

    def set_face(self, face, face_matrix):
        # set all the values on a face base on a 3*3 face matrix
        face

    def print_cube(self):
        pass
