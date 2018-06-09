import pyglet

class Window(pyglet.window.Window):
    """ self define window """

    def __init__(self, **kwargs):
        """ TODO """
        super().__init__(**kwargs)


canvas = Window()
