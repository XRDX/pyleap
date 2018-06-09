import pyglet
import util 
from math import sin, cos, pi

class Shape():
    """ base shape class """
    def __init__(self, color="orange", point_count=0, glType=pyglet.gl.GL_LINE_LOOP):
        self._color = color
        self.point_count = point_count
        self.glType = glType

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
        self.vertex_list.draw(self.glType)

    def stroke(self):
        self.vertex_list.draw(pyglet.gl.GL_LINE_LOOP)

    def collide(self, other):
        return False

    def update_vertex_list(self):
        fmt, color = util.color2list(self._color)
        self.vertex_list = pyglet.graphics.vertex_list(self.point_count,
            ('v2i', self.points),
            (fmt, color * self.point_count))

class Rectangle(Shape):

    def __init__(self, x=100, y=100, w=100, h=50, color="orange"):
        super().__init__(color, point_count=4, glType=pyglet.gl.GL_QUADS)
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self.update_vertex_list()
    
    @property
    def w(self):
        return self._w
    
    @w.setter
    def w(self, w):
        self._w = w
        self.update_vertex_list()

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        self._h = h
        self.update_vertex_list()

    @property
    def points(self):
        x = self._x
        y = self._y
        w = self._w
        h = self._h
        return (x, y, x+w, y, x+w, y+h, x, y+h)

class Line(Shape):
    def __init__(self, x1=100, y1=100, x2=200, y2=200, color="orange"):
        super().__init__(color, point_count=2, glType=pyglet.gl.GL_LINES)
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.update_vertex_list()

    @property
    def points(self):
        return (self._x1, self._y1, self._x2, self._y2)

class Triangle(Shape):
    """ Triangle """

    def __init__(self, x1=100, y1=100, x2=200, y2=150, x3=200, y3=100, color="orange"):
        super().__init__(color, point_count=3, glType=pyglet.gl.GL_TRIANGLES)
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._x3 = x3
        self._y3 = y3
        self.update_vertex_list()

    @property
    def points(self):
        return (self._x1, self._y1, self._x2, self._y2, self._x3, self._y3)

class Circle(Shape):
    """ Circle """
    def __init__(self, x=100, y=100, r=30, color="orange"):
        super().__init__(color, point_count=32, glType=pyglet.gl.GL_POLYGON)
        self._x = x
        self._y = y
        self._r = r

        self.update_vertex_list()

    @property
    def points(self):
        n = self.point_count
        d = pi * 2 / n
        x, y, r = self._x, self._y, self._r

        ps = []
        for i in range(n):
            ps += [int(x + r*sin(d*i)), int(y + r*cos(d*i))]

        return tuple(ps)
    