""" 音效对象
Audio drivers

Windows	    Mac OS X	Linux
OpenAL 	    OpenAL	    OpenAL [1]
DirectSound	 	 
						Pulseaudio

"""

import pyglet
from pyleap.resource import rss

pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')

__all__ = ['Audio', 'play', 'pause']

cache_players = {}

def Audio(url, loop=False):
    if url not in cache_players:
        source = pyglet.media.load(rss.get(url), streaming=False)

        if(loop==False):
            cache_players[url] = source
        else:
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




