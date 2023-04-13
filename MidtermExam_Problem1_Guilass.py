import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Perimeter(self):
        return 2 * self.radius * math.pi
    def Area(self):
        return (self.radius ** 2) * math.pi
    def display(self):
        print ("The Perimeter of the circle is: ",self.Perimeter())
        print("The Area of the circle is: ",self.Area())


radius = Circle (float(input("Radius of the circle: ")))
radius.display()