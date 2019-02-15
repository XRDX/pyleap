# 基本图形

## 基本图形类 Shape

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

## 矩形

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

## 椭圆

```python
class Ellipse(Shape):
    """ 基本图形：椭圆 Ellipse
    """

    def __init__(self, x=100, y=100, r_x=50, r_y=30, color="orange"):
```