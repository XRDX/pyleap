### 窗口

```python
class Window(pyglet.window.Window):
    """ 
    属性 Attributes

    caption
    str，窗口标题，只读.

    width/w
    窗口宽度，单位像素点，只读。

    height/h
    窗口高度，单位像素点，只读。

    方法 Methods

    clear()
    清除窗口里的内容

    set_caption(caption)
    设置窗口标题
    Parameters: caption (str or unicode)

    set_size(width, height)
    设置窗口大小
    """
    
window = Window()
```

举例：

```python
window.set_size(400, 500)
```

