import pyglet

class Mouse():
    """ Mouse """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.events = {
            "move": [],
            "press": [],
            "release": []
        }

    def on_move(self, func):
        """ f() when mouse moving """
        self.events["move"].append(func)

    def on_press(self, func):
        """ f() when mouse press """
        self.events["press"].append(func)

    def on_release(self, func):
        self.events["release"].append(func)

    def move(self):
        for func in self.events["move"]:
            func()

    def press(self):
        for func in self.events["press"]:
            func()

    def release(self):
        for func in self.events["release"]:
            func()
            

mouse = Mouse()
