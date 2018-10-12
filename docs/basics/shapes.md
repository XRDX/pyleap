## 基本图形

### 基本图形类 Shape

所有图形都继承与Shape，Shape拥有以下两个主要的属性
1. Collision，主要用于检测碰撞以及点击事件，详见Collision一节
2. Transform，用于图形的变换处理，详见Transform一节


```python
class Shape(CollisionMixin, TransformMixin):
    """ 默认参数
    颜色 color: "orange"
    线条粗细 line_width： 1 (1~10，最大值为10)
    透明度 opacity: 1 (0~1，默认为1，表示不透明，0为全透明)
    """
  
    def draw(self):
        """ 使用draw方法将图形绘制在窗口里 """

    def stroke(self):
        """ 使用stroke方法将图形绘制在窗口里，仅对基本的几何图形有效 """
```

### 圆

```python
class Circle(Shape):
    """ 基本图形：圆 Circle """

    def __init__(self, x=100, y=100, r=30, color="orange"):
        """ 
        圆心： x、y,    默认为100, 100
        半径： r，     默认为30
        颜色： color,  默认为 "orange"
        """
```


实例：

```python
from pyleap import *

ball = Circle(x=100, y=100, r=50, color="red")

def draw(dt):
    ball.draw()

repeat(draw)
run()
```



### 矩形

```python
class Rectangle(Shape):
    """ 长方形： Rectangle

    """

    def __init__(self, x=100, y=100, w=100, h=50, color="orange"):
        """ 长方形
        左下角顶点的位置： x, y
        宽度： w
        高度： h
        颜色： color 默认为 "orange"
        """
```


### 线段

```python
class Line(Shape):
    def __init__(self, x1=100, y1=100, x2=200, y2=200, line_width=1, color="orange"):
        """ 线段
        线段宽度： line_width， 默认为1
        颜色： color, 默认为"orange"
        """
```


### 文字
```python
class Text(Rectangle):
    """ Text
    src: 文本内容
    font_size: 文字高度
    """

    def __init__(self, src, x, y, font_size=16, color="orange"):
                 
```


### 椭圆
```python
class Ellipse(Shape):
    """ 基本图形：椭圆 Ellipse 
    """

    def __init__(self, x=100, y=100, r_x=50, r_y=30, color="orange"):
       
```