""" 基本图形： 线段

包含2个点

属性：
points： （x1, y1, x2, y2）
"""
from pyleap.shape.shape import Shape
from pyglet import gl
import math


class Line(Shape):
    def __init__(self, x1=100, y1=100, x2=200, y2=200, line_width=1, color="orange"):
        """ 线段
        线段宽度： line_width， 默认为1
        颜色： color, 默认为"orange"
        """
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2
        super().__init__(x, y, color, gl=gl.GL_LINES, line_width=line_width)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


    def update_points(self):
        self.points = (self.x1, self.y1, self.x2, self.y2)

