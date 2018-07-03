""" 基本图形类 Shape

所有图形都继承与Shape，Shape拥有以下两个主要的属性
1. Collision，主要用于检测碰撞以及点击事件
2. Transform，用于图形的变换处理

"""

import pyglet
from pyglet import gl

from pyleap.transform import Transform, TransformMixin
from pyleap.collision import CollisionMixin
from pyleap.color import color_to_tuple
from pyleap.util import all_shapes


class Shape(CollisionMixin, TransformMixin):
    """ base shape class """

    def __init__(self, x, y, color="orange", gl=gl.GL_LINE_LOOP,
                 line_width=1):
        """ 默认参数
        颜色 color: "orange"
        线条粗细 line_width： 1
        """
        self.x = x
        self.y = y
        self.color = color
        self.gl = gl
        self.transform = Transform()

        # 图形的线条宽度，默认为1
        self.line_width = line_width

        # 图形的近似多边形 (x1, y1, x2, y2, ...)
        self.points = ()

        # 用于记录press事件函数
        self._press = None

        # 仅Point类point_size属性有效
        self.point_size = 1

    def draw(self):
        """ 使用draw方法将图形绘制在窗口里 """
        self.update_all()
        self.vertex_list.draw(self.gl)

    def stroke(self):
        """ 使用stroke方法将图形绘制在窗口里，仅对基本的几何图形有效 """
        self.update_all()
        self.vertex_list.draw(gl.GL_LINE_LOOP)

    def update_all(self):
        """ 在绘制之前，针对形变进行计算，通过设置openGL的属性来达到绘制出变形的图形 """
        self.update_points()
        self.update_vertex_list()
        self.update_anchor()

        gl.glLoadIdentity() # reset gl
        gl.glLineWidth(self.line_width)
        gl.glPointSize(self.point_size)
        self.transform.update_gl()

        # handle shapes click envets
        all_shapes.discard(self)
        all_shapes.add(self)     


    def update_points(self):
        """ translate shapes to points，在子类中实现 """
        pass

    def update_vertex_list(self):
        """ 使用pyglet来绘制基本图形之前，转为pyglet识别的属性 """
        color = color_to_tuple(self.color)
        length = len(self.points) // 2
        self.vertex_list = pyglet.graphics.vertex_list(
            length,
            ('v2f', self.points),
            ('c4B', color * length))

    def update_anchor(self):
        """ 如果是使用set_anchor_rate来设定锚点，那么就需要不停的更新锚点的位置 """
        t = self.transform
        self.update_collision_rect()
        if t.anchor_x_r and t.anchor_y_r:
            t.anchor_x = self.min_x + (self.max_x - self.min_x) * t.anchor_x_r
            t.anchor_y = self.min_y + (self.max_y - self.min_y) * t.anchor_y_r

    