import pyglet
from pyglet import gl

from pyleap.collision import CollisionMixin
from pyleap.util import color_to_tuple


class Shape(CollisionMixin):
    """ base shape class """

    def __init__(self, x, y, color, gl=gl.GL_LINE_LOOP):
        self._x = int(x)
        self._y = int(y)
        self._color = color
        self.gl = gl

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
        self.update_vertex_list()

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
        self.update_vertex_list()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
        self.update_vertex_list()

    def draw(self):
        self.vertex_list.draw(self.gl)

    def stroke(self):
        self.vertex_list.draw(gl.GL_LINE_LOOP)

    def update_vertex_list(self):
        color = color_to_tuple(self._color)
        points = self.points
        length = len(points) // 2
        self.vertex_list = pyglet.graphics.vertex_list(
            length,
            ('v2f', points),
            ('c{}B'.format(len(color)), color * length))

    def collide(self, shape):
        return collide(self, shape)

