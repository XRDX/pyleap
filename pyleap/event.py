from pyleap.window import window
from pyleap.mouse import mouse


@window.event
def on_mouse_motion(x, y, dx, dy):
    mouse.x, mouse.y = x, y
    mouse.move()
    window.update_caption(mouse)


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    mouse.x, mouse.y = x, y
    mouse.move()


@window.event
def on_mouse_press(x, y, button, modifiers):
    mouse.press()


@window.event
def on_mouse_release(x, y, button, modifiers):
    mouse.release()
