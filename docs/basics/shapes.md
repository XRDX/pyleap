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

    def __init__(self, src, x=window.center_x, y=window.center_y,
            font_name='Arial',
            font_size=16, color="orange"):
                 
```
能够使用的字体是和系统相关的，在不同系统下常见字体如下：

#### 字体名称速查

**Windows** 系统上可用的字体

| 字体   | 字体名称 |
| ------ | -------- |
| 黑体   | SimHei   |
| 宋体   | SimSun   |
| 新宋体 | NSimSun  |
|  仿宋| FangSong  |
| 楷体| KaiTi  |
| 仿宋GB2312| FangSongGB2312  |
|  楷体GB2312| KaiTiGB2312  |
| 微软雅黑| Microsoft YaHei  |

**Mac Os** 上可以使用的字体有

| 字体     | 字体名称                      |
| -------- | ----------------------------- |
| 冬青黑体 | Hiragino Sans GB              |
| 华文细黑 | STHeiti Light （又名STXihei） |
| 华文黑体 | STHeiti                       |
| 华文楷体 | STKaiti                       |
| 华文宋体 | STSong                        |
| 华文仿宋 | STFangsong                    |

如果安装了Microsoft Office软件，那么还可以使用以下字体

| 字体 | 字体名称 |
| ---- | -------- |
| 隶书 | LiSu     |
|幼圆|YouYuan|
|华文细黑|STXihei|
|华文楷体|STKaiti|
|华文宋体|STSong|
|华文中宋|STZhongsong|
|华文仿宋|STFangsong|
|方正舒体|FZShuTi|
|方正姚体|FZYaoti|
|华文彩云|STCaiyun|
|华文琥珀|STHupo|
|华文隶书|STLiti|
|华文行楷|STXingkai|
|华文新魏|STXinwei|

#### 等宽字体

如果一个字体所有字母的宽度都一样，那么这个字体就是一个等宽字体。在一些特殊情况下，我们可能需要使用等宽字体，比如代码区域，为了便于阅读和差错，大多数人更喜欢使用等宽字体。

| 字体     | 字体名称 |
| -------- | -------- |
| Consolas | Consolas |


### 椭圆
```python
class Ellipse(Shape):
    """ 基本图形：椭圆 Ellipse 
    """

    def __init__(self, x=100, y=100, r_x=50, r_y=30, color="orange"):
       
```