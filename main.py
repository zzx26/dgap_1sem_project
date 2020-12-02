import pygame as pg
import render_object as ro
import camera as c
import projection as p


class SoftwareRender:
    def __init__(self):
        pg.init()
        self.resolution = self.width, self.height = 800, 600
        self.h_width, self.h_height = self.width // 2, self.height // 2
        self.FPS = 25
        self.screen = pg.display.set_mode(self.resolution)
        self.clock = pg.time.Clock()
        self.create_objects()

    def draw(self):
        """method that will create an actual image"""
        self.screen.fill(pg.Color('cyan'))
        self.object.draw()

    def run(self):
        """working cycle of the game"""
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            current_fps = 'Current FPS: ' + str(self.clock.get_fps())
            pg.display.set_caption(current_fps)
            pg.display.flip()
            self.clock.tick(self.FPS)

    def create_objects(self):
        self.camera = c.Camera(self, [0.5, 1.5, -2])
        self.projection = p.Projection(self)
        self.object = ro.Object3D(self)


if __name__ == '__main__':
    app = SoftwareRender()
    app.run()
