# 漫游3D表情宇宙

ASDW控制，利用数值计算来模拟3D效果

![3d_world](../images/samples/3d_world.gif)

```python
from pyleap import *
from random import randint

player = Sprite("https://r.leaplearner.com/i/54b42c.png")
player.scale = 0.3
window.set_size(640, 400)
r = 1.02
n = 250
w,h = window.w, window.h
batch = Batch()


emojis = []
dx = dy = 0
speed = 5


def draw(dt):
    global dx, dy
    emojis.sort(key=lambda e: e.w)

    window.clear()
    Rectangle(0,0,w,h,"black").draw()
    if key.a.pressed: dx += speed
    if key.d.pressed: dx -= speed
    if key.w.pressed: dy -= speed
    if key.s.pressed: dy += speed

    dx = dx*0.9
    dy = dy*0.9
    move(dx, dy)

    
    for e in emojis:
        update(e)

    batch.draw()
    for e in emojis:
        if e.w > 50: e.draw()
    
    

    window.show_fps()
    player.draw()

def new(e):
    e.x = randint(-20, w+20)
    e.y = randint(-20, h+20)
    e.w = e.h = 2

def update(e):
    e.w *= r
    e.h = e.w
    if e.w > 5000: new(e)
    e.x = (e.x - w/2) * (1+e.w/5000) + w/2
    e.y = (e.y - h/2) * (1+e.w/5000) + h/2

    if e.x > w or e.x < 0 or e.y > h or e.y<0: new(e)

def move(x, y):
    for e in emojis:
        e.x += x*e.w/1000
        e.y += y*e.w/1000

for i in range(n):
    e = Sprite("https://r.leaplearner.com/ud/production/A01T0018/158520185737928.png", batch=batch)
    e.x = randint(-20, w+20)
    e.y = randint(-20, h+20)
    e.w = e.h = randint(3, 10) * randint(3, 10)
    emojis.append(e)

repeat(draw)
run()
```