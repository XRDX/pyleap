import pyglet

class Window(pyglet.window.Window):
    """ self define window """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

