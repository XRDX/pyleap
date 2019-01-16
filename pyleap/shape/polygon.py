import math
import pyglet

from pyleap.shape.shape import Shape


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
            points = list(args[:len(args)-1])
        else:
            color = "orange"
            points = list(args)

        self._x = sum(points[::2]) / (len(points) // 2)
        self._y = sum(points[1::2]) / (len(points) // 2)
        self._move_x = 0
        self._move_y = 0

        super().__init__(color, gl=pyglet.gl.GL_POLYGON)
        self.points = self._points = points

    @property
    def x(self):
        return self._x + self._move_x
    
    @x.setter
    def x(self, x):
        self._move_x = x - self._x

    @property
    def y(self):
        return self._y + self._move_y
    
    @y.setter
    def y(self, y):
        self._move_y = y - self._y

    def update_points(self):
        if self._move_x==0 and self._move_y==0:
            self.points = self._points
            return

        ps = [self._move_x, self._move_y] * (len(self.points)//2)
        for i in range(len(ps)):
            ps[i] += self._points[i]
        
        self.points = tuple(ps)


class Triangle(Polygon):
    """ Triangle """

    def __init__(self, *args):
        super().__init__(*args)
        self.gl = pyglet.gl.GL_TRIANGLES
        