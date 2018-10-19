import pyglet
import sys

from pyleap.resource import Resource

# 用于管理资源
rss = Resource()

def null():
    """ 空函数 """
    pass

stop = pyglet.clock.unschedule

def repeat(f, dt=1/60):
    """ 重复执行函数f，时间间隔dt """
    stop(f)
    pyglet.clock.schedule_interval(f, dt)


def run_after(f, dt=1/60):
    """ 在一定时间之后执行 """
    pyglet.clock.schedule_once(f, dt)


def run():
    """ 在程序的最后运行，进入循环阻塞 """
    pyglet.app.run()
    

"""all_shapes, use for track all the shapes draw on the windows
"""
all_shapes = set()

__all__ = ['null', 'run', 'stop', 'repeat', 'run_after', 'all_shapes', 'rss']
