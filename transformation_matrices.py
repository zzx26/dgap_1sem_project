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


class RotateX(Transformation):
    def __init__(self, a):
        super().__init__()
        self.a = a
        self.matrix = self.ed_matrix @ np.array([
            [1, 0, 0, 0],
            [0, np.cos(a), np.sin(a), 0],
            [0, -np.sin(a), np.cos(a), 0],
            [0, 0, 0, 1]
        ])


class RotateY(Transformation):
    def __init__(self, a):
        super().__init__()
        self.a = a
        self.matrix = self.ed_matrix @ np.array([
            [np.cos(a), 0, -np.sin(a), 0],
            [0, 1, 0, 0],
            [np.sin(a), 0, np.cos(a), 0],
            [0, 0, 0, 1]
        ])


class RotateZ(Transformation):
    def __init__(self, a):
        super().__init__()
        self.a = a
        self.matrix = self.ed_matrix @ np.array([
            [np.cos(a), np.sin(a), 0, 0],
            [-np.sin(a), np.cos(a), 0, 0],
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
