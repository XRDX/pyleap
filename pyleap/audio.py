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
from pyleap.resource import rss

__all__ = ['Audio', 'play', 'pause']

cache_players = {}

def Audio(url, loop=False):
    if url not in cache_players:
        source = pyglet.media.load(rss.get(url))
        player = pyglet.media.Player()
        player.queue(source)
        cache_players[url] = player
        player.loop = loop

    return cache_players[url]


def play(url, loop=False):
    Audio(url, loop).play()

def pause(url):
    """ 暂停播放音效 """
    Audio(url).pause()




