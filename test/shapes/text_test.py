from pyleap import *

t = Text('Hello, world', color="red", font_size=30, font_name="LiSu")
t.src = "隶书"
r = Rectangle(t.x, t.y, t.w, t.h)

def draw(dt):
    window.clear()

    t.rotation += 1
    r.rotation += 1

    r.stroke()
    t.draw()

repeat(draw)
run()