from pyleap.shape.shape import Shape
from pyglet import gl
import math


class Line(Shape):
    def __init__(self, x1=100, y1=100, x2=200, y2=200, line_width=1, color="orange"):
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2
        super().__init__(x, y, color, gl=gl.GL_LINES, line_width=line_width)
        self.points = (x1, y1, x2, y2)

