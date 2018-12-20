### 音效对象

pyleap支持的音效格式有（不限于以下列出的格式）：

* AU
* MP2
* MP3
* OGG/Vorbis
* WAV
* WMA

在项目中使用音效，除wav格式的音效外，其他的音效资源需要安装Avbin才能播放。 Avbin下载地址：http://avbin.github.io/AVbin/Download.html
可以使用网络地址链接，如果使用的是网络地址链接，则会下载该资源到本地，下次运行时将直接读取本地资源

```python
class Audio(url, loop=False):
    """ 方法
    play() : 播放当前音效
    pause() : 暂停播放当前音效
    """
```

```python
def play(url, loop=False):
    """ 播放音效 """

def pause(url):
    """ 暂停音效 """
```