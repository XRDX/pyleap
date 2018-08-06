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
            x = sum(args[0: len(args)-1: 2]) / ((len(args) - 1) / 2)
            y = sum(args[1: len(args)-1: 2]) / ((len(args) - 1) / 2)

        else:
            color = "orange"
            x = sum(args[0: len(args): 2]) / (len(args) / 2)
            y = sum(args[1: len(args): 2]) / (len(args) / 2)


        super().__init__(x, y, color, gl=gl.GL_POLYGON)

        if isinstance(args[-1], str):
            self.points = args[0: len(args)-1]
        else:
            self.points = args

