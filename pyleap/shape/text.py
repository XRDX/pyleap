import pyglet
from pyleap.window import window
from pyleap.util import color2list


class Text(pyglet.text.Label):
    """ Text """

    def __init__(self, src, x=window.center_x, y=window.center_y, font_size=16, color="orange"):
        super().__init__(src, x=x, y=y, font_size=font_size)
        self.color = color2list(color)[1]