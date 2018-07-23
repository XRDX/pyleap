### 图像 `Sprite`

```javascript
class Sprite extends Rectangle
  constructor (src, x = 0, y = 0, w = null, h = null)
```

#### 属性

------

##### 图片链接 `src`

获取或者设置图片的链接

##### 加载完成事件 `onload`

如果定义了`onload`事件，那么当图片加载完成时就会触发

#### 方法

------

##### 裁剪图片 `clip(sx, sy, sw, sh)`

`sx`,` sy`: 图片裁剪开始的位置

`sw`, `sh`: 裁剪的图片大小