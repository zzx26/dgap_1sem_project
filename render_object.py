import numpy as np
import pygame as pg
import transformation_matrices as tm
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
        # вершины
        # FIXME принять во внимание формат записи даннных при написании ассет креатора
        self.vertexes = np.array([np.array(v) for v in vertexes])
        # грани; числа в кортежах - индексы элементов предыдущей переменной
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
        vertexes = self.vertexes @ self.render.camera.camera_matrix()
        vertexes_neg_z = vertexes
        vertexes = vertexes @ self.render.projection.projection_matrix
        # нормируем координаты
        vertexes /= vertexes[:, -1].reshape(-1, 1)
        # эта строчка удаляет вершины вне pov, возможно буду проблемы с полигонами
        # предроложительно надо добавить штуку, которая будет маркировать полигоны, которые полностью вне поля зрения
        # чтобы можно было их дал  ее не отрисовывать(например заменить координату на стринг)
        vertexes[(vertexes > 2) | (vertexes < -2)] = 100
        # преобразуем в координаты экрана
        vertexes_screen_check = vertexes
        vertexes = vertexes @ self.render.projection.to_screen_matrix
        # отсекаем z, w
        vertexes = vertexes[:, :2]
        # FIXME здесь будет все веселье с отрисовкой
        render_order = self.get_render_order()

        for i in range(len(render_order)):
            print(vertexes_neg_z[self.faces[render_order[i]]].reshape(-1)[2::4])
            if 100 in vertexes_screen_check[self.faces[render_order[i]]]:
                continue
            if (vertexes_neg_z[self.faces[render_order[i]]].reshape(-1)[2::4] < 0).any():
                print('t')
                continue
            polygon = vertexes[self.faces[render_order[i]]]
            pg.draw.polygon(self.render.screen, pg.Color('dark grey'), polygon)
            pg.draw.polygon(self.render.screen, pg.Color('dark red'), polygon, 3)

    # def translate(self, pos):
    #     self.vertexes = self.vertexes @ tm.translate(pos)
    #
    # def scale(self, scale_to):
    #     self.vertexes = self.vertexes @ tm.scale(scale_to)
    #
    # def rotate_x(self, angle):
    #     self.vertexes = self.vertexes @ tm.rotate_x(angle)
    #
    # def rotate_y(self, angle):
    #     self.vertexes = self.vertexes @ tm.rotate_y(angle)
    #
    # def rotate_z(self, angle):
    #     self.vertexes = self.vertexes @ tm.rotate_z(angle)
