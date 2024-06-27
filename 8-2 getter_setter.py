import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.radius
    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 한다.")
        self.__radius = value


circle = Circle(10)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

print(circle.__radius)

circle.set_radius(2)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())