from pyglet import gl
from pyleap.shape.shape import Shape
import math

class Polygon(Shape):
    """
    多边形：Polygon
    """
    def __init__(self, *args):

        """ 多边形

            颜色： color 默认为 "orange"
        """

        if isinstance(args[-1], str):
            color = args[-1]
            points = args[:len(args)-1]

        else:
            color = "orange"
            points = args

        x = sum(points[::2]) / (len(points) / 2)
        y = sum(points[1::2]) / (len(points) / 2)

        super().__init__(x, y, color, gl=gl.GL_POLYGON)

        self.points = points