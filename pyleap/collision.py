

class CollisionShape():

    def __init__(self, points):
        self.points = points

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


def collide(s1, s2):
    cs1 = CollisionShape(s1.points)
    cs2 = CollisionShape(s2.points)

    if cs1.min_x < cs2.max_x and cs1.max_x > cs2.min_x \
            and cs1.min_y < cs2.max_y and cs1.max_y > cs2.min_y:
        x = (min(cs1.max_x, cs2.max_x) + max(cs1.min_x, cs2.min_x)) // 2
        y = (min(cs1.max_y, cs2.max_y) + max(cs1.min_y, cs2.min_y)) // 2
        return (x, y)

    return False
