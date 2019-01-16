import pyglet
from pyleap.shape.shape import Shape


class Rectangle(Shape):
    """ 长方形： Rectangle
    """

    def __init__(self, x=100, y=100, w=100, h=50, color="orange"):
        """ 长方形
        左下角顶点的位置： x, y
        宽度： w
        高度： h
        颜色： color 默认为 "orange"
        """
        super().__init__(color, gl=pyglet.gl.GL_QUADS)
        self.x, self.y, self.w, self.h = x, y, w, h

    def update_points(self):
        """ 统一变为多个点组成的多边形，用于处理碰撞 """
        x, y, w, h = self.x, self.y, self.w, self.h
        self.points = (x, y, x + w, y, x + w, y + h, x, y + h)
