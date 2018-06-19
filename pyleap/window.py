import pyglet
from pyglet import gl
from pyleap.util import all_shapes

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

    def clear(self):
        all_shapes.clear()
        super().clear()


platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_default_screen()

template = gl.Config(alpha_size=8)
config = screen.get_best_config(template)
context = config.create_context(None)
window = Window(context=context)

# config = pyglet.gl.Config(alpha_size=8)
# window = Window(config=config)
# window = Window()
window.set_caption("LeapLearner")

# alpha
gl.glEnable(gl.GL_LINE_SMOOTH);
gl.glEnable(gl.GL_POLYGON_SMOOTH);
gl.glEnable(gl.GL_BLEND);
gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA);
gl.glHint(gl.GL_LINE_SMOOTH_HINT, gl.GL_DONT_CARE);
gl.glHint(gl.GL_POLYGON_SMOOTH_HINT, gl.GL_DONT_CARE);
