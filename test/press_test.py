from pyleap import *

bg = Rectangle(0, 0, window.width, window.height, color="white")
c = Circle(200, 200, 100, hsl(0))
c.transform.scale_y = 0.5

i = 0

def update():
    global i
    i += 10
    c.color = hsl(i)
    print(hsl(i))

def draw(dt):
    # update()
    window.clear()
    bg.draw()
    c.draw()

c.on_press(update)
schedule_interval(draw)

run()
