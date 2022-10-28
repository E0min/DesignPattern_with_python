import copy
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.z = 0

    def set_z(self):
        self.z = 18

p1 = Point(1,2)
p1. set_z()

p2 = copy.deepcopy(p1)
print(p2.x)
print(p2.y)

