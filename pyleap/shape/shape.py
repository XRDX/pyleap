""" 基本图形类 Shape

所有图形都继承与Shape，Shape拥有以下两个主要的属性
1. Collision，主要用于检测碰撞以及点击事件
2. Transform，用于图形的变换处理

"""

import pyglet
import math

from pyleap.transform import Transform, TransformMixin
from pyleap.collision import CollisionMixin
from pyleap.color import color_to_tuple
from pyleap.util import all_shapes, all_right_shapes, null


class Shape(CollisionMixin, TransformMixin):
    """ base shape class """


    def __init__(self, color="orange", gl=pyglet.gl.GL_LINE_LOOP,
                 line_width=1):
        """ 默认参数
        颜色 color: "orange"
        线条粗细 line_width： 1
        """
        self.color = color
        self.gl = gl
        self.transform = Transform()

        # 图形的线条宽度，默认为1
        self.line_width = line_width

        # 图形的顶点 (Point1, Point2, ...)
        self.points = ()

        # 用于记录press事件函数
        self._press = null
        self._right_press = null

        # 仅Point类point_size属性有效
        self.point_size = 1

        # 透明度 opacity
        self.opacity = 1

    def draw(self):
        """ 使用draw方法将图形绘制在窗口里 """
        self._before_draw()
        self.vertex_list.draw(self.gl)
        self._after_draw()
    
    def _after_draw(self):
        """ reset gl """
        pyglet.gl.glLoadIdentity()  # reset gl
        pyglet.gl.glLineWidth(1)

    def stroke(self):
        """ 使用stroke方法将图形绘制在窗口里，仅对基本的几何图形有效 """
        self._before_draw()
        length = len(self.points)
        
        # thick lines
        # if self.line_width == 1:
        #     if length==4:
        #         self.vertex_list.draw(pyglet.gl.GL_LINES)
        #     elif length > 4:
        #         self.vertex_list.draw(pyglet.gl.GL_LINE_LOOP)
        #     return

        # 
        color = color_to_tuple(self.color, self.opacity)
        if length == 4:
            x, y, x1, y1 = self.points[0:4]
            l = max(1, math.sqrt((x1-x)*(x1-x)+(y1-y)*(y1-y)))
            ly = (x1-x) / l * self.line_width / 2
            lx = - (y1-y) / l * self.line_width / 2

            points = [x-lx, y-ly, x+lx, y+ly, x1+lx, y1+ly, x1-lx, y1-ly]

            vertex_list = pyglet.graphics.vertex_list(
                4,
                ('v2f', points),
                ('c4B', color * 4))
            vertex_list.draw(pyglet.gl.GL_QUADS)

        elif length > 4:
            points = []
            for i in range(0, length, 2):
                x, y = self.points[i], self.points[i+1]
                x1, y1 = self.points[i-2], self.points[i-1]
                x2, y2 = self.points[(i+2) % length], self.points[(i+3) % length]

                l1 = max(1, math.sqrt((x1-x)*(x1-x)+(y1-y)*(y1-y)))
                l2 = max(1, math.sqrt((x2-x)*(x2-x)+(y2-y)*(y2-y)))

                nx1, ny1 = (x - x1) / l1, (y - y1) / l1
                nx2, ny2 = (x - x2) / l2, (y - y2) / l2
                nx, ny = nx1 + nx2, ny1 + ny2
                vx, vy = -ny1, nx1

                t = nx1*nx2 + ny1*ny2
                if t > 0.99:
                    lx = vx * self.line_width / 2
                    ly = vy * self.line_width / 2
                    points += [x-lx, y-ly, x+lx, y+ly, x+lx, y+ly, x-lx, y-ly]
                elif t < -0.99:
                    lx = vx * self.line_width / 2
                    ly = vy * self.line_width / 2
                    points += [x+lx, y+ly, x-lx, y-ly]
                else:
                    radio = 1/(vx*nx + vy*ny)
                    if radio < 0: 
                        radio = -radio

                    lx = (nx1+nx2) * self.line_width / 2 * radio
                    ly = (ny1+ny2) * self.line_width / 2 * radio
                    points += [x+lx, y+ly, x-lx, y-ly]

            batch = pyglet.graphics.Batch()
            for i in range(0, len(points), 4):
                batch.add(4, pyglet.gl.GL_QUADS, None,
                    ('v2f', (points[i-4], points[i-3], points[i-2], points[i-1],
                        points[i+2], points[i+3], points[i], points[i+1])),
                    ('c4B', color * 4))

            batch.draw()

        self._after_draw()

    def _before_draw(self):
        """ 在绘制之前，针对形变进行计算，通过设置openGL的属性来达到绘制出变形的图形 """
        self.update_points()
        self.update_vertex_list()
        self.update_anchor()

        pyglet.gl.glLoadIdentity()  # reset gl
        pyglet.gl.glLineWidth(self.line_width)
        pyglet.gl.glPointSize(self.point_size)
        self.transform.update_gl()

        # handle shapes click envets
        all_shapes.discard(self)
        if(self._press != None):
            all_shapes.add(self)

        all_right_shapes.discard(self)
        if(self._right_press != None):
            all_right_shapes.add(self)  

    def update_points(self):
        """ translate shapes to points，在子类中实现 """
        pass

    def update_vertex_list(self):
        """ 使用pyglet来绘制基本图形之前，转为pyglet识别的属性 """
        color = color_to_tuple(self.color, self.opacity)
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

__all__ = ["Shape"]