from pyleap.window import window
from pyglet.window import key as default_key

from pyleap import null

class SingleKey():

    def __init__(self):
        self._press = null
        self._release = null
        self.pressed = False
    
    def on_press(self, f):
        self._press = f

    def press(self):
        self.pressed = True;
        self._press()

    def on_release(self, f):
        self._release = f

    def release(self):
        self.pressed = False;
        self._release()


class Key(dict):
    """ 
    当按下A键时，key.A 为True，否则为False

    键名

    字母：A, B, C, D, E, F, G...
    数字：因为数字不能直接作为变量, 变为_1, _2, ... 如 key._1
    方向键：LEFT，UP，RIGHT，DOWN
    功能键：HOME，PAGEUP，PAGEDOWN，END，BEGIN，BACKSPACE，TAB，LINEFEED
        CLEAR，RETURN，ENTER，PAUSE，SCROLLLOCK，SYSREQ，ESCAPE，SPACE
    功能键：F1, F2, F3..
    切换键：LSHIFT, RSHIFT, LCTRL, RCTRL，CAPSLOCK，LMETA，RMETA，LALT，RALT
        LWINDOWS， RWINDOWS，LCOMMAND，RCOMMAND，LOPTION，ROPTION
    数字区：NUM_0，NUM_1，NUM_2...


    """

    def __init__(self, **kw):
        super().__init__(**kw)

        for symbol, name in default_key.__dict__['_key_names'].items():
             s_k = SingleKey()
             self[symbol] = s_k
             self[name] = s_k

    def __getattr__(self, key):
        return self[key.upper()]



key = Key()


__all__ = ['key']