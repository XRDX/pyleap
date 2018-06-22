import pyglet
from pyleap.resource import rss


class Audio(pyglet.media.StaticSource):


    def __init__(self, src):
        super().__init__(pyglet.media.load(rss.get(src)))
