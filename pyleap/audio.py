""" 音效对象
支持的音效格式有（不限于以下列出的格式）：

* AU
* MP2
* MP3
* OGG/Vorbis
* WAV
* WMA

在项目中使用音效，除wav格式的音效外，其他的音效资源需要安装Avbin才能播放。 Avbin下载地址：http://avbin.github.io/AVbin/Download.html
可以使用网络地址链接，如果使用的是网络地址链接，则会下载该资源到本地，下次运行时将直接读取本地资源
"""

import pyglet
from pyleap.util import rss


class StaticSource(pyglet.media.StaticSource):
    """ 音效对象
   
    Audio(url)

    方法
    play() : 播放
    pause() ： 暂停
    """
    def __init__(self, src): 
        source = pyglet.media.load(rss.get(src))
        super().__init__(source)


def Audio(src, loop=False):
    if loop:
        return BGM(src)
    else:
        return StaticSource(src)
        

class BGM(pyglet.media.Player):
    """ 循环播放的音乐

    方法
    play() : 播放
    pause() ： 暂停
    """

    def __init__(self, src, loop=True):
        super().__init__()
        source = pyglet.media.load(rss.get(src))
        source_group = pyglet.media.SourceGroup(source.audio_format, None)
        source_group.loop = loop
        source_group.queue(source)
        self.queue(source_group)


cache_musics = {}

def play(url, loop=False):
    if url not in cache_musics:
        if loop:
            cache_musics[url] = BGM(url)
        else:
            cache_musics[url] = Audio(url)

    cache_musics[url].play()

def pause(url):
    """ 暂停播放音效 """
    cache_musics[url].pause()


__all__ = ['Audio', 'play', 'pause']

