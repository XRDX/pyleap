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

        s1.update_collision_rect()
        s2.update_collision_rect()

        if s1.min_x < s2.max_x and s1.max_x > s2.min_x \
                and s1.min_y < s2.max_y and s1.max_y > s2.min_y:
            x = (min(s1.max_x, s2.max_x) + max(s1.min_x, s2.min_x)) / 2
            y = (min(s1.max_y, s2.max_y) + max(s1.min_y, s2.min_y)) / 2
            return (x, y)

        return False
