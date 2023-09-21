import numbers


class Shape:

    def __init__(self):
        self.name = type(self).__name__

    def area(self) -> numbers:
        pass

    def __str__(self):  # name of tha class and curly braces toString
        return str(f'{type(self).__name__} {self.__dict__}')


class Square(Shape):

    def __init__(self, side: int):
        super().__init__()
        self.side = side


square = Square(5)

print(square)
print(square.area())



