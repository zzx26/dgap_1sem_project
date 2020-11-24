import numpy as np
import pygame as pg
import transformation_matrices as tm


class Object3D:
    def __init__(self, render):
        self.render = render
        # вершины
        # FIXME принять во внимание формат записи даннных при написании ассет креатора
        self.vertexes = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 0, 1),
                                  (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)])
        # грани; числа в кортежах - индексы элементов предыдущей переменной
        # FIXME придумать, как перегнать грани в покрашенные полигоны при отрисовке
        self.faces = np.array([(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (2, 3, 7, 6), (1, 2, 6, 5), (0, 3, 7, 4)])

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        vertexes = self.vertexes @ self.render.camera.camera_matrix()
        vertexes = vertexes @ self.render.projection.projection_matrix
        # нормируем координаты
        vertexes /= vertexes[:, -1].reshape(-1, 1)
        # эта строчка удаляет вершины вне pov, возможно буду проблемы с полигонами
        # предроложительно надо добавить штуку, которая будет маркировать полигоны, которые полностью вне поля зрения
        # чтобы можно было их далее не отрисовывать(например заменить координату на стринг)
        # vertexes[(vertexes > 2) | (vertexes < -2)] = 0
        vertexes = vertexes @ self.render.projection.to_screen_matrix
        vertexes = vertexes[:, :2]
        # FIXME здесь будет все веселье с отрисовкой
        for face in self.faces:
            polygon = vertexes[face]
            pg.draw.polygon(self.render.screen, pg.Color('red'), polygon, 3)

        # подсвечивает точки фигур
        for vertex in vertexes:
            #FIXME жуткий костыль, который сожрет всю память(почему то выдает флоат)
            vertex = [int(i) for i in vertex]
            pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 6)

    def translate(self, pos):
        self.vertexes = self.vertexes @ tm.translate(pos)

    def scale(self, scale_to):
        self.vertexes = self.vertexes @ tm.scale(scale_to)

    def rotate_x(self, angle):
        self.vertexes = self.vertexes @ tm.rotate_x(angle)

    def rotate_y(self, angle):
        self.vertexes = self.vertexes @ tm.rotate_y(angle)

    def rotate_z(self, angle):
        self.vertexes = self.vertexes @ tm.rotate_z(angle)