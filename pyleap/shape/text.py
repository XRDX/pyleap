import pyglet
from pyleap.window import window
from pyleap.color import color_to_tuple
from pyleap.util import all_shapes

from pyleap.shape.rectangle import Rectangle


class Text(Rectangle):
    """ Text
    src: 文本内容
    font_size: 文字高度
    """

    def __init__(self, src, x=window.center_x, y=window.center_y,
                 font_size=16, color="orange"):
        """ """

        self.text = pyglet.text.Label(text=src, font_size=font_size)
        super().__init__(x=x, y=y, h=font_size, color=color)
        self.update_width()

    def draw(self):
        self.update_all()
        self.text.x = self.x
        self.text.y = self.y
        self.text.font_size = self.h
        self.text.color = color_to_tuple(self.color)
        self.text.draw()

    @property
    def src(self):
        return self.text.text

    @src.setter
    def src(self, src):
        self.text.text = src
        self.update_width()

    @property
    def font_size(self):
        return self.h

    @font_size.setter
    def font_size(self, font_size):
        self.h = font_size
        self.update_width()

    def update_width(self):
        self.w = self.h * len(self.src) * 0.618
    