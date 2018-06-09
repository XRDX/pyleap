import pyglet

from .window import canvas


def do_nothing():
    pass


class Mouse():
    """ Mouse """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = do_nothing
        self.click = do_nothing


mouse = Mouse()


@canvas.event
def on_mouse_motion(x, y, dx, dy):
    mouse.x, mouse.y = x, y
    mouse.move()


@canvas.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    mouse.x, mouse.y = x, y
    mouse.move()


@canvas.event
def on_mouse_press(x, y, button, modifiers):
    mouse.click()


run = pyglet.app.run
setInterval = pyglet.clock.schedule_interval
