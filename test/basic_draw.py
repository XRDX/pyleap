from pyleap import *

def draw(dt):
    Rectangle(0, 0, window.width, window.height, "white").draw()
    Rectangle(100, 200, 300, 400, "green").draw()
    Line(100, 100, 500, 100, 2, 'pink').draw()
    # triangle(200, 100, 300, 100, 250, 150, "green")
    Circle(200, 200, 50, "red").draw()
    Text('Hello, world', 350, 100).draw()

schedule_interval(draw)
run()
