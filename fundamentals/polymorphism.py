from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def get_area(self):
        pass


class Triangle(Shape):
    def __init__(self, x, y):
        super().__init__(x=x, y=y)

    def draw(self):
        res = ''
        for i in range(self.x):
            spaces = ' ' * i
            res += f'|{spaces}\ \n'
        res += '-' * self.x
        print(res)

    def get_area(self):
        return (self.x * self.y) / 2


class Square(Shape):
    def __init__(self, x, y):
        super().__init__(x=x, y=x)

    def draw(self):
        res, spaces = '', '  ' * self.x
        res += ' -' * self.x
        res += f'\n| {spaces}| \n' * self.y
        res += ' -' * self.x
        print(res)

    def get_area(self):
        return self.x * self.y


def get_shape_info(shape_obj_that_takes_on_many_forms):
    print(shape_obj_that_takes_on_many_forms.get_area())
    shape_obj_that_takes_on_many_forms.draw()


if __name__ == "__main__":
    triangle = Triangle(3, 3)
    square = Square(3, 3)
    get_shape_info(triangle)
    get_shape_info(square)
