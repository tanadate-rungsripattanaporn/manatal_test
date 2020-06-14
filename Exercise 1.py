import math
class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
circle1=circle(7)
print('area of this circle =',circle1.area())
print('perimeter of this circle =',circle1.perimeter())