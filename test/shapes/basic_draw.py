from pyleap import Rectangle, window, Line, Polygon, Circle, Text, repeat, run


bg = Rectangle(0, 0, window.w, window.h, "white")

def draw(dt):
    window.clear()
    
    bg.draw()
    window.show_axis()

    Rectangle(10, 10, 300, 200, "#00ff0080").stroke()

    Line(100, 100, 600, 100, 100, 'pink').draw()
    Polygon(200, 50, 300, 50, 250, 150, "green").draw()
    Circle(200, 200, 120, "#ff000010").draw()
    Text('Hello, world', 350, 100).draw()
    window.show_fps()

repeat(draw)
run()
