import pyglet

from pyleap.resource import rss
from pyleap.window import window
from pyleap.shape.rectangle import Rectangle

cache_images = {}


class Sprite(Rectangle):
    """ Sprite """

    def __init__(self, src, x=300, y=200, w=None, h=None, batch=None):
        """
        默认位置： 300, 200
        """
        self.batch = batch
        self.src = src
        w = w or self._sprite.width
        h = h or self._sprite.height
        super().__init__(x, y, w, h)
        self.collision_scale = 0.8

    @property
    def w(self):
        return self.img.width * self._sprite.scale_x
    
    @w.setter
    def w(self, w):
        self._sprite.scale_x =  w / self.img.width

    @property
    def h(self):
        return self.img.height * self._sprite.scale_y
    
    @h.setter
    def h(self, h):
        self._sprite.scale_y =  h / self.img.height

    @property
    def src(self):
        return self._src
    
    @src.setter
    def src(self, src):
        if src not in cache_images:
            try:
                file_name = rss.get(src);
                if file_name[-4:] == ".gif":
                    img = pyglet.image.load_animation(file_name)
                    img.height = img.get_max_height()
                    img.width = img.get_max_width()
                else:
                    img = pyglet.image.load(file_name)
            except pyglet.image.codecs.ImageDecodeException:
                import os, sys
                print("Couldn't load image, please delete the picture and retry.")
                print("Error picture: {}\\{}".format(os.getcwd(), rss.get(src)))
                sys.exit()

            
            self.center_image(img)
            cache_images[src] = img

        self._src = src
        self.img = cache_images[src]
        
        if hasattr(self, "_sprite"):
            self._sprite.image = self.img
        else:
            try:
                self._sprite = pyglet.sprite.Sprite(img=self.img, batch=self.batch)
            except pyglet.gl.lib.GLException:
                from ctypes import c_long
                import sys,os
                i = c_long()
                pyglet.gl.glGetIntegerv(pyglet.gl.GL_MAX_TEXTURE_SIZE, i)

                width = self.img.width
                height = self.img.height

                n = max(width//i.value, height//i.value) + 1 # 缩小倍数
                self.img.width //= n
                self.img.height //=n 
                self._sprite = pyglet.sprite.Sprite(img=self.img, batch=self.batch)

                # print("The limit size of picture： on your PC is: {}x{}".format(i.value, i.value))
                # print("Resize the size of picture：")
                # print("Error picture：{}\\{}".format(os.getcwd(), rss.get(src)))
                # sys.exit()


    @property
    def x(self):
        return self._sprite.x

    @x.setter
    def x(self, x):
        self._sprite.x = x

    @property
    def y(self):
        return self._sprite.y

    @y.setter
    def y(self, y):
        self._sprite.y = y

    @property
    def opacity(self):
        return self._sprite.opacity / 255

    @opacity.setter
    def opacity(self, opacity):
        self._sprite.opacity = int(opacity * 255)

    def center_image(self, img):
        """Sets an image's anchor point to its center"""
        img.anchor_x = img.width // 2 # int
        img.anchor_y = img.height // 2 # int

    def update_points(self):
        min_x = self.x - self.w/2 * self.collision_scale
        min_y = self.y - self.h/2 * self.collision_scale
        max_x = self.x + self.w/2 * self.collision_scale
        max_y = self.y + self.h/2 * self.collision_scale
        self.points = (min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y)

    def draw(self):
        self._before_draw()
        if(type(self._sprite.image)==pyglet.image.Animation):
            pyglet.gl.glTranslatef(-self.w//2, -self.h//2, 0)
        self._sprite.draw()
        self._after_draw()

    def delete(self):
        self._sprite.delete()
