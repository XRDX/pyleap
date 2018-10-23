from pyglet.window import mouse as default_mouse
from pyleap import null


class Mouse():
    """ 鼠标类
    属性
    x: x坐标
    y: y坐标

    LEFT: bool, 左键是否被按下
    RIGHT： bool, 右键是否被按下

    事件
    on_move(f): 鼠标移动时
    on_press(f): 左键点击时
    on_release(f): 左键松开时
    on_right_press(f): 右键点击时
    on_right_release(f): 右键松开时

    """

    def __init__(self):
        self.x = 0
        self.y = 0
        self._move = null

        self._press = null
        self._release = null

        self._right_press = null
        self._right_release = null

        self.LEFT = False
        self.RIGHT = False

    def on_move(self, func):
        """ 注册鼠标移动事件 """
        self._move = func

    def on_press(self, func):
        """ 注册鼠标点击事件 """
        self._press = func

    def on_release(self, func):
        """ 注册鼠标点击事件 """
        self._release = func

    def on_right_press(self, f):
        """ 注册鼠标右键点击事件 """
        self._right_press = f

    def on_right_release(self, f):
        """ 注册鼠标右键点击事件 """
        self._right_release = f
        
    def move(self):
        """ 触发鼠标移动事件 """
        self._move()

    def press(self):
        """ 触发鼠标左键点击事件 """
        self.LEFT = True
        self._press()

    def release(self):
        """ 触发鼠标左键松开事件 """
        self.LEFT = False
        self._release()

    def right_press(self):
        """ 触发鼠标右击事件 """
        self.RIGHT = True
        self._right_press()

    def right_release(self):
        """ 触发鼠标右键松开事件 """
        self.RIGHT = False
        self._right_release()

mouse = Mouse()
