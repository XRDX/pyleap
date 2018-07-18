import pyglet

from pyleap.util import rss
from pyleap.window import window
from pyleap.shape.rectangle import Rectangle


cache_images = {}

class Sprite(Rectangle):
    """ Sprite """

    def __init__(self, src, x=300, y=200):
        """
        默认位置： 300, 200
        """
        if src not in cache_images:
              img = pyglet.image.load(rss.get(src))
              self.center_image(img)
              cache_images[src] = img
        
        self.img = cache_images[src]
        self.sprite = pyglet.sprite.Sprite(img=self.img, x=x, y=y)
        # self.collision_scale = 0.8
        super().__init__(x, y)      


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
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.draw()
