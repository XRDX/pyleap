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