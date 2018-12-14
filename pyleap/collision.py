"""
判断2个基本图形是否发生碰撞，

如果没有碰撞，则返回False
如果碰撞，则返回其中一个碰撞的坐标点，如 {'x': 100, 'y': 200}

"""
from pyleap.mouse import mouse


__all__ = ['shape_clicked', 'CollisionMixin' ]

class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def shape_clicked(shape):
    shape.transform.update_points(shape.points)
    return point_in_points((mouse.x, mouse.y), shape.transform)

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

    return cross_count % 2



def points_in_points(s1, s2):
    for i in range(0, len(s1.points), 2):
        x = s1.points[i]
        y = s1.points[i+1]

        # outside the collide rect
        if(x < s2.min_x or x > s2.max_x or y < s2.min_y or y > s2.max_y):
            continue

        if(point_in_points((x, y), s2)):
            return P(x, y)

    return False

def lines_cross(s1, s2):
    for i in range(0, len(s1.points), 2):
        x1 = s1.points[i-2]
        y1 = s1.points[i-1]
        x2 = s1.points[i]
        y2 = s1.points[i+1]
        for i in range(0, len(s2.points), 2):
            x3 = s2.points[i-2]
            y3 = s2.points[i-1]
            x4 = s2.points[i]
            y4 = s2.points[i+1]
            p = line_cross(x1, y1, x2, y2, x3, y3, x4, y4)
            if p: return p

    return False

def line_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    """ 判断两条线段是否交叉 """
    # out of the rect
    if min(x1, x2) > max(x3, x4) or max(x1, x2) < min(x3, x4) or \
       min(y1, y2) > max(y3, y4) or max(y1, y2) < min(y3, y4):
        return False

    # same slope rate
    if ((y1 - y2) * (x3 - x4) == (x1 - x2) * (y3 - y4)):
        return False

    if cross_product(x3, y3, x2, y2, x4, y4) * cross_product(x3, y3, x4, y4, x1, y1) < 0 or \
       cross_product(x1, y1, x4, y4, x2, y2) * cross_product(x1, y1, x2, y2, x3, y3) < 0:
        return False

    # get collide point
    b1 = (y2 - y1) * x1 + (x1 - x2) * y1
    b2 = (y4 - y3) * x3 + (x3 - x4) * y3
    D = (x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1)
    D1 = b2 * (x2 - x1) - b1 * (x4 - x3)
    D2 = b2 * (y2 - y1) - b1 * (y4 - y3)

    return P(D1 / D, D2 / D)


def cross_product (x1, y1, x2, y2, x3, y3):
    """ 叉乘
    vector 1: x1, y1, x2, y2
    vector 2: x1, y1, x3, y3
    """
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)


class CollisionMixin():
    """ 碰撞图形
    将任意图形转换为多边形进行判断，图形需要拥有points属性

    按照以下步骤进行判断
    1. 如果图形的外接矩形没有碰撞，返回False
    2. 如果图形的点在目标图形内，返回这个点
    3. 如果图形的边和目标图形的边相交，返回相交点
    4. 返回False

    """

    def update_collision_rect(self):
        """ 获取外接矩形 """
        self.min_x = min(self.points[::2])
        self.max_x = max(self.points[::2])
        self.min_y = min(self.points[1::2])
        self.max_y = max(self.points[1::2])

    def collide(self, s2):
        """ 判断图形是否碰到了另外一个图形 """
        s1 = self
        if not (s1.points and s2.points):
            return False

        t1 = s1.transform
        t2 = s2.transform

        t1.update_points(s1.points)
        t2.update_points(s2.points)

        # 更新外接矩形
        t1.update_collision_rect()
        t2.update_collision_rect()

        # simple collide rect
        if not (t1.min_x < t2.max_x and t1.max_x > t2.min_x \
                and t1.min_y < t2.max_y and t1.max_y > t2.min_y):
            return False

        return points_in_points(t1, t2) or \
               points_in_points(t2, t1) or \
               lines_cross(t1, t2)

    def on_press(self, func):
        """ 当图形被点击时，触发func函数 """
        self._press = func

