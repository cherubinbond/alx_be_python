from math import pi

class Shape:
    """
    Base class representing a generic shape.
    """
    def area(self):
        """
        This method is not implemented in the base class and raises an error.
        Derived classes should override this method to calculate their specific area.
        """
        raise NotImplementedError("Subclasses must implement area() method")

class Rectangle(Shape):
    """
    Derived class representing a rectangle with length and width attributes.
    """
    def __init__(self, length, width):
        """
        Initializes a Rectangle instance with length and width.

        Args:
            length (int): The length of the rectangle.
            width (int): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the base class area() method to calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle (length times width).
        """
        return self.length * self.width

class Circle(Shape):
    """
    Derived class representing a circle with radius attribute.
    """
    def __init__(self, radius):
        """
        Initializes a Circle instance with radius.

        Args:
            radius (int): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the base class area() method to calculate the area of the circle.

        Returns:
            float: The area of the circle (pi times radius squared).
        """
        return pi * self.radius**2
from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
