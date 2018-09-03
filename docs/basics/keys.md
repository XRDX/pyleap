### 按键
```python
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
    
key = Key()
```

使用：
```python
if key._1:
    print("key 1 is pressed")
```