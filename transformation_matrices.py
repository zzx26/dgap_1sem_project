import math
import numpy as np


class Transformation:
    def __init__(self):
        self.ed_matrix = np.eye(4)

    def __call__(self, v_matrix):
        return v_matrix @ self.matrix


class Translate(Transformation):
    def __init__(self, pos):
        super().__init__()
        self.tx, self.ty, self.tz = pos
        self.matrix = self.ed_matrix @ np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [self.tx, self.ty, self.tz, 1]
        ])


class Rotate_x(Transformation):
    def __init__(self, a):
        super().__init__()
        self.a = a
        self.matrix = self.ed_matrix @ np.array([
            [math.cos(a), math.sin(a), 0, 0],
            [-math.sin(a), math.cos(a), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])


class Rotate_y(Transformation):
    def __init__(self, a):
        super().__init__()
        self.a = a
        self.matrix = self.ed_matrix @ np.array([
            [math.cos(a), 0, -math.sin(a), 0],
            [0, 1, 0, 0],
            [math.sin(a), 0, math.cos(a), 0],
            [0, 0, 0, 1]
        ])


class Rotate_z(Transformation):
    def __init__(self, a):
        super().__init__()
        self.a = a
        self.matrix = self.ed_matrix @ np.array([
            [math.cos(a), math.sin(a), 0, 0],
            [-math.sin(a), math.cos(a), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])


class Scale(Transformation):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.matrix = self.ed_matrix @ np.array([
            [n, 0, 0, 0],
            [0, n, 0, 0],
            [0, 0, n, 0],
            [0, 0, 0, 1]
        ])


# # пример
# r = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
#               (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)])
#
# s = Rotate_z(3)
# b = s(r)
# print(b)
