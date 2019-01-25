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
                font_size=16, color="orange", font_name=None):
        """ """
        self.text = pyglet.text.Label(text=src, font_size=font_size, font_name=font_name)
        super().__init__(x=x, y=y, h=font_size, color=color)
        self.w = self.text.content_width
        self.h = self.text.content_height

    def draw(self):
        self._before_draw()
        self.text.x = self.x
        self.text.y = self.y
        self.text.color = color_to_tuple(self.color)
        self.text.draw()
        self._after_draw()

    @property
    def src(self):
        return self.text.text

    @src.setter
    def src(self, src):
        self.text.text = src
        self.w = self.text.content_width

    @property
    def font_size(self):
        return self.text.font_size

    @font_size.setter
    def font_size(self, font_size):
        self.text.font_size = font_size
        self.w = self.text.content_width
        self.h = self.text.content_height 
