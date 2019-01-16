from pyleap import *

c = Circle(200, 200, 100)
t = Triangle(120, 130, 400, 300, 200, 230)
l = Line(100, 500, 500, 420)
r = Rectangle(40, 50, 100, 100)

c.color =  "#ff000090"
l.color = "#00ff0090"
r.color = "#0000ff90"

r.rotation = 45

r.line_width = 20
c.line_width = 20
l.line_width = 100
t.line_width = 15

@repeat
def draw(dt):
    window.clear()
    t.stroke()
    c.stroke()
    l.stroke()
    r.stroke()
    window.show_fps()
    

run()