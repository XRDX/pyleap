import pyglet


class Window(pyglet.window.Window):
    """ self define window """

    def __init__(self, **kwargs):
        """ TODO """
        super().__init__(**kwargs)

    @property
    def w(self):
        return self.width

    @w.setter
    def w(self, w):
        self.height = w

    @property
    def h(self):
        return self.height

    @h.setter
    def h(self, h):
        self.height = h

    @property
    def center_x(self):
        return self.width // 2

    @property
    def center_y(self):
        return self.height // 2


canvas = Window()
