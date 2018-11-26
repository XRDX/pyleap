import pyglet
from pyglet import gl
from pyleap.util import all_shapes
import platform

# disable debug gl option 
pyglet.options['debug_gl'] = False

class Window(pyglet.window.Window):
    """ 
    属性 Attributes

    caption
    str，窗口标题，只读.

    width/w
    窗口宽度，单位像素点，只读。

    height/h
    窗口高度，单位像素点，只读。

    方法 Methods

    clear()
    清除窗口里的内容

    set_caption(caption)
    设置窗口标题
    Parameters: caption (str or unicode)

    set_size(width, height)
    设置窗口大小
    """

    def __init__(self, **kwargs):
        """ TODO """
        super().__init__(**kwargs)

        # config = pyglet.gl.Config(alpha_size=8)
        # window = Window(config=config)
        # window = Window()
        self.set_caption("LeapLearner")

    @property
    def w(self):
        """ width """
        return self.width

    @property
    def h(self):
        """ height """
        return self.height

    @property
    def center_x(self):
        return self.width // 2

    @property
    def center_y(self):
        return self.height // 2

    @property
    def caption(self):
        return self._title
    
    def set_caption(self, caption):
        self._title = caption

    def update_caption(self, mouse):
        """ 添加坐标显示 """
        caption = "{}  x: {}, y: {}".format(self._title, mouse.x, mouse.y)
        super().set_caption(caption)

    def clear(self):
        all_shapes.clear()
        super().clear()

    def show_axis(self):
        from pyleap import Line, Text
        for x in range(0, window.w, 100):
            Line(x, 0, x, window.h, 1, '#eeaa00').draw()
            Text(str(x), x+2, 2, 10).draw()
        for y in range(0, window.h, 100):
            Line(0, y, window.w, y, 1, '#eeaa00').draw()
            Text(str(y), 2, y+2, 10).draw()




sysstr = platform.system()
if(sysstr =="Windows"):
    platform = pyglet.window.get_platform()
    display = platform.get_default_display()
    screen = display.get_default_screen()

    template = pyglet.gl.Config(alpha_size=8)
    config = screen.get_best_config(template)
    context = config.create_context(None)

    try:
        window = Window(config=config, context=context) 
    except pyglet.gl.ContextException:
        window = Window()
    
else:
    window = Window()


# alpha
gl.glEnable(gl.GL_LINE_SMOOTH);
gl.glEnable(gl.GL_POLYGON_SMOOTH);
gl.glEnable(gl.GL_BLEND);
gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA);
gl.glHint(gl.GL_LINE_SMOOTH_HINT, gl.GL_DONT_CARE);
gl.glHint(gl.GL_POLYGON_SMOOTH_HINT, gl.GL_DONT_CARE);

