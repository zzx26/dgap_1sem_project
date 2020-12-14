import pygame as pg
from typing import Tuple, Callable
from pygame.font import SysFont


def _round_rect(surface, rect, color, radius=None):
    if not radius:
        pg.draw.rect(surface, color, rect)
        return

    radius = min(radius, rect.width / 2, rect.height / 2)

    r = rect.inflate(-radius * 2, -radius * 2)
    for corn in (r.topleft, r.topright, r.bottomleft, r.bottomright):
        pg.draw.circle(surface, color, corn, radius)
    pg.draw.rect(surface, color, r.inflate(radius * 2, 0))
    pg.draw.rect(surface, color, r.inflate(0, radius * 2))


class Button:
    def __init__(
            self,
            surface,
            x: int,
            y: int,
            click_handler: Callable = lambda: None,
            text="",
            width=0,
            height=0,
            color: Tuple[int] = None,
            border_width=0,
            hover_color=None,
            clicked_color=None,
            border_radius=0,
            font: pg.font.Font = None,
            font_color=None
    ):

        self.surface = surface
        self.x = x
        self.y = y
        self.click_handler = click_handler
        self.color = color or (224, 224, 224)
        self.border_width = border_width
        self.hover_color = hover_color
        self.clicked_color = clicked_color
        self.border_radius = border_radius
        self.text = text

        if font is None:
            self.font = SysFont('couriernew', 20)

        text_size = self.font.size(text)
        self.width = width or text_size[0] + self.border_width + 2
        self.height = height or text_size[1] + self.border_width + 2
        self.font_color = font_color or (0, 0, 0)

        self.hovered = False
        self.clicked = False
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def __repr__(self):
        return f'<Button "{self.text}" at ({self.x}, {self.y})>'

    def __contains__(self, point: Tuple[int]):
        return self.rect.collidepoint(point)

    def draw(self):
        color = self.color
        if self.clicked and self.clicked_color:
            color = self.clicked_color
        elif self.hovered and self.hover_color:
            color = self.hover_color

        if not self.border_width:
            _round_rect(self.surface, self.rect, color, self.border_radius)
        else:
            _round_rect(self.surface, self.rect, (0, 0, 0), self.border_radius)
            _round_rect(
                self.surface,
                self.rect.inflate(-self.border_width, -self.border_width),
                color,
                self.border_radius
            )
        text = self.font.render(self.text, 1, self.font_color)
        place = text.get_rect(center=self.rect.center)
        self.surface.blit(text, place)

    def handle_event(self, event):
        if event.type == pg.MOUSEMOTION:
            self.hovered = event.pos in self
        elif event.type == pg.MOUSEBUTTONDOWN and event.pos in self:
            self.clicked = True
            self.click_handler()
        elif event.type == pg.MOUSEBUTTONUP:
            self.clicked = False

    def handle_events(self, event_list):
        for event in event_list:
            self.handle_event(event)
