import point as p
point1 = p.Point(3,4)
point2 = p.Point(2,7)
point3 = point1 + point2
print(point1)
print(point2)
print(point3)

import vector2d as v2d
vector = v2d.Vector2D(point1, point2)
print(vector)
print("norm = " + str(vector.norm()))
