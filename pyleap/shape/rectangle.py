from pyglet import gl
from pyleap.shape.circle import Shape


class Rectangle(Shape):
    """ Rectangle """

    def __init__(self, x=100, y=100, w=100, h=50, color="orange"):
        super().__init__(x, y, color, gl=gl.GL_QUADS)
        self.w = w
        self.h = h

    def _update_points(self):
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        self.points = (x, y, x + w, y, x + w, y + h, x, y + h)
