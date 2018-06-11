import pyglet
from pyglet import gl
from math import sin, cos, pi

from pyleap.util import color2list
from pyleap.collision import collide
from pyleap.window import window
from pyleap.resource import rss


class Shape():
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
        fmt, color = color2list(self._color)
        self.vertex_list = pyglet.graphics.vertex_list(
            self.len,
            ('v2i', self.points),
            (fmt, color * self.len))

    @property
    def len(self):
        return len(self.points) // 2

    def collide(self, shape):
        return collide(self, shape)


class Point(Shape):
    """ Point """

    def __init__(self, x=100, y=100, color="orange"):
        super().__init__(x, y, color, gl=gl.GL_POINTS)


class Rectangle(Shape):
    """ Rectangle """

    def __init__(self, x=100, y=100, w=100, h=50, color="orange"):
        super().__init__(x, y, color, gl=gl.GL_QUADS)
        self._w = int(w)
        self._h = int(h)
        self.update_vertex_list()

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, w):
        self._w = int(w)
        self.update_vertex_list()

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        self._h = int(h)
        self.update_vertex_list()

    @property
    def points(self):
        x = self._x
        y = self._y
        w = self._w
        h = self._h
        return (x, y, x + w, y, x + w, y + h, x, y + h)


class Line(Shape):
    def __init__(self, x1=100, y1=100, x2=200, y2=200, lineWidth=1, color="orange"):
        x = (x1 + x2) // 2
        y = (y1 + y2) // 2
        super().__init__(x, y, color, gl=gl.GL_LINES)
        self._x1 = int(x1)
        self._y1 = int(y1)
        self._x2 = int(x2)
        self._y2 = int(y2)
        self._lineWidth = lineWidth

        self.update_vertex_list()

    @property
    def points(self):
        return (self._x1, self._y1, self._x2, self._y2)


class Triangle(Shape):
    """ Triangle """

    def __init__(self, x1=100, y1=100, x2=200, y2=150, x3=200, y3=100,
                 color='orange'):
        x = (x1 + x2 + x3) // 2
        y = (y1 + y2 + y3) // 2
        super().__init__(x, y, color, gl=gl.GL_TRIANGLES)
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
        super().__init__(x, y, color, gl=gl.GL_POLYGON)
        self._r = r

        self.update_vertex_list()

    @property
    def points(self):
        n = 32
        d = pi * 2 / n
        x, y, r = self._x, self._y, self._r

        ps = []
        for i in range(n):
            ps += [int(x + r * sin(d * i)), int(y + r * cos(d * i))]
        return tuple(ps)


class Sprite(pyglet.sprite.Sprite):
    """ Sprite """

    def __init__(self, src, x=window.center_x, y=window.center_y):
        self.img = pyglet.image.load(rss.get(src))
        self.center_image()
        super().__init__(img=self.img, x=x, y=y)

    def center_image(self):
        """Sets an image's anchor point to its center"""
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2

    @property
    def points(self):
        min_x = self.x - self.img.anchor_x
        min_y = self.y - self.img.anchor_y
        max_x = self.x + self.img.width - self.img.anchor_x
        max_y = self.y + self.img.width - self.img.anchor_y

        return (min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y)

    def collide(self, shape):
        return collide(self, shape)


class Text(pyglet.text.Label):
    """ Text """

    def __init__(self, src, x=window.center_x, y=window.center_y, font_size=16, color="orange"):
        super().__init__(src, x=x, y=y, font_size=font_size)
        self.color = color2list(color)[1]
