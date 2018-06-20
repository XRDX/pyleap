import pyglet
from pyleap.window import window
from pyleap.color import color_to_tuple
from pyleap.util import all_shapes

from pyleap.shape.rectangle import Rectangle


class Text(Rectangle):
    """ Text """

    def __init__(self, text, x=window.center_x, y=window.center_y,
                 font_size=16, color="orange"):

        self.text = pyglet.text.Label(text=text, font_size=font_size)
        super().__init__(x=x, y=y, w=font_size*len(text)*0.6, h=font_size, color=color)

    def draw(self):
        self.update_all()
        self.text.x = self.x
        self.text.y = self.y
        self.text.color = color_to_tuple(self.color)
        self.text.draw()
