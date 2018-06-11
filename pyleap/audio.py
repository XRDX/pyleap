import pyglet
from pyleap.resource import rss


class Audio(pyglet.media.StaticSource):


    def __init__(self, src):
        self.src = rss.get(src)
        super().__init__(pyglet.media.load(self.src))
