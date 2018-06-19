from pyglet import gl
from pyleap.shape.shape import Shape


class Triangle(Shape):
    """ Triangle """

    def __init__(self, x1=100, y1=100, x2=200, y2=150, x3=200, y3=100,
                 color='orange'):
        x = (x1 + x2 + x3) / 3
        y = (y1 + y2 + y3) / 3
        super().__init__(x, y, color, gl=gl.GL_TRIANGLES)
        self.points = (x1, y1, x2, y2, x3, y3)


