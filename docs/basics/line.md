# 线段

将平面上的两点连接起来，就组成了一条线段。只要确定了线段的两个端点，就可以确定了整个线段的位置。

## 线段的定义

```python
class Line(Shape):
    def __init__(self, x1=100, y1=100, x2=200, y2=200, line_width=1, color="orange"):
        """ 线段
        线段宽度： line_width， 默认为1
        颜色： color, 默认为"orange"
        """
```

## 跳跃的线条

```python
from pyleap import *
import random

# 创建对象
line = Line()
line.x1speed = 5-random.random()*10
line.y1speed = 5-random.random()*10
line.x2speed = 5-random.random()*10
line.y2speed = 5-random.random()*10
color = 0

# 绘制函数
def draw(dt):
    global color

    line.x1 += line.x1speed
    line.y1 += line.y1speed
    line.x2 += line.x2speed
    line.y2 += line.y2speed

    if line.x1 < 0 or line.x1 > window.w:
        line.x1speed = -line.x1speed
    if line.x2 < 0 or line.x2 > window.w:
        line.x2speed = -line.x2speed
    if line.y1 < 0 or line.y1 > window.h:
        line.y1speed = -line.y1speed
    if line.y2 < 0 or line.y2 > window.h:
        line.y2speed = -line.y2speed

    color += 1
    line.color = hsl(color)
    line.draw()

repeat(draw)
run()
```