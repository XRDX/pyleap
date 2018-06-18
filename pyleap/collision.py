"""
collide(shape1, shape2)

Detect if shape1 hit shape2

"""

def update_collision_rect(shape):
    shape.min_x = min(shape.points[::2])
    shape.max_x = max(shape.points[::2])
    shape.min_y = min(shape.points[1::2])
    shape.max_y = max(shape.points[1::2])

def collide(s1, s2):
    if not (s1.points and s2.points):
        return False

    update_collision_rect(s1)
    update_collision_rect(s2)

    if s1.min_x < s2.max_x and s1.max_x > s2.min_x \
            and s1.min_y < s2.max_y and s1.max_y > s2.min_y:
        x = (min(s1.max_x, s2.max_x) + max(s1.min_x, s2.min_x)) / 2
        y = (min(s1.max_y, s2.max_y) + max(s1.min_y, s2.min_y)) / 2
        return (x, y)

    return False
