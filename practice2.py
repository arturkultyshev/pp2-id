import math


class Point(object):
    def __init__(self, x, y):
        self.dy = None
        self.dx = None
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def shift(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.x = self.x + dx
        self.y = self.y + dy

    def distance(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
"""

    def __str__(self):
        return f'Класс точки. {self.get_x(), self.get_y()}'
"""

point1 = Point(10, 4)
point2 = Point(5, 12)

print(point1.distance(point2))
point1.shift(10, 1)
print(point1.distance(point2))
print(point2)
