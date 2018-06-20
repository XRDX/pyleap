import pyglet
from pyleap.window import window
from pyleap.color import color_to_tuple
from pyleap.util import all_shapes

from pyleap.shape.shape import Shape
from pyleap.collision import CollisionMixin
from pyleap.transform import Transform, TransformMixin


class Text(pyglet.text.Label, CollisionMixin, TransformMixin):
    """ Text """

    def __init__(self, text, x=window.center_x, y=window.center_y,
                 font_size=16, color="orange"):
        color = color_to_tuple(color)
        super().__init__(text=text, x=x, y=y, font_size=font_size, color=color)
        self.transform = Transform()
        self.press_events = []

    def update_points(self):
        min_x = self.x
        min_y = self.y
        max_x = self.x + self.font_size * len(self.text) * 0.5
        # width/height = 0.5
        max_y = self.y + self.font_size

        self.points = (min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y)

    def update_anchor(self):
        pass

    def draw(self):
        self.update_points()
        self.update_anchor()

        pyglet.gl.glLoadIdentity()
        self.transform.update_gl()
        all_shapes.discard(self)
        all_shapes.add(self)
        super().draw()
