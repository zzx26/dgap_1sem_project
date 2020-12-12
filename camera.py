import numpy as np
import pygame as pg
import transformation_matrices as tm


class Camera:
    def __init__(self, render, position):
        self.render = render
        self.position = np.array([*position, 1.0])
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])
        self.h_fov = np.pi / 3
        self.v_fov = self.h_fov * (render.height / render.width)
        self.near_plane = 0.1
        self.far_plane = 100
        self.moving_speed = 0.03
        self.rotation_speed = 0.02
        self.yaw_positive_matrix = tm.Rotate_y(self.rotation_speed)
        self.yaw_negative_matrix = tm.Rotate_y(-self.rotation_speed)
        self.pitch_positive_matrix = tm.Rotate_x(self.rotation_speed)
        self.pitch_negative_matrix = tm.Rotate_x(-self.rotation_speed)

    def control(self):
        key = pg.key.get_pressed()
        if key[pg.K_w]:
            self.position += self.forward * self.moving_speed
        if key[pg.K_a]:
            self.position -= self.right * self.moving_speed
        if key[pg.K_s]:
            self.position -= self.forward * self.moving_speed
        if key[pg.K_d]:
            self.position += self.right * self.moving_speed
        if key[pg.K_q]:
            self.position += self.up * self.moving_speed
        if key[pg.K_e]:
            self.position -= self.up * self.moving_speed
        if key[pg.K_j]:
            self.camera_yaw_negative()
        if key[pg.K_l]:
            self.camera_yaw_positive()
        if key[pg.K_i]:
            self.camera_pitch_negative()
        if key[pg.K_k]:
            self.camera_pitch_positive()

    def camera_yaw_positive(self):
        self.forward = self.yaw_positive_matrix(self.forward)
        self.right = self.yaw_positive_matrix(self.right)
        self.up = self.yaw_positive_matrix(self.up)

    def camera_yaw_negative(self):
        self.forward = self.yaw_negative_matrix(self.forward)
        self.right = self.yaw_negative_matrix(self.right)
        self.up = self.yaw_negative_matrix(self.up)

    def camera_pitch_positive(self):
        self.forward = self.pitch_positive_matrix(self.forward)
        self.right = self.pitch_positive_matrix(self.right)
        self.up = self.pitch_positive_matrix(self.up)

    def camera_pitch_negative(self):
        self.forward = self.pitch_negative_matrix(self.forward)
        self.right = self.pitch_negative_matrix(self.right)
        self.up = self.pitch_negative_matrix(self.up)

    def translate_matrix(self):
        """переход в систему координат камеры"""
        x, y, z, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])

    def camera_matrix(self):
        return self.translate_matrix() @ self.rotate_matrix()
