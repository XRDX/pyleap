from pyglet import gl
from pyleap.shape.circle import Shape


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