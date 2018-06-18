from pyglet import gl
from pyleap.shape.circle import Shape

class Point(Shape):
    """ Point """

    def __init__(self, x=100, y=100, color="orange"):
        super().__init__(x, y, color, gl=gl.GL_POINTS)
        self.update_points()

    def _update_points(self):
        self.points = (self.x, self.y)
