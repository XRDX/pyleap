### 形变

形变包括旋转、缩放等方式

#### 属性值
##### rotation

设置或者获取旋转角度，默认为0，360度制

```python
shape.rotation = 90
```



##### scale

设置或者获取缩放比例，默认为1
设置为2时，即为原来的2倍大小
设置为0.5时，几位原来的1/2大小

```python
shape.scale = 2
```



##### scale_x

设置或者获取图形水平方向的缩放比例，和上述的scale相互叠加

```python
shape.scale_x = 2
```



##### scale_x

设置或者获取图形垂直方向的缩放比例，和上述的scale相互叠加

```python
shape.scale_y = 0.5
```



#### 方法
##### set_anchor(x, y)

设置图形形变的中心点，参数为坐标值

```python
shape.set_anchor(300, 300)
```



##### set_anchor_rate(x_r, y_r)

设置图形形变的百分比，默认为(0.5, 0.5)，即图像中心点
设置为(0, 0)，即沿着图形左下角进行形变
设置为(1, 1), 即沿着图形右上角进行形变

```python
shape.set_anchor_rate(0.1, 0.2)
```

