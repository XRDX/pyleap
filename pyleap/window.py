import pyglet
import platform

from pyleap.mouse import mouse
from pyleap.collision import shape_clicked
from pyleap.util import all_shapes, config, get_fps, screen
from pyleap.key import key

__all__ = ['window', "Window"]

# disable debug gl option 
pyglet.options['debug_gl'] = False


def enable_smooth_multisample_blend():
    # 抗锯齿
    pyglet.gl.glEnable(pyglet.gl.GL_LINE_SMOOTH)
    pyglet.gl.glHint(pyglet.gl.GL_LINE_SMOOTH_HINT, pyglet.gl.GL_DONT_CARE)

    pyglet.gl.glEnable(pyglet.gl.GL_POLYGON_SMOOTH)
    pyglet.gl.glHint(pyglet.gl.GL_POLYGON_SMOOTH_HINT, pyglet.gl.GL_DONT_CARE)

    # 抗锯齿-多样本缓冲(Multisample Buffer)
    pyglet.gl.glEnable(pyglet.gl.GL_MULTISAMPLE)

    # 支持透明
    pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
    pyglet.gl.glEnable(pyglet.gl.GL_BLEND)

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
        # low quality window
        if config.get_window_quality() == 'low':
            super().__init__()
        # Mac or Linux
        elif platform.system() != "Windows": 
            super().__init__()
            enable_smooth_multisample_blend()
        
        elif platform.system() == "Windows":
            template = pyglet.gl.Config(alpha_size=8, sample_buffers=1, samples=4)
            configs = screen.get_matching_configs(template)
            if configs:
                super().__init__(config=configs[0])
                enable_smooth_multisample_blend()
            else:
                super().__init__()
    
        self.set_caption("LeapLearner")

        location_x, location_y = config.get_window_position()
        self.set_location(location_x, location_y)
        self.axis_batch = None
        init_event(self)

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
        # super().clear()
        pyglet.graphics.vertex_list(4,
            ('v2i', (0, 0, self.w, 0, self.w, self.h, 0, self.h)),
            ('c3B', (255, 255, 255) * 4)
        ).draw(pyglet.gl.GL_QUADS)

    def show_axis(self):       
        if self.axis_batch is None:
            self.create_axis_batch()

        self.axis_batch.draw()

    def create_axis_batch(self):
        self.axis_batch = pyglet.graphics.Batch()
        for x in range(0, self.w, 100):
            self.axis_batch.add(
                2, pyglet.gl.GL_LINES, None,
                ('v2i', (x, 0, x, self.h)),
                ('c3B', (240, 160, 0) * 2))

            pyglet.text.Label(str(x), x=x+2, y=2, color=(240, 160, 0, 255), batch=self.axis_batch)

        for y in range(0, self.h, 100):
            self.axis_batch.add(
                2, pyglet.gl.GL_LINES, None,
                ('v2i', (0, y, self.w, y)),
                ('c3B', (240, 160, 0) * 2))
            pyglet.text.Label(str(y), x=2, y=y+2, color=(240, 160, 0, 255), batch=self.axis_batch)

    def show_fps(self):
        fps = int(get_fps())

        if fps>100:
            s = "fps: >100"
        else:
            s = "fps: {}".format(fps)
        pyglet.text.Label(s, x=2, y=window.h-15, color=(240, 160, 0, 255)).draw()

    def keep_on_top(self):
        # keep window on top
        if platform.system()=="Windows":
            try:
                import win32gui
                import win32con
                win32gui.SetWindowPos(self._hwnd, win32con.HWND_TOPMOST, 0,0,0,0,
                win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            except:
                print("Please install pywin32 first to use keep_on_top()")
        # Mac
        elif "Darwin" in platform.system():
            import os
            script = 'tell application "System Events" \
              to set frontmost of the first process whose unix id is {pid} to true'.format(pid=os.getpid())
            os.system("/usr/bin/osascript -e '{script}'".format(script=script))
        else:
            print("window.keep_on_top() is only supported on windows")

    def set_quality(self, quality='low'):
        config.set_window_quality(quality)


def init_event(window):
    @window.event
    def on_mouse_motion(x, y, dx, dy):
        """ 当鼠标没有按下时移动的时候触发 """
        mouse.x, mouse.y = x, y
        mouse.move()
        window.update_caption(mouse)


    @window.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        """ 当鼠标按下并且移动的时候触发 """
        mouse.x, mouse.y = x, y
        mouse.move()

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        """ 按下鼠标时 

        """ 
        if button == 1: #MouseKeyCode.LEFT:
            mouse.press()
        elif button == 4: #MouseKeyCode.RIGHT:
            mouse.right_press()

        # 判断是否有图形的点击事件被触发了
        shapes = list(all_shapes)
        while shapes:
            shape = shapes.pop()
            if(shape._press and shape_clicked(shape)):
                shape._press()


    @window.event
    def on_mouse_release(x, y, button, modifiers):
        """ 松开鼠标时 """ 
        if button == 1: #MouseKeyCode.LEFT:
            mouse.release()
        elif button == 4: #MouseKeyCode.RIGHT:
            mouse.right_release()


    @window.event
    def on_key_press(symbol, modifiers):
        """ 当键盘按键按下时触发 """
        try:
            key[symbol].press()
        except:
            pass


    @window.event
    def on_key_release(symbol, modifiers):
        """ 当键盘按键松开时触发 """
        try:
            key[symbol].release()
        except:
            pass

    @window.event
    def on_move(x, y):
        config.set_window_position(x, y)


window = Window()
