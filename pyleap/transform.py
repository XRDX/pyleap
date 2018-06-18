import math
from pyglet import gl
from pyleap.collision import CollisionMixin

#     # x, y, z
#     gl.glLoadIdentity()
#     gl.glTranslatef(x, y, z=0)
#     gl.glScalef(x, y, z=1.0)
#     gl.glRotatef(30, 0.0, 0.0, 1.0)
#     gl.glTranslatef(-100, -100, 0)

class Transform(CollisionMixin):


    def __init__(self):
        self.anchor_x = 0
        self.anchor_y = 0
        self.anchor_x_r = 0.5
        self.anchor_y_r = 0.5
        self.rotation = 0
        self.scale = 1
        self.scale_x = 1
        self.scale_y = 1

    def set_anchor(self, x, y):
        self.anchor_x = x
        self.anchor_y = y
        self.anchor_x_r = None
        self.anchor_y_r = None

    def set_anchor_rate(self, x, y):
        self.anchor_x_r = x
        self.anchor_y_r = y

    def get_point(self, x, y):
        x -= self.anchor_x
        y -= self.anchor_y

        x *= self.scale_x * self.scale
        y *= self.scale_y * self.scale

        d = self.rotation / 180 * math.pi
        cos = math.cos(d)
        sin = math.sin(d)

        new_x = x*cos - y*sin
        new_y = y*cos + x*sin

        x = new_x
        y = new_y

        x += self.anchor_x
        y += self.anchor_y

        return (x, y)

    def update_points(self, ps):
        self.points = ()
        for i in range(0, len(ps), 2):
            self.points += self.get_point(ps[i], ps[i+1])

    def update_gl(self):
        gl.glTranslatef(self.anchor_x, self.anchor_y, 0)
        gl.glRotatef(self.rotation, 0.0, 0.0, 1.0)
        gl.glScalef(self.scale_x, self.scale_y, 1.0)
        gl.glTranslatef(-self.anchor_x, -self.anchor_y, 0)


