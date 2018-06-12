"""
collide(shape1, shape2)

Detect if shape1 hit shape2

"""
from pyleap.util import SimplePoint


class CollisionMixin():

    @property
    def min_x(self):
        return min(self.points[::2])

    @property
    def max_x(self):
        return max(self.points[::2])

    @property
    def min_y(self):
        return min(self.points[1::2])

    @property
    def max_y(self):
        return max(self.points[1::2])


    def collide(self, s2):
        s1 = self
        if s1.min_x < s2.max_x and s1.max_x > s2.min_x \
                and s1.min_y < s2.max_y and s1.max_y > s2.min_y:
            x = (min(s1.max_x, s2.max_x) + max(s1.min_x, s2.min_x)) / 2
            y = (min(s1.max_y, s2.max_y) + max(s1.min_y, s2.min_y)) / 2
            return SimplePoint(x, y)

        return False
