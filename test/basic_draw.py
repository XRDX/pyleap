from pyleap import *

def draw(dt):
    rectangle(0, 0, window.width, window.height, "orange")
    rectangle(100, 200, 300, 400, "green")
    line(100, 200, 300, 400, 2, 'pink')
    # triangle(200, 100, 300, 100, 250, 150, "green")
    circle(200, 200, 50, "red")
    # text('Hello, world')

schedule_interval(draw)
run()
