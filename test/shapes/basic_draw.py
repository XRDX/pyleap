from pyleap import *

def draw(dt):
    window.clear()
    Rectangle(0, 0, 200, 300, "blue").draw()
    window.show_axis()
    Rectangle(100, 200, 300, 200, "#00ff0080").draw()
    Line(100, 100, 600, 100, 100, 'pink').draw()
    Triangle(200, 50, 300, 50, 250, 150, "green").stroke()
    Circle(200, 200, 50, "#ff000080").draw()
    Text('Hello, world', 350, 100).draw()

repeat(draw)
run()
