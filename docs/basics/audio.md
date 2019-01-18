# 音效对象 Audio

pyleap支持的音效格式有（不限于以下列出的格式）：

AU, MP2, MP3, OGG/Vorbis, WAV, WMA...

使用网络地址链接，如果使用的是网络地址链接，则会下载该资源到本地，下次运行时将直接读取本地资源

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

## 例子 Examples

键盘钢琴

```python
from pyleap import *

window.set_size(600, 500)
title = Text("小星星", 240, 450, 30)
bg = Sprite("https://rss.leaplearner.com/Image/Bgs/background.png", 300, 250)
contents = Sprite("https://upload-images.jianshu.io/upload_images/9107736-2a8859da48c7a1a3.PNG", 300, 250)

bg.scale = 0.6

Do = Audio("https://r.leaplearner.com/ud/A01T0047/6Mdf.mp3")
Re = Audio("https://r.leaplearner.com/ud/A01T0047/6QxW.mp3")
Mi = Audio("https://r.leaplearner.com/ud/A01T0047/VQZy.mp3")
Fa = Audio("https://r.leaplearner.com/ud/A01T0047/CU6z.mp3")
So = Audio("https://r.leaplearner.com/ud/A01T0047/5Ws5.mp3")
La = Audio("https://r.leaplearner.com/ud/A01T0047/skKg.mp3")
Si = Audio("https://r.leaplearner.com/ud/A01T0047/ltsY.mp3")

@key._1.on_press
def do():
    Do.play()

@key._2.on_press
def re():
    Re.play()

@key._3.on_press
def mi():
    Mi.play()

@key._4.on_press
def fa():
    Fa.play()

@key._5.on_press
def so():
    So.play()

@key._6.on_press
def la():
    La.play()

@key._7.on_press
def si():
    Si.play()

def Loop(dt):
    window.clear()
    bg.draw()
    title.draw()
    contents.draw()

repeat(Loop)
run()
```

## 常见问题 Q&A

Q：无法播放音效

A1：如果是数字按键，确认是英文输入法
A2：一般情况下无需安装插件即可播放音效，部分电脑无法播放音效，则需要安装Avbin才能播放，请选择正确的版本安装，然后重启电脑。

[Avbin下载地址](http://avbin.github.io/AVbin/Download.html)