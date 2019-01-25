# 文字 Text

在pyleap中显示文字

## Text的定义

```python
Text(src, x=window.center_x, y=window.center_y,
    font_size=16, color="orange", font_name=None)
```

## Text的属性

* src: 文字内容
* x, y: 文字左下角的位置
* font_size: 文字大小，数字
* color: 文字颜色
* font_name: 字体

### Text的其他属性

* w: 宽度，文字的宽度
* h: 高度，文字的高度

## Text的方法

draw()

将文字绘制出来

举例

```python
from pyleap import *

t = Text('STCaiyun', color="red", font_size=30, font_name="STCaiyun")
t2 = Text('Hello, world1', y=30)
t3 = Text('Hello, world2', y=70)
t4 = Text('Hello, world3', y=100, color="red")
t5 = Text('Consolas', y=130, color="red", font_size=20, font_name="Consolas")
t6 = Text("LiSu", 120, 380, 50, font_name="LiSu")

r = Rectangle(t.x, t.y, t.w, t.h)

def draw(dt):
    window.clear()
    r.stroke()
    t.draw()
    t2.draw()
    t3.draw()
    t4.draw()
    t5.draw()
    t6.draw()

repeat(draw)
run()
```

## 字体查询

能够使用的字体是和系统相关的，在不同系统下常见字体如下：

## 字体名称速查

以下字体能否可用，要看系统上是否安装了该字体，不同的系统上支持不一样的字体。

**Windows** 系统上可用的字体

| 字体       | 字体名称        |
| ---------- | --------------- |
| 黑体       | SimHei          |
| 宋体       | SimSun          |
| 新宋体     | NSimSun         |
| 仿宋       | FangSong        |
| 楷体       | KaiTi           |
| 仿宋GB2312 | FangSongGB2312  |
| 楷体GB2312 | KaiTiGB2312     |
| 微软雅黑   | Microsoft YaHei |

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

| 字体     | 字体名称    |
| -------- | ----------- |
| 隶书     | LiSu        |
| 幼圆     | YouYuan     |
| 华文细黑 | STXihei     |
| 华文楷体 | STKaiti     |
| 华文宋体 | STSong      |
| 华文中宋 | STZhongsong |
| 华文仿宋 | STFangsong  |
| 方正舒体 | FZShuTi     |
| 方正姚体 | FZYaoti     |
| 华文彩云 | STCaiyun    |
| 华文琥珀 | STHupo      |
| 华文隶书 | STLiti      |
| 华文行楷 | STXingkai   |
| 华文新魏 | STXinwei    |

### 等宽字体

如果一个字体所有字母的宽度都一样，那么这个字体就是一个等宽字体。在一些特殊情况下，我们可能需要使用等宽字体，比如代码区域，为了便于阅读和差错，大多数人更喜欢使用等宽字体。
