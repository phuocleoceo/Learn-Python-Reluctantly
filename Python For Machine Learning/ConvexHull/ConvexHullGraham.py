from math import inf


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def GetCrossProduct(p1, p2, p3):
    return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)


def GetSlope(p1, p2):
    if p1.x == p2.x:
        return inf
    else:
        return 1.0*(p1.y-p2.y)/(p1.x-p2.x)


def ConvexHull(points):
    hull = []
    points.sort(key=lambda p: [p.x, p.y])
    start = points.pop(0)
    hull.append(start)
    points.sort(key=lambda p: (GetSlope(p, start), -(p.y), p.x))
    for pt in points:
        hull.append(pt)
        while len(hull) > 2 and GetCrossProduct(hull[-3], hull[-2], hull[-1]) < 0:
            hull.pop(-2)
    return hull


# MAIN
points = [Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4),
          Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)]
for p in ConvexHull(points):
    print("(", p.x, ",", p.y, ")")
