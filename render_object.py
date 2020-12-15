import numpy as np
import pygame as pg
from numba import njit


@njit(fastmath=True)
def any_func(arr, a, b):
    return np.any((arr == a) | (arr == b))


class Object3D:
    """
    vertexes - вершины, faces - грани, middles - середины граней
    """

    def __init__(self, render, camera, vertexes='', faces=''):
        self.render = render
        self.camera = camera
        self.vertexes = vertexes
        self.faces = faces
        self.vertexes = np.array([np.array(v) for v in vertexes])
        self.faces = np.array([np.array(face) for face in faces])
        self.middles = np.array([np.ones(4) for i in range(len(self.faces))])
        for i in range(len(self.faces)):
            coord = 0
            for j in range(len(self.faces[i])):
                coord += self.vertexes[self.faces[i, j]] / (len(self.faces[i]))
            self.middles[i] = coord
        self.order = np.ones(len(self.faces))

    def get_render_order(self):
        cam_coords = np.tile(self.camera.position, (len(self.middles), 1))
        distances = self.middles - cam_coords
        distances = np.sqrt((distances * distances).sum(axis=1))
        return np.argsort(-distances)

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        """
        Функция проекции и отрисовки модели
        """
        vertexes = self.vertexes @ self.render.camera.camera_matrix()
        vertexes_neg_z = vertexes
        vertexes = vertexes @ self.render.projection.projection_matrix

        vertexes /= vertexes[:, -1].reshape(-1, 1)
        vertexes[(vertexes > 2) | (vertexes < -2)] = 100
        vertexes_screen_check = vertexes
        vertexes = vertexes @ self.render.projection.to_screen_matrix
        vertexes = vertexes[:, :2]
        render_order = self.get_render_order()

        for i in range(len(render_order)):
            if 100 in vertexes_screen_check[self.faces[render_order[i]]]:
                continue
            if (vertexes_neg_z[self.faces[render_order[i]]].reshape(-1)[2::4] < 0).any():
                continue
            polygon = vertexes[self.faces[render_order[i]]]
            pg.draw.polygon(self.render.screen, pg.Color('dark grey'), polygon)
            pg.draw.polygon(self.render.screen, pg.Color('dark red'), polygon, 3)
