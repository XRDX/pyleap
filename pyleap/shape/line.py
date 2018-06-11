from pyleap.shape.shape import Shape
from pyglet import gl

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
