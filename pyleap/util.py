import pyglet

from pyleap.constant_colors import color_dict


def color_to_tuple(color):
    """ convert any color to standard ()
    "red"       ->  'c3B', (255, 125, 0)
    "#ffffff"   ->  'c3B', (255, 255, 255)
    "#ffffffff" ->  'c4B', (255, 255, 255, 255)
    """
    if(type(color) == str and color[0] == "#"):
        color = hex_color_to_tuple(color)

    elif(type(color) == str and color in color_dict):
        color = color_dict[color.lower()]

    while len(color) < 4:
        color += (255,)

    return color

def hex_color_to_tuple(hex):
    """ convent hex color to tuple
    "#ffffff"   ->  (255, 255, 255)
    "#ffff00ff" ->  (255, 255, 0, 255)
    """
    hex = hex[1:]
    length = len(hex) // 2
    return tuple(int(hex[i*2:i*2+2], 16) for i in range(length))


unschedule = pyglet.clock.unschedule


def schedule_interval(func, dt=1/60):
    unschedule(func)
    pyglet.clock.schedule_interval(func, dt)


def schedule_once(func, dt=1/60):
    pyglet.clock.schedule_once(func, dt)


def run():
    pyglet.app.run()


slice = lambda s, step : [s[i:i+step] for i in range(0, len(s), step)]
