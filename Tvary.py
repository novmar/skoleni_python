## interface

# tvar:
# - obvod
# - plocha
# Ctverec:
# - delka strany
#
import math,pytest
class tvar():
    pass

class Ctverec(tvar):
    """

    """
    def __init__(self,side):
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self,side):
        if type(side) not in (int,float):
            raise TypeError("Strana musi byt cislo")
        if side <=0:
            raise ValueError ("Strana musi byt vetsi nez 0")
        self._side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def obvod(self):
        return 4 * self.side

class Trojuhelnik(tvar):
    def __init__(self,a,b,c):
        if (a+b<=c) or (a+c<=b) or (b+c<=a):
            raise ValueError ("to nebude trojuhelnik")

        self.a=a
        self.b=b
        self.c=c
    @property
    def area(self):
        return self.a+self.b+self.c
    @property
    def plocha(self):
        """

        """
        s=self.area/2
        return math.sqrt(
            s * (s-self.a) *
            (s - self.b) *
            (s - self.c)
        )

shapes=[ Ctverec(4),Ctverec(10),Trojuhelnik(12,13,14),Trojuhelnik(4,2,3)]
for shape in shapes:
    area=shape.area
    print (f"plocha je {area}")



t=Trojuhelnik(3,4,5)
assert t.area == 12
assert t.plocha == 6

# test classs square
s = Ctverec(1)
assert s.side == 1
assert s.obvod == 4
assert s.area == 1
with pytest.raises(ValueError) as excinfo:
    s=Ctverec(-2)


s = Ctverec(5)
print(s.side)
print(s.obvod)
isinstance(s,tvar)
#s = Ctverec(0)
