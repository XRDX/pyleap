# 按键

按键的状态

按键的事件

```python
class Key(dict):
    """
    当按下A键时，key.A.pressed 为True，否则为False

    按键事件：key.A.on_press(func)
    按键松开事件：key.A.on_release(func)

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
key = Key()
```

例子：A键事件和状态

```python
from pyleap import *


def press():
    print("a press")

def release():
    print("a release")

key.a.on_press(press)
key.A.on_release(release)

def a_value(dt):
    print(key.a.pressed)

repeat(a_value, 1)
run()
```

## 包装器写法

```python
@key.a.on_press
def press():
    print("a pressed")
```