import pyglet
import sys
import os
import configparser

__all__ = ['null', 'run', 'stop', 'repeat', 'run_after', 'all_shapes',
        'all_right_shapes', 'P', 'get_fps', 'Batch', 'config', 'screen']

get_fps = pyglet.clock.get_fps
Batch = pyglet.graphics.Batch
stop = pyglet.clock.unschedule

display = pyglet.canvas.get_display()
screen = display.get_default_screen()

def null():
    """ 空函数 """
    pass

def repeat(f, dt=1/60):
    """ 重复执行函数f，时间间隔dt """
    stop(f)
    pyglet.clock.schedule_interval_soft(f, dt)


def run_after(f, dt=1/60):
    """ 在一定时间之后执行 """
    pyglet.clock.schedule_once(f, dt)


def run():
    """ 在程序的最后运行，进入循环阻塞 """
    pyglet.app.run()
    

# all_shapes, use for track all the shapes draw on the windows
all_shapes = set()
all_right_shapes = set()


class P:
    """ P for point """
    def __init__(self, x, y):
        self.x = x
        self.y = y

# config file: download/config.ini

class Config:
    def __init__(self, src='download/config.ini'):
        self.src = src
        try:
            # user configs
            self.config = configparser.ConfigParser()
            self.config.read(self.src)
            if not os.path.exists("download"):
                os.makedirs("download")
        except:
            self.config = {}

    def save(self):
        try:
            with open(self.src, 'w') as configfile:
                self.config.write(configfile)
        except:
            pass

    def get_window_position(self):
        location_x = location_y = -1

        if 'location' in self.config:
            location_x = int(self.config['location']['x'])
            location_y = int(self.config['location']['y'])

        if location_x < 0 or location_y < 0 or screen.width < location_x or screen.height < location_y:
            location_x = screen.width // 2
            location_y = screen.height // 2
        return [location_x, location_y]

    def set_window_position(self, x, y):
        self.config['location'] = {'x': str(x),'y': str(y)}
        self.save()

    def set_window_quality(self, quality='normal'):
        if quality == self.get_window_quality(): return
        self.config['window'] = {'quality': quality}
        self.save()

    def get_window_quality(self):
        quality = 'normal'
        if 'window' in self.config:
            quality = self.config['window']['quality']

        return quality

config = Config()
