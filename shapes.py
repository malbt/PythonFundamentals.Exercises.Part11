# Exercise 1


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square:

    def __init__(self):
        self.Rectangle = rectangle()

    import shapes
    rect = shapes.Rectangle(2, 4)
    rect.area()
    # line 27 AttributeError: partially initialized module 'shapes' has no attribute 'Square' (most likely due to a
    # circular import)
    square = shapes.Square(8)
    square.area()

    square.perimeter()
