import pyglet
from pyleap.window import window
from pyleap.util import color_to_tuple
from pyleap.collision import CollisionMixin


class Text(pyglet.text.Label, CollisionMixin):
    """ Text """

    def __init__(self, src, x=window.center_x, y=window.center_y, font_size=16, color="orange"):
        super().__init__(src, x=x, y=y, font_size=font_size)
        self.color = color_to_tuple(color)[1]

    @property
    def points(self):
        min_x = self.x
        min_y = self.y
        max_x = self.x + self.font_size * len(self.text) / 2
        max_y = self.y + self.font_size

        return (min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y)