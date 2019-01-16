import pyglet
from pyleap.shape.shape import Shape

__all__ = ['Point']


class Point(Shape):
    """ 点 Point """

    def __init__(self, x=100, y=100, color="orange", point_size=1):
        super().__init__(color, gl=pyglet.gl.GL_POINTS)
        self.x = x
        self.y = y
        self.point_size = point_size # only for point

    def update_points(self):
        self.points = (self.x, self.y)
