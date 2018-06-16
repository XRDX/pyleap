from pyleap.shape.shape import Shape
from pyglet import gl
import math


class Line(Shape):
    def __init__(self, x1=100, y1=100, x2=200, y2=200, lineWidth=1, color="orange"):
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2
        super().__init__(x, y, color, gl=gl.GL_QUADS)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.lineWidth = lineWidth

    def _update_points(self):
        dx = (self.y2-self.y1) * self.lineWidth / self.length / 2
        dy = (self.x1-self.x2) * self.lineWidth / self.length / 2
        self.points = (self.x1 - dx, self.y1 - dy,
                    self.x1 + dx, self.y1 + dy,
                    self.x2 + dx, self.y2 + dy,
                    self.x2 - dx, self.y2 - dy)

    @property
    def length(self):
        return math.sqrt((self.x1-self.x2)*(self.x1-self.x2) \
                        +(self.y1-self.y2)*(self.y1-self.y2))
