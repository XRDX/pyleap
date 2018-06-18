import math

class TransformMixin():


    def init_transform(self):
        self.anchor_x = None
        self.anchor_y = None
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
        self.anchor_x_r = 0.5
        self.anchor_y_r = 0.5

    def get_real_point(self, x, y):
        if self.anchor_x_r != None and self.anchor_y_r != None:
            self.anchor_x = self.min_x + (self.max_x - self.min_x) * self.anchor_x_r
            self.anchor_y = self.min_y + (self.max_y - self.min_y) * self.anchor_y_r

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

    def update_real_points(self):
        self.real_points = ()
        ps = self.points
        for i in range(0, len(ps), 2):
            self.real_points += self.get_real_point(ps[i], ps[i+1])

    def update_points(self):
        self._update_points()
        self.update_collision_rect()
        self.update_real_points()

