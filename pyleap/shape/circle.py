from pyglet import gl
from math import sin, cos, pi
from pyleap.shape.shape import Shape


class Circle(Shape):
    """ Circle """

    def __init__(self, x=100, y=100, r=30, color="orange"):
        super().__init__(x, y, color, gl=gl.GL_POLYGON)
        self.r = r
        self.update_points()

    def _update_points(self):
        n = 32
        d = pi * 2 / n
        x, y, r = self.x, self.y, self.r

        ps = []
        for i in range(n):
            ps += [(x + r * sin(d * i)), (y + r * cos(d * i))]
        self.points = tuple(ps)
