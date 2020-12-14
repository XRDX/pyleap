# 常见问题解答

## 启动黑屏

现象：启动以后显示黑屏

A：将默认的使用的显卡驱动修改为Nvidia

右键菜单 -> 找到Nvidia设置 -> 3d设置-> 默认选择Nvidia


## 图片不显示

在代码第二行增加

```python
window.set_quality("low")
```

来使用兼容模式运行


## 闪屏

修改你的显示代码

比如你的代码中，draw函数用来绘制图形，repeat用来重复绘制

```python

def draw(dt):
    a.draw()
    b.draw()

repeat(draw)
```

修改为使用事件驱动的方式来进行：

```python
@window.event
def on_draw():
    a.draw()
    b.draw()

```

注意，要移除掉dt参数和repeat这一行