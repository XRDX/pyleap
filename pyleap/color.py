from pyleap.constant_colors import color_dict


def color_to_tuple(color):
    """ convert any color to standard ()
    "red"       ->  'c3B', (255, 125, 0)
    "#ffffff"   ->  'c3B', (255, 255, 255)
    "#ffffffff" ->  'c4B', (255, 255, 255, 255)
    """
    if(type(color) == str and color[0] == "#"):
        color = hex_color_to_tuple(color)

    elif type(color) == str:
        if color in color_dict:
            color = color_dict[color.lower()]
        else:
            color = (255, 125, 0, 255) 

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

def hsl(h, s=0.5, l=0.5):
    return hsla_to_rgba(h, s, l, 1)

def hsla(h, s=0.5, l=0.5, a=1):
    return hsla_to_rgba(h, s, l, a)

def hsla_to_rgba(h, s, l, a):
    """ 0 <= H < 360, 0 <= s,l,a < 1
    """
    h = h % 360
    s = max(0, min(1, s))
    l = max(0, min(1, l))
    a = max(0, min(1, a))

    c = (1 - abs(2*l - 1)) * s
    x = c * (1 - abs(h/60%2 - 1))
    m = l - c/2

    if h<60:
        r, g, b = c, x, 0
    elif h<120:
        r, g, b = x, c, 0
    elif h<180:
        r, g, b = 0, c, x
    elif h<240:
        r, g, b = 0, x, c
    elif h<300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x


    return (int((r+m)*255), int((g+m)*255), int((b+m)*255), int(a*255))