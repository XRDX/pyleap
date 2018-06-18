import pyglet
from pyglet import gl

from pyleap.resource import rss
from pyleap.window import window

from pyleap.transform import Transform
from pyleap.collision import collide, update_collision_rect
from pyleap.util import color_to_tuple, UpdateInfo


class Sprite(pyglet.sprite.Sprite):
    """ Sprite """

    def __init__(self, src, x=window.center_x, y=window.center_y):

        self.img = pyglet.image.load(rss.get(src))
        self.center_image()

        super().__init__(img=self.img, x=x, y=y)

        self.points = ()
        self.transform = Transform()

    def center_image(self):
        """Sets an image's anchor point to its center"""
        self.img.anchor_x = self.img.width // 2 # int
        self.img.anchor_y = self.img.height // 2 # int

    def update_points(self):
        w = self.img.width
        h = self.img.height
        a_x = self.img.anchor_x
        a_y = self.img.anchor_y

        min_x = self.x - a_x * self.scale_x * self.scale
        min_y = self.y - a_y * self.scale_y * self.scale
        max_x = self.x + (w - a_x) * self.scale_x * self.scale
        max_y = self.y + (h - a_y) * self.scale_y * self.scale
        self.points = (min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y)

    def draw(self):
        self.update_points()
        self.update_anchor()
        self.update_gl()
        super().draw()

    def update_anchor(self):
        t = self.transform
        update_collision_rect(self)
        if t.anchor_x_r != None and t.anchor_y_r != None:
            t.anchor_x = self.min_x + (self.max_x - self.min_x) * t.anchor_x_r
            t.anchor_y = self.min_y + (self.max_y - self.min_y) * t.anchor_y_r

    def update_gl(self):
        gl.glLoadIdentity()
        self.transform.update_gl()

    def collide(self, other_shape):
        return collide(self, other_shape)
