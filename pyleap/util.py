import pyglet



def schedule_interval(func, dt=1/60):
    unschedule(func)
    pyglet.clock.schedule_interval(func, dt)


def schedule_once(func, dt=1/60):
    """ 在程序的最后运行，进入循环阻塞 """
    pyglet.clock.schedule_once(func, dt)


def run():
    """ 在程序的最后运行，进入循环阻塞 """
    pyglet.app.run()


unschedule = pyglet.clock.unschedule
stop = unschedule
repeat = schedule_interval
run_after = schedule_once

"""all_shapes, use for track all the shapes draw on the windows
"""
all_shapes = set()
