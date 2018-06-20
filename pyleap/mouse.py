from pyglet.window import mouse as default_mouse

class Mouse():
    """ Mouse """

    def __init__(self):
        self.x = 0
        self.y = 0
        self._move = None
        self._press = None
        self._release = None
        self.LEFT = False
        self.RIGHT = False

    def on_move(self, func):
        """ f() when mouse moving """
        self.move = func

    def on_press(self, func):
        """ f() when mouse press """
        self.press = func

    def on_release(self, func):
        self.release = func

    def move(self):
        if(self._move): self._move()

    def press(self):
        if(self._press): self._press()

    def release(self):
        if(self._release): self._release()    

mouse = Mouse()
