
import math

# Tvar:
#   - obvod
#   - plocha

class Square:
    def __init__(self, side):
        self.side = side

##    def get_perimeter(self):
##        return self.side * 4
##    def set_perimeter(self, value):
##        self.side = value / 4
##    perimeter = property(get_perimeter, set_perimeter)
##
##    def perimeter(self):
##        return self.side * 4
##    perimeter = property(perimeter)
##
##    @property
##    def perimeter(self):
##        return self.side * 4
##

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, side):
        if type(side) not in (int, float):
            raise TypeError("side must be integer")
        if not side > 0:
            raise ValueError("side must be positive")
        self._side = side

    @property
    def perimeter(self):
        return self.side * 4

    @perimeter.setter
    def perimeter(self, value):
        self.side = value / 4

    @property
    def area(self):
        return self.side ** 2

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        #return 5
        s = self.perimeter / 2
        return math.sqrt(
             s *
            (s - self.a) *
            (s - self.b) *
            (s - self.c))

##try:
##    area = Triangle(1, 2, 4).area()
##except ValueError:
##    pass
##else:
##    raise Exception("expected a ValueError")

import pytest
with pytest.raises(ValueError):
    area = Triangle(1, 2, 4).area

shapes = [Square(4), Square(6), Triangle(1, 2, 2), Square(1)]
for shape in shapes:
    # polymorfismus
    area = shape.area
    print(area)

# Test class Square
t = Triangle(3, 4, 5)
assert t.perimeter == 12
assert t.area == 6

s = Square(1)
assert s.side == 1
assert s.perimeter == 4
assert s.area == 1

s = Square(2)
assert s.side == 2
assert s.perimeter == 8
assert s.area == 4