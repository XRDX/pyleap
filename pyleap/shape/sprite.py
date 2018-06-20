import pyglet

from pyleap.resource import rss
from pyleap.window import window
from pyleap.shape.rectangle import Rectangle


class Sprite(Rectangle):
    """ Sprite """

    def __init__(self, src, x=window.center_x, y=window.center_y):
        self.img = pyglet.image.load(rss.get(src))
        self.center_image(self.img)

        self.sprite = pyglet.sprite.Sprite(img=self.img, x=x, y=y)
        # self.collision_scale = 0.8
        super().__init__(x, y)

    @property
    def x(self):
        return self.sprite.x

    @x.setter
    def x(self, x):
        self.sprite.x = x

    @property
    def y(self):
        return self.sprite.y

    @y.setter
    def y(self, y):
        self.sprite.y = y        


    def center_image(self, img):
        """Sets an image's anchor point to its center"""
        img.anchor_x = img.width // 2 # int
        img.anchor_y = img.height // 2 # int

    def update_points(self):
        w = self.img.width
        h = self.img.height

        min_x = self.x - w/2
        min_y = self.y - h/2
        max_x = self.x + w/2
        max_y = self.y + h/2
        self.points = (min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y)

    def draw(self):
        self.update_all()
        self.sprite.draw()
