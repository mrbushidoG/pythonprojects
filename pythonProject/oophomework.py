import math
from scipy.stats import linregress


class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        # return math.sqrt(((self.coor1[1] - self.coor1[0])**2) + ((self.coor2[1] - self.coor2[0])**2))
        return math.dist(self.coor1,self.coor2)

    def slope(self):
        return (self.coor2[1] - self.coor2[0])/(self.coor2[1] - self.coor2[0])

# class Cylinder:
#
#     def __init__(self,height=1, radius=1):
#         self.height = height
#         self.radius = radius
#
#     def volume(self):
#         return 3.14*(self.radius**2)*self.height
#
#     def surface_area(self):
#         return 2*(3.14*self.radius*self.height) + 2*(3.14*self.radius**2)
#
#
# cylinder = Cylinder(5,7)
#
# volume = cylinder.volume()
# surface_area = cylinder.surface_area()
#
# print(f"Volume is {volume} and the surface area is {surface_area}")
coordinate1 = (3,2)
coordinate2 = (8,10)
line = Line(coordinate1,coordinate2)

distance = line.distance()
slope = line.slope()

print(f"Distance {distance} and the slope is {slope}")