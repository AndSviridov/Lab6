class Vector(object):
    def __init__(self, x, y, z):
        self.crd = (x, y, z)

    def __add__(self, other):
        return Vector(x=self.crd[0]+other.crd[0], y=self.crd[1]+other.crd[1], z=self.crd[2]+other.crd[2])


a = Vector(x=10, y=2, z=4)
b = Vector(x=-5, y=-2, z=3)
c = a + b

print(c.crd)