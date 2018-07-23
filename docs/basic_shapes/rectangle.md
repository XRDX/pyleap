### 长方形 rectangle

长方形是由顶点位置和宽和高组成，并且我们可以画出不同颜色的长方形。长方形的定义如下：

```javascript
rectangle(x, y, w, h, *color)
/***************************
x - x坐标
y - y坐标
w - 宽度
h - 高度
color - 颜色，默认为orange
***************************/
```

通过设定rectangle的属性，我们可以绘制不同的一些长方形。

```javascript
canvas.showAxis();
rectangle(50, 50, 100, 50);
rectangle(50, 150, 100, 50, 'red');
rectangle(50, 250, 100, 50, '#ffff00');

// 如果想要画一个边框的长方形边框，在使用rectangle之前，使用fill方法
fill(false); // 无填充
rectangle(200, 50, 100, 50);
rectangle(200, 150, 100, 50, 'red');
rectangle(200, 250, 100, 50, '#ffff00');
```

运行后就可以得到下述结果，在这里`canvas.showAxis();`让我们能够在画布上显示出坐标。

![rectangle](../images/2018/rectangle.png)
