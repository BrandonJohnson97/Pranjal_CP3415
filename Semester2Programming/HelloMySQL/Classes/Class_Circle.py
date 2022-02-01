class Circle:
    def __init__(self, radius:float):
        self.radius = radius

    def get_Area(self):
        # pi r squared
        area = 3.14*self.radius**2
        return area

    def get_Circumference(self):
        # 2 pi R
        circumference = 2*3.14*self.radius
        return circumference

my_circle = Circle(radius= 3)
print(my_circle.get_Area())
print(my_circle.get_Circumference())
