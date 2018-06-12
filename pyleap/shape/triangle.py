from pyglet import gl
from pyleap.shape.circle import Shape


class Triangle(Shape):
    """ Triangle """

    def __init__(self, x1=100, y1=100, x2=200, y2=150, x3=200, y3=100,
                 color='orange'):
        x = (x1 + x2 + x3) / 3
        y = (y1 + y2 + y3) / 3
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