import pyglet
from pyglet import gl

from pyleap.transform import TransformMixin
from pyleap.collision import CollisionMixin
from pyleap.util import color_to_tuple, UpdateInfo


class Shape(TransformMixin, CollisionMixin):
    """ base shape class """

    def __init__(self, x, y, color, gl=gl.GL_LINE_LOOP):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.gl = gl

    def draw(self):
        self.update_vertex_list()
        self.vertex_list.draw(self.gl)

    def stroke(self):
        self.update_vertex_list()
        self.vertex_list.draw(gl.GL_LINE_LOOP)

    def update_points(self):
        self._update_points()
        self.update_colision_rect()
        self.update_real_points()

    def update_real_points(self):
        self.real_points = ()
        ps = self.points
        for i in range(0, len(ps), 2):
            self.real_points += self.get_real_point(ps[i], ps[i+1])

    def update_vertex_list(self):
        self.update_points()
        color = color_to_tuple(self.color)
        length = len(self.points) // 2
        self.vertex_list = pyglet.graphics.vertex_list(
            length,
            ('v2f', self.real_points),
            ('c4B'.format(len(color)), color * length))





