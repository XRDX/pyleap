## Pyglet

测试能否运行Pyglet

```python
import pyglet

window = pyglet.window.Window()

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()
    
pyglet.app.run()
```



测试定时运行

```python
pyglet.clock.schedule_interval(draw, 1/60)
pyglet.app.run()
```

