from pyleap import *

def draw(dt):
    window.clear()
    Rectangle(0, 0, window.w, window.h, 'white').draw()
    if key.F1.pressed:
        window.show_axis()
    if key.a.pressed:
        Text("A").draw()

repeat(draw)
run()
