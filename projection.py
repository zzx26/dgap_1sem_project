import numpy as np


class Projection:
    def __init__(self, render):
        near = render.camera.near_plane
        far = render.camera.far_plane
        right = np.tan(render.camera.h_fov / 2)
        left = -right
        top = np.tan(render.camera.v_fov / 2)
        bottom = -top

        a00 = 2 / (right - left)
        a11 = 2 / (top - bottom)
        a22 = (far + near) / (far - near)
        a32 = -2 * near * far / (far - near)
        self.projection_matrix = np.array([
            [a00, 0, 0, 0],
            [0, a11, 0, 0],
            [0, 0, a22, 1],
            [0, 0, a32, 0]
        ])

        HW, HH = render.h_width, render.h_height
        self.to_screen_matrix = np.array([
            [HW, 0, 0, 0],
            [0, -HH, 0, 0],
            [0, 0, 1, 0],
            [HW, HH, 0, 1]
        ])