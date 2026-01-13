from abc import ABC, abstractmethod

# -------------------------------------------------------
# ABSTRACT BASE CLASS
# -------------------------------------------------------
# Shape is an abstract class that defines a CONTRACT.
# Any class inheriting from Shape MUST implement:
#   1. area()
#   2. perimeter()
#
# Shape itself CANNOT be instantiated.
# -------------------------------------------------------

class Shape(ABC):

    @abstractmethod
    def area(self):
        """
        Abstract method for calculating area.
        Must be implemented by all subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method for calculating perimeter.
        Must be implemented by all subclasses.
        """
        pass


# -------------------------------------------------------
# CONCRETE CLASS IMPLEMENTATION
# -------------------------------------------------------
# Rectangle is a concrete subclass of Shape.
# Since it implements ALL abstract methods,
# it can be instantiated.
# -------------------------------------------------------

class Rectangle(Shape):

    def __init__(self, length, width):
        # Call parent class constructor (good practice)
        super().__init__()

        # Initialize rectangle dimensions
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate area of rectangle.
        Formula: length * width
        """
        return self.length * self.width

    def perimeter(self):
        """
        Calculate perimeter of rectangle.
        Formula: 2 * (length + width)
        """
        return 2 * (self.length + self.width)


# -------------------------------------------------------
# INVALID USAGE (COMMENTED OUT)
# -------------------------------------------------------
# Cannot create an object of an abstract class
# because it has unimplemented abstract methods.
#
# shape = Shape()
# TypeError:
# Can't instantiate abstract class Shape
# without an implementation for abstract method 'area'
# -------------------------------------------------------


# -------------------------------------------------------
# VALID USAGE
# -------------------------------------------------------
# Rectangle implements all abstract methods,
# so it can be instantiated safely.
# -------------------------------------------------------

r1 = Rectangle(5, 8)

# Calls the implemented area() method
print(r1.area())        # Output: 40

# Calls the implemented perimeter() method
print(r1.perimeter())   # Output: 26
