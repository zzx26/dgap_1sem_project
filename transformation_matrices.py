import math
import numpy as np


def translate(pos):
    """changes the position of an object, pos - 3 num tuple"""
    tx, ty, tz = pos
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [tx, ty, tz, 1]
    ])


def rotate_x(a):
    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(a), math.sin(a), 0],
        [0, -math.sin(a), math.cos(a), 0],
        [0, 0, 0, 1]
    ])


def rotate_y(a):
    return np.array([
        [math.cos(a), 0, -math.sin(a), 0],
        [0, 1, 0, 0],
        [math.sin(a), 0, math.cos(a), 0],
        [0, 0, 0, 1]
    ])


def rotate_z(a):
    return np.array([
        [math.cos(a), math.sin(a), 0, 0],
        [-math.sin(a), math.cos(a), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def scale(n):
    return np.array([
        [n, 0, 0, 0],
        [0, n, 0, 0],
        [0, 0, n, 0],
        [0, 0, 0, 1]
    ])

class Translate:
    def __init__(self, vertexes, matrx, tx, ty, tz, tr):
        self.vertexes = vertexes
        self.matrx = matrx
        self.tx = tx
        self.ty = ty
        self.tz = tz
        self.tr = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [tx, ty, tz, 1]
        ])

    def __call__(self, pos):
        self.tx, self.ty, self.tz = pos
        vertexes = self.matrx @ self.tr
        return vertexes


class Rotate_x:
    def __init__(self, vertexes, matrx, a, rt):
        self.vertexes = vertexes
        self.matrx = matrx
        self.a = a
        self.rt = np.array([
            [math.cos(a), math.sin(a), 0, 0],
            [-math.sin(a), math.cos(a), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    def __call__(self, al):
        self.a = al

        global matrx



class Rotate_y:
    def __init__(self, matrx):
        self.matrx = matrx

    def __call__(self, a):
        global matrx
        matrx = self.matrx @ np.array([
            [math.cos(a), 0, -math.sin(a), 0],
            [0, 1, 0, 0],
            [math.sin(a), 0, math.cos(a), 0],
            [0, 0, 0, 1]
        ])


class Rotate_z:
    def __init__(self, matrx):
        self.matrx = matrx

    def __call__(self, a):
        global matrx
        matrx = self.matrx @ np.array([
            [math.cos(a), math.sin(a), 0, 0],
            [-math.sin(a), math.cos(a), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])


class Scale:
    def __init__(self, matrx):
        self.matrx = matrx

    def __call__(self, n):
        global matrx
        matrx = self.matrx @ np.array([
            [n, 0, 0, 0],
            [0, n, 0, 0],
            [0, 0, n, 0],
            [0, 0, 0, 1]
        ])

