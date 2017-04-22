class Vector2D:
    def __init__(self, point1=None, point2=None):
        self.point1 = point1
        self.point2 = point2
    def norm(self):
        from math import hypot
        return hypot(self.point1.x - self.point2.x,
                     self.point1.y - self.point2.y)
    def __str__(self):
        return "point1 : {}, point2 : {}".format(self.point1, self.point2)
