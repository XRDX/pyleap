import pyglet
from pyglet import gl

from pyleap.transform import Transform
from pyleap.collision import collide, update_collision_rect
from pyleap.util import color_to_tuple, UpdateInfo


class Shape():
    """ base shape class """

    def __init__(self, x, y, color="orange", gl=gl.GL_LINE_LOOP, line_width=1, point_size=1):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.gl = gl
        self.transform = Transform()
        self.line_width = line_width
        self.point_size = point_size
        self.points = ()

    def draw(self):
        self.update_points()
        self.update_vertex_list()
        self.update_anchor()
        self.update_gl()
        self.vertex_list.draw(self.gl)

    def stroke(self):
        self.update_points()
        self.update_vertex_list()
        self.update_anchor()
        self.update_gl()
        self.vertex_list.draw(gl.GL_LINE_LOOP)

    def update_gl(self):
        gl.glLoadIdentity()
        gl.glLineWidth(self.line_width)
        gl.glPointSize(self.point_size)
        self.transform.update_gl()

    def update_points(self):
        """ translate shapes to points """
        pass

    def update_vertex_list(self):
        color = color_to_tuple(self.color)
        length = len(self.points) // 2
        self.vertex_list = pyglet.graphics.vertex_list(
            length,
            ('v2f', self.points),
            ('c4B'.format(len(color)), color * length))

    def collide(self, other_shape):
        return collide(self, other_shape)

    def update_anchor(self):
        t = self.transform
        update_collision_rect(self)
        if t.anchor_x_r != None and t.anchor_y_r != None:
            t.anchor_x = self.min_x + (self.max_x - self.min_x) * t.anchor_x_r
            t.anchor_y = self.min_y + (self.max_y - self.min_y) * t.anchor_y_r





