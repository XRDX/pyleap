"""基本图形：椭圆

椭圆是以圆心为中心的多边形（72边形）的形式进行拟合
"""


from pyglet import gl
from math import sin, cos, pi, sqrt
from pyleap.shape.shape import Shape


class Ellipse(Shape):
    """ 基本图形：椭圆 Ellipse 
    """

    def __init__(self, x=100, y=100, r_x=50, r_y=30, color="orange"):
        """ 
        圆心： x、y,        默认为100, 100
        半径： r_x, r_y    默认为50, 30
        颜色： color,      默认为 "orange"
        """
        super().__init__(color, gl=gl.GL_POLYGON)
        self.x, self.y, self.r_x, self.r_y = x, y, r_x, r_y

    def update_points(self):
        """ 椭圆的近似图形：72边形 """
        n = max(8, min(72, int(2*sqrt(self.r_x+self.r_y))))
        d = pi * 2 / n
        x, y, r_x, r_y = self.x, self.y, self.r_x, self.r_y

        ps = []
        for i in range(n):
            ps += [(x + r_x * sin(d * i)), (y + r_y * cos(d * i))]
        self.points = tuple(ps)
