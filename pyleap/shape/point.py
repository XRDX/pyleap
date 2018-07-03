from pyglet import gl
from pyleap.shape.circle import Shape

class Point(Shape):
    """ 点 Point """

    def __init__(self, x=100, y=100, color="orange", point_size=1):
        super().__init__(x, y, color, gl=gl.GL_POINTS)

        self.point_size = point_size # only for point

    def update_points(self):
        self.points = (self.x, self.y)
