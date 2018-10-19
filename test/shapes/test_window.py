from pyleap import *

def draw(dt):
    window.clear()
    Rectangle(0, 0, window.w, window.h, 'white').draw()
    if key.space:
        window.show_axis()

repeat(draw)
run()
