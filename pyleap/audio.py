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


class Audio(pyglet.media.StaticSource):
    """ 音效对象
   
    属性

    time    ： 当前的播放时间（秒），只读属性，通过seek()方法更改时间
    playing  : bool值，当前是否在播放，只读属性
    volume  ： float值，音量大小，从0到1，

    方法

    play() : 开始或者继续播放当前音效
    pause() : 暂停播放当前音效
    seek()  : 设置播放的时间

    """

    def __init__(self, src):
        """ Decoding sounds can be processor-intensive and may introduce latency, particularly for short sounds that must be played quickly, such as bullets or explosions. You can force such sounds to be decoded and retained in memory rather than streamed from disk by wrapping the source in a StaticSource:"""
        super().__init__(pyglet.media.load(rss.get(src)))
