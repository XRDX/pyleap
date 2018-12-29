from pyleap import *

t = Text('Hello, world', color="red", font_size=30, font_name="STCaiyun")
t2 = Text('Hello, world')
t3 = Text('Hello, world', y=70)
t4 = Text('Hello, world', y=100, color="red")
t5 = Text('Hello, world', y=130, color="red", font_size=20, font_name="Consolas")

r = Rectangle(t.x, t.y, t.w, t.h)

def draw(dt):
    window.clear()

    t.rotation += 1
    r.rotation += 1

    r.stroke()
    t.draw()
    t2.draw()
    t3.draw()
    t4.draw()
    t5.draw()

repeat(draw)
run()