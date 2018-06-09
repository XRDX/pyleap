from .constant_colors import color_dict

def color2list(color):
    """ convert any color to standard ()
    "red"       ->  'c3B', (255, 125, 0)
    "#ffffff"   ->  'c3B', (255, 255, 255)
    "#ffffffff" ->  'c3B', (255, 255, 255, 255)
    """
    if(type(color) == tuple and len(color) == 3):
        return ('c3B/static', color)

    elif(type(color) == tuple and len(color) == 4):
        return ('c4B/static', color)

    elif(type(color) == str and color[0] == "#"):
        return ('c3B/static', (255, 255, 255))

    elif(type(color) == str and color in color_dict):
        return ('c3B/static', color_dict[color.lower()])

    else:
        return ('c3B/static', (255, 125, 0))




