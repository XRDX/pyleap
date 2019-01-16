"""基本图形：圆

圆是以圆心为中心的正多边形（正72边形）的形式进行拟合
"""

import pyglet
from math import sin, cos, pi, sqrt
from pyleap.shape.shape import Shape


class Circle(Shape):
    """ 基本图形：圆 Circle 
    """

    def __init__(self, x=100, y=100, r=30, color="orange"):
        """ 
        圆心： x、y,    默认为100, 100
        半径： r，     默认为30
        颜色： color,  默认为 "orange"
        """
        super().__init__(color, gl=pyglet.gl.GL_POLYGON)
        self.x, self.y, self.r = x, y, r

    def update_points(self):
        """ 圆的近似图形：正多边形 """
        n = max(8, min(72, int(4*sqrt(self.r))))

        d = pi * 2 / n
        x, y, r = self.x, self.y, self.r

        ps = []
        for i in range(n):
            ps += [(x + r * sin(d * i)), (y + r * cos(d * i))]
        self.points = tuple(ps)
