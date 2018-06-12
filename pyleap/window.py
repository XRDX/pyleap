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

    def set_caption(self, title):
        self.title = title
        super().set_caption(title)

    def update_caption(self, mouse):
        super().set_caption("{}  x: {}, y: {}".format(self.title, mouse.x, mouse.y))


# alpha

# pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
# pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

# config = pyglet.gl.Config(alpha_size=8)


# window = Window(config=config)
window = Window()
window.set_caption("LeapLearner")
