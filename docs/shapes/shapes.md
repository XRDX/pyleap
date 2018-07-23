### 圆形 `Circle`

```javascript
class Circle extends Shape {
  constructor (x = 50, y = 50, r = 20, color="orange")
```

#### 属性值

##### 坐标值 `x,y`

圆形的坐标值

##### 半径 `r` / `radius`

等价属性，可以任意使用其中一个

### 点 Point

```javascript
class Point extends Circle {
  constructor (x, y, color="red")
```

### 线段 Line

属性值

坐标点 `x1, y1, x2, y2`

各个点的坐标值

坐标` x, y`

获取或者设置线段的中心点

### 多边形 `Polygon`

```javascript
class Polygon extends Shape
```

坐标 `x, y`

获取或者设置多边形的中心点

### 三角形 `Triangle`

```javascript
const Triangle = Polygon;
```

### 矩形 `Rectangle`

```javascript
class Rectangle extends Shape
  constructor (x = 100, y = 100, w = 100, h = 50, color="orange")
```

属性值

坐标点 `x,y`

矩形左上角顶点的坐标值

宽度` w` / `width`

矩形的宽度

高度 `h` / `width`

矩形的高度

**方法**

设置碰撞的区域 `setCollisionScale(w, h)`

设置碰撞区域大小，默认为1，即正常大小

当`w`设置为0.5时，表示可碰撞区域的宽度为原始宽度的一半

### 椭圆 `Ellipse`

```javascript
class Ellipse extends Shape {
  constructor (x, y, rX, rY, color="orange")
```

### 属性

圆心位置 `x, y`

水平轴半径 `rX`, `radiusX`

垂直轴半径` rY`, `raduisY`

### 文本 `Text`

```javascript
class Text extends Rectangle
  constructor (src = 'LeapLearner', x = 0, y = 0, size = 20, color="orange", font = 'Arial')
```

#### 属性

##### 文本内容 `src`

获取或者设置文本的内容

##### 字体大小 ` size`

获取或者设置文本字体大小

##### 字体 `font`

获取或者设置文本字体