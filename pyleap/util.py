import pyglet


unschedule = pyglet.clock.unschedule
stop = unschedule

def schedule_interval(func, dt=1/60):
    unschedule(func)
    pyglet.clock.schedule_interval(func, dt)


def schedule_once(func, dt=1/60):
    pyglet.clock.schedule_once(func, dt)


def run():
    pyglet.app.run()



"""all_shapes, use for track all the shapes draw on the windows
"""
all_shapes = set()
