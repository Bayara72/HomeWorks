"""1) Создайте класс Rectangle у которого в __init__ будут
length(длина) и width(ширина). Создайте методы find_area,
find_perimeter, draw_rectangle.
Первые два метода должны высчитывать площадь и периметр
прямоугольника, ну а послдений метод, “нарисовать”
фигуру. Например,квадрат с размером 3x3 должен выглядеть
так -
* * *
* * *
* * *"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def find_area(self):
        return self.length * self.width

    def find_perimeter(self):
        return 2 * (self.length + self.width)

    def draw_rectangle(self):
        for i in range(self.width):
            print(self.length * '* ')
        return self.length, self.width


Rec = Rectangle(5, 3)
print(f'Area : {Rec.find_area()}')
print(f'Perimeter : {Rec.find_perimeter()}')
Rec.draw_rectangle()
