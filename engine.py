import pygame as pg
import render_object as ro
import camera as c
import projection as p
import button as but


class Soft:
    def __init__(self, file_name):
        pg.init()
        self.file_name = file_name
        self.resolution = self.width, self.height = 1000, 700
        self.h_width, self.h_height = self.width // 2, self.height // 2
        self.FPS = 25
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.screen = pg.display.set_mode(self.resolution)
        self.stop_program = False
        self.clock = pg.time.Clock()
        self.create_objects()
        self.close_button = but.Button(self.screen, self.width // 2 + 100, self.height // 2 + 200,
                                       self.close_program, text="Close",
                                       width=120,
                                       height=40, hover_color=self.white, clicked_color=self.red)

    def close_program(self):
        self.stop_program = True

    def draw(self):
        """method that will create an actual image"""
        self.screen.fill(pg.Color('cyan'))
        self.object.draw()
        self.close_button.draw()

    def create_objects(self):
        self.camera = c.Camera(self, [-5, 6, -50])
        self.projection = p.Projection(self)
        self.object = self.get_objects_from_file(self.file_name)

    def get_objects_from_file(self, filename):
        self.camera = c.Camera(self, [-5, 6, -50])
        vertexes, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertexes.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return ro.Object3D(self, camera=self.camera, vertexes=vertexes, faces=faces)

    def run(self):
        """working cycle of the game"""
        while True:
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                self.close_button.handle_event(event)
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            current_fps = 'Current FPS: ' + str(self.clock.get_fps())
            pg.display.set_caption(current_fps)
            pg.display.flip()
            self.clock.tick(self.FPS)

            if self.stop_program:
                break


if __name__ == '__main__':
    eng = Soft()
    eng.run()
