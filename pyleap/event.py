from pyleap.window import window
from pyleap.mouse import mouse
from pyleap.collision import shape_clicked
from pyleap.util import all_shapes


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
    shapes = list(all_shapes)
    while shapes:
        shape = shapes.pop()
        if(shape.press_events and shape_clicked(shape)):
            shape.click()


@window.event
def on_mouse_release(x, y, button, modifiers):
    mouse.release()
