from math import sqrt, inf
from copy import deepcopy


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def Distance(p1, p2):
    return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))


def BruteForce(P, n):
    POINT1 = Point()
    POINT2 = Point()
    min_val = inf
    for i in range(n):
        for j in range(i + 1, n):
            if Distance(P[i], P[j]) < min_val:
                min_val = Distance(P[i], P[j])
                POINT1.x = P[i].x
                POINT1.y = P[i].y
                POINT2.x = P[j].x
                POINT2.y = P[j].y
    return min_val, POINT1, POINT2


def StripClosest(strip, size, d):
    POINT3 = Point()
    POINT4 = Point()
    min_val = d
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y - strip[i].y) < min_val:
            min_val = Distance(strip[i], strip[j])
            POINT3.x = strip[i].x
            POINT3.y = strip[i].y
            POINT4.x = strip[j].x
            POINT4.y = strip[j].y
            j += 1

    return min_val, POINT3, POINT4


def ClosestUtil(P, Q, n):
    global PR1
    global PR2

    if n <= 3:
        return BruteForce(P, n)

    mid = n // 2
    midPoint = P[mid]

    Pl = P[:mid]
    Pr = P[mid:]

    dl, POINT1, POINT2 = ClosestUtil(Pl, Q, mid)
    dr, POINT3, POINT4 = ClosestUtil(Pr, Q, n - mid)

    if dl < dr:
        PR1.x = POINT1.x
        PR1.y = POINT1.y
        PR2.x = POINT2.x
        PR2.y = POINT2.y
    else:
        PR1.x = POINT3.x
        PR1.y = POINT3.y
        PR2.x = POINT4.x
        PR2.y = POINT4.y

    d_min = min(dl, dr)

    stripP = []
    stripQ = []
    lr = Pl + Pr
    for i in range(n):
        if abs(lr[i].x - midPoint.x) < d_min:
            stripP.append(lr[i])
        if abs(Q[i].x - midPoint.x) < d_min:
            stripQ.append(Q[i])

    stripP.sort(key=lambda point: point.y)

    strcls_a, POINT1, POINT2 = StripClosest(stripP, len(stripP), d_min)
    strcls_b, POINT3, POINT4 = StripClosest(stripQ, len(stripQ), d_min)
    min_a = min(d_min, strcls_a)
    min_b = min(d_min, strcls_b)

    return min(min_a, min_b)


def Closest(P, n):
    P.sort(key=lambda point: point.x)
    Q = deepcopy(P)
    Q.sort(key=lambda point: point.y)
    return ClosestUtil(P, Q, n)


# MAIN
input = [Point(2, 2), Point(15, 30), Point(20, 10),
         Point(7, 2), Point(12, 7), Point(5, 4)]
PR1 = Point()
PR2 = Point()
d_min = Closest(input, len(input))
print(">> Khoang cach ngan nhat can tim la la : ", d_min)
print("A : (", PR1.x, ",", PR1.y, ")")
print("B : (", PR2.x, ",", PR2.y, ")")
