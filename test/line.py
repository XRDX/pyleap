from pyleap import *

def draw(dt):
    Rectangle(0, 0, window.w, window.h, "white").draw()
    window.show_axis()
    Line(100, 150, 200, 150, 0.1, '#eeaa00').draw()
    Line(150, 200, 150, 300, 1, 'red').draw()
    Line(100, 300, 300, 400, 4, '#00ff00').draw()
    Line(100, 400, 300, 100, 10, 'black').draw()

schedule_interval(draw)
run()
