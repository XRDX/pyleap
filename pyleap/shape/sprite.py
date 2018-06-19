import pyglet
from pyglet import gl

from pyleap.resource import rss
from pyleap.window import window

from pyleap.transform import Transform
from pyleap.collision import CollisionMixin
from pyleap.color import color_to_tuple
from pyleap.util import all_shapes


class Sprite(pyglet.sprite.Sprite, CollisionMixin):
    """ Sprite """

    def __init__(self, src, x=window.center_x, y=window.center_y):

        self.img = pyglet.image.load(rss.get(src))
        self.center_image()

        super().__init__(img=self.img, x=x, y=y)

        self.points = ()
        self.transform = Transform()
        self.press_events = []

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
        # call pyglet.sprite.Sprite.draw
        all_shapes.discard(self)
        all_shapes.add(self)
        super().draw()

    def update_anchor(self):
        t = self.transform
        self.update_collision_rect()
        if t.anchor_x_r != None and t.anchor_y_r != None:
            t.anchor_x = self.min_x + (self.max_x - self.min_x) * t.anchor_x_r
            t.anchor_y = self.min_y + (self.max_y - self.min_y) * t.anchor_y_r

    def update_gl(self):
        gl.glLoadIdentity()
        self.transform.update_gl()
