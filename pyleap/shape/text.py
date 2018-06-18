import pyglet
from pyleap.window import window
from pyleap.util import color_to_tuple
from pyleap.shape.shape import Shape


class Text(Shape):
    """ Text """

    def __init__(self, text, x=window.center_x, y=window.center_y, font_size=16, color="orange"):
        super().__init__(x, y, color)
        color = color_to_tuple(color)
        self.text = pyglet.text.Label(text=text, x=x, y=y, font_size=font_size, color=color)

    def update_points(self):
        min_x = self.x
        min_y = self.y
        max_x = self.x + self.font_size * len(self.text) / 2
        max_y = self.y + self.font_size

        self.points = (min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y)

    def draw(self):
        self.text.draw()
