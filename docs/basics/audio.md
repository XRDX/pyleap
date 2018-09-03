### 音效对象

```python
class Audio(pyglet.media.Player):
    """ 音效对象

    Audio(url, loop=False)
    
    属性
    
    time    ： 当前的播放时间（秒），只读属性，通过seek()方法更改时间
    playing  : bool值，当前是否在播放，只读属性
    volume  ： float值，音量大小，从0到1，
    loop     : bool值，是否重复播放
    
    方法
    
    play() : 开始或者继续播放当前音效
    pause() : 暂停播放当前音效
    seek()  : 设置播放的时间
    
    """
```