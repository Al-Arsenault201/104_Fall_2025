

class Shape:
    def area(self):
        # Base implementation (optional)
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


def print_area(shape: Shape):
    # Subtype polymorphism: different subclasses respond to area() differently
    print("Area:", shape.area())


# Subtype instances
r = Rectangle(4, 5)
c = Circle(3)

print_area(r)  # Area: 20
print_area(c)  # Area: 28.27431