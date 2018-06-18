"""
collide(shape1, shape2)

Detect if shape1 hit shape2

"""
def point_in_points(p, s2):
    x = p[0]
    y = p[1]
    cross_count = 0
    for i in range(0, len(s2.points), 2):
        x1 = s2.points[i-2]
        y1 = s2.points[i-1]
        x2 = s2.points[i]
        y2 = s2.points[i+1]
        if (x1 < x and x2 < x) or (y1-y)*(y2-y) > 0 or (y1==y2) or (y2==y):
            continue
        cross_x = x1 - (x1-x2)*(y1-y)/(y1-y2)
        if(cross_x >= x):
            cross_count += 1

    if cross_count %2 == 1:
        return True
    else:
        return False


def points_in_points(s1, s2):
    for i in range(0, len(s1.points), 2):
        x = s1.points[i]
        y = s1.points[i+1]

        # outside the collide rect
        if(x < s2.min_x or x > s2.max_x or y < s2.min_y or y > s2.max_y):
            continue

        if(point_in_points((x, y), s2)):
            return (x, y)

    return False

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

        # simple collide rect
        if not (t1.min_x < t2.max_x and t1.max_x > t2.min_x \
                and t1.min_y < t2.max_y and t1.max_y > t2.min_y):
            return False

        return points_in_points(t1, t2) or points_in_points(t2, t1)

        return False


