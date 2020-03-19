class Rectangle:

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):

    def __init__(self, length):
        super(). __init__(length, length)


rect = Rectangle(2, 4)
print(rect.area())
# 8

square = Square(8)
print(square.area())
# 64

print(square.perimeter())
# 32
