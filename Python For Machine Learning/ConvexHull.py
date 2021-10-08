MAX = 50
NEG_INF = -0.0001


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def Determinant(p, q, r):
    d1 = q.x*r.y+p.x*q.y+p.y*r.x
    d2 = q.x*p.y+p.x*r.y+r.x*q.y
    return d1-d2


def ConvexHull(points):
    n = len(points)
    Lupp = [Point]*MAX
    Llow = [Point]*MAX
    for i in range(0, n-1):
        for j in range(n-2, i-2, -1):
            if (points[j].x >= points[j+1].x) and (points[j].y > points[j+1].y):
                points[j], points[j+1] = points[j+1], points[j]
    Lupp[0] = points[0]
    Lupp[1] = points[1]
    j1 = 1
    for i in range(2, n):
        j1 += 1
        Lupp[j1] = points[i]
        while j1 > 1 and Determinant(Lupp[j1-2], Lupp[j1-1], Lupp[j1]) > NEG_INF:
            Lupp[j1-1] = Lupp[j1]
            j1 -= 1
    Llow[0] = points[n-1]
    Llow[1] = points[n-2]
    j2 = 1
    for i in range(n-3, -1, -1):
        j2 += 1
        Llow[j2] = points[i]
        while j2 > 1 and Determinant(Llow[j2-2], Llow[j2-1], Llow[j2]) > NEG_INF:
            Llow[j2-1] = Llow[j2]
            j2 -= 1
    for i in range(0, j2-2):
        Lupp[j1+i] = Llow[i]
    n2 = j1+j2-2
    print(">> Convex hull : ")
    for i in range(0, n2):
        print("(", Lupp[i].x, ",", Lupp[i].y, ")")


# MAIN
points = [Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4),
          Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)]
ConvexHull(points)

# 03 44 31 00
