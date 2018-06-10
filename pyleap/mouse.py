class Mouse():
    """ Mouse """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.moveEvents = []
        self.clickEvents = []

    def on_move(self, func):
        """ f() when mouse moving """
        self.moveEvents.append(func)

    def on_press(self, func):
        """ f() when mouse press """
        self.clickEvents.append(func)

    def move(self):
        for func in self.moveEvents:
            func()

    def press(self):
        for func in self.clickEvents:
            func()


mouse = Mouse()
