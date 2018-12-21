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

    def __init__(self):
        """ 初始化，创建一个窗口 """

        sysstr = platform.system()
        plat = pyglet.window.get_platform()
        display = plat.get_default_display()
        screen = display.get_default_screen()
            
        if(sysstr =="Windows"):
            template = gl.Config(alpha_size=8, sample_buffers=1, samples=4)
            configs = screen.get_matching_configs(template)

            if not configs:
                super().__init__()
            else:
                super().__init__(config=configs[0])

        else: # Mac or Linux
            super().__init__()
        
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
        for x in range(0, self.w, 100):
            Line(x, 0, x, self.h, 1, '#eeaa00').draw()
            Text(str(x), x+2, 2, 10).draw()
        for y in range(0, self.h, 100):
            Line(0, y, self.w, y, 1, '#eeaa00').draw()
            Text(str(y), 2, y+2, 10).draw()


window = Window()

# 必须放在window后面

# 抗锯齿
gl.glEnable(gl.GL_LINE_SMOOTH);
gl.glHint(gl.GL_LINE_SMOOTH_HINT, gl.GL_DONT_CARE);

gl.glEnable(gl.GL_POLYGON_SMOOTH);
gl.glHint(gl.GL_POLYGON_SMOOTH_HINT, gl.GL_DONT_CARE);

# 抗锯齿-多样本缓冲(Multisample Buffer)
gl.glEnable(gl.GL_MULTISAMPLE);

# 支持透明
gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA);
gl.glEnable(gl.GL_BLEND);

