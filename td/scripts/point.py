class Point:
     def __init__(self, x=None, y=None):
          self.x = x
          self.y = y
     def  __str__(self):
          return "(x, y) = ({}, {})".format(self.x, self.y)
     def __add__(self, other):
          return Point(self.x+other.x, self.y+other.y)
