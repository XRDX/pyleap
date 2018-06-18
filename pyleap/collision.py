"""
collide(shape1, shape2)

Detect if shape1 hit shape2

"""
class CollisionMixin():


    def update_collision_rect(self):
        self.min_x = min(self.points[::2])
        self.max_x = max(self.points[::2])
        self.min_y = min(self.points[1::2])
        self.max_y = max(self.points[1::2])

    def collide(self, s2):
        s1 = self
        if not (s1.points and s2.points):
            return False

        t1 = s1.transform
        t2 = s2.transform

        t1.update_points(s1.points)
        t2.update_points(s2.points)

        t1.update_collision_rect()
        t2.update_collision_rect()

        if t1.min_x < t2.max_x and t1.max_x > t2.min_x \
                and t1.min_y < t2.max_y and t1.max_y > t2.min_y:

            x = (min(t1.max_x, t2.max_x) + max(t1.min_x, t2.min_x)) / 2
            y = (min(t1.max_y, t2.max_y) + max(t1.min_y, t2.min_y)) / 2
            return (x, y)

        return False
