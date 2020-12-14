import pygame as pg
import asset_creator as ac
import button as but
from tkinter.filedialog import *


class SoftwareRender:
    def __init__(self):
        pg.init()
        self.window_width = 1000
        self.window_height = 700
        self.screen = pg.display.set_mode((self.window_width, self.window_height))
        self.FPS = 30
        self.clock = pg.time.Clock()
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.open_button = but.Button(self.screen, self.window_width // 2 - 50, self.window_height // 2,
                                      self.open_file_dialog, text="Open file",
                                      width=120,
                                      height=40, hover_color=self.white, clicked_color=self.white)

    def open_file_dialog(self):
        """Открывает диалоговое окно выбора имени файла и вызывает
        функцию считывания параметров системы небесных тел из данного файла.
        Считанные объекты сохраняются в глобальный список space_objects
        """
        in_filename = askopenfilename(filetypes=(("Text file", ".obj"),))
        a = ac.Soft(in_filename)
        a.run()

    def draw_interface(self):
        pg.draw.rect(self.screen, self.red, ([0, self.window_height - 100], [self.window_width, self.window_height]))
        self.open_button.draw()

    def run(self):
        """Главная функция главного модуля.
        """

        print('Modelling started!')
        pg.display.set_caption("3D Visualization")
        clock = pg.time.Clock()
        pg.display.update()

        while True:
            clock.tick(self.FPS)
            for event in pg.event.get():
                self.open_button.handle_event(event)
                if event.type == pg.QUIT:
                    exit()
            self.draw_interface()
            pg.display.update()
            self.screen.fill(self.black)


app = SoftwareRender()
app.run()
