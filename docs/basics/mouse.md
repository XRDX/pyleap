### 鼠标

```python
class Mouse():
    """ 鼠标类
    属性
    x: x坐标
    y: y坐标

    LEFT: bool, 左键是否被按下
    RIGHT： bool, 右键是否被按下
    
    事件
    on_move(f): 鼠标移动时
    on_press(f): 左键点击时
    on_release(f): 左键松开时
    on_right_press(f): 右键点击时
    on_right_release(f): 右键松开时
    
    """
    
mouse = Mouse()
```

举例：

```python
circle.x = mouse.x
```