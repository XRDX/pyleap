from pyleap.shape import Rectangle, Line, Circle


def rectangle(x, y, w, h, color, fill=True):
    r = Rectangle(x, y, w, h, color)
    if fill:
        r.draw()
    else:
        r.stroke()


def circle(x, y, r, color, fill=True):
    c = Circle(x, y, r, color)
    if fill:
        c.draw()
    else:
        c.stroke()


def line(x1, y1, x2, y2, lineWidth, color):
    lin = Line(x1, y1, x2, y2)
    lin.color = color
    lin.draw()
