### 序列帧动画 Animation

![ani](../images/ani.png)

```javascript
class Animation extends Sprite
  constructor (src, x, y, w, h)
```

**方法**

##### 设置序列帧 `setFrame(c, r)`

`c`: 序列帧的列数，如上述实例的图片中，列数为8

`r`: 序列帧的行数

默认参数为4x1

##### 设置播放速度 setSpeed(speed)

设置序列帧的播放速度，多少个draw更新一次序列帧，默认为10