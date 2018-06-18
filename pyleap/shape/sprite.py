import pyglet
from pyglet import gl

from pyleap.resource import rss
from pyleap.window import window
from pyleap.collision import CollisionMixin
from pyleap.transform import TransformMixin


class Sprite(pyglet.sprite.Sprite, TransformMixin, CollisionMixin):
    """ Sprite """

    def __init__(self, src, x=window.center_x, y=window.center_y):
        self.img = pyglet.image.load(rss.get(src))
        self.center_image()

        super().__init__(img=self.img, x=x, y=y)
        self.collision_scale = 1

        self.init_transform()
        self.update_points()

    def center_image(self):
        """Sets an image's anchor point to its center"""
        self.img.anchor_x = self.img.width // 2 # int
        self.img.anchor_y = self.img.height // 2 # int

    def _update_points(self):
        w = self.img.width
        h = self.img.height
        a_x = self.img.anchor_x
        a_y = self.img.anchor_y
        scale_x = self.scale_x * self.scale * self.collision_scale
        scale_y = self.scale_y * self.scale * self.collision_scale

        min_x = self.x - a_x * scale_x
        min_y = self.y - a_y * scale_y
        max_x = self.x + (w - a_x) * scale_x
        max_y = self.y + (h - a_y) * scale_y
        self.points = (min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y)


    def draw(self):
        self.update_points()
        super().draw()
