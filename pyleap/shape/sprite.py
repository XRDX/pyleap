import pyglet
from pyglet import gl

from pyleap.resource import rss
from pyleap.window import window
from pyleap.collision import collide


class Sprite(pyglet.sprite.Sprite):
    """ Sprite """

    def __init__(self, src, x=window.center_x, y=window.center_y):
        self.img = pyglet.image.load(rss.get(src))
        self.center_image()
        super().__init__(img=self.img, x=x, y=y)

    def center_image(self):
        """Sets an image's anchor point to its center"""
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2

    @property
    def points(self):
        min_x = self.x - self.img.anchor_x
        min_y = self.y - self.img.anchor_y
        max_x = self.x + self.img.width - self.img.anchor_x
        max_y = self.y + self.img.width - self.img.anchor_y

        return (min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y)

    def collide(self, shape):
        return collide(self, shape)
