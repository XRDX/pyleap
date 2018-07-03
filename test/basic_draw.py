from pyleap import *

def draw(dt):
    Rectangle(0, 0, window.width, window.height, "white").draw()
    Rectangle(100, 200, 300, 400, "green").draw()
    Line(100, 100, 500, 100, 5, 'pink').draw()
    Triangle(200, 50, 300, 50, 250, 150, "green").stroke()
    Circle(200, 200, 50, "#ff4444aa").draw()
    Text('Hello, world', 350, 100).draw()

repeat(draw)
run()
