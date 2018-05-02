"""Задача 2
 Реализовать программу подсчета площади, периметра, #объема геометрических фигур
(треугольник, прямоугольник, квадрат, трапеция, окружность). 
 Если одна из фигур не поддерживает вычисление одного из свойств, в
программе должно быть вызвано исключение с человеко-читабельным сообщением и корректно обработано.
"""
from math import pi


class RandomFigure():  # родительский класс, площадь и периметр
    def __init__(self):
        self.area = 0
        self.perimetr = 0

    def getarea(self):
        """геттер, чтобы не доставать площадь напрямую"""
        return self.area

    def getper(self):
        """геттер, чтобы не доставать периметр напрямую"""
        return self.perimetr

    def task(self, num=None):
        """метод вызова реализации задания"""
        classes = {0: Square, 1: Triangle, 2: Rectangle, 3: Trapetion, 4: Circle}
        print({0: "Square", 1: "Triangle", 2: "Rectangle", 3: "Trapetion", 4: "Circle"})

        if num is None:
            try:
                num = int(input("Choose num: "))
                return print(classes[num]())
            except ValueError as e:
                print(e)
                raise NotImplementedError
        return print(classes[num]())

    def __str__(self):
        return "The area of the {} is {}, the perimetr is {}".format(
            self.__class__.__name__, self.getarea(), self.getper())


class Square(RandomFigure):
    def __init__(self):
        super().__init__()  # получение конструктора(инициализатора) родительского класса

        try:
            a = int(input("Enter side: "))
            self.area = a * a
            self.perimetr = a * 4
        except ValueError:
            print("You entered not an int!")
            raise NotImplementedError


class Triangle(RandomFigure):
    def __init__(self):
        super().__init__()  # получение конструктора(инициализатора) родительского класса

        try:
            a1 = float(input("Enter side 1: "))
            a2 = float(input("Enter side 2: "))
            a3 = float(input("Enter side 3: "))
            p = float((a1 + a2 + a3) / 2)
            self.area = (p * (p - a1) * (p - a2) * (p - a3)) ** 0.5
            self.perimetr = p * 2
        except ValueError:
            print("You entered not an int!")
            raise NotImplementedError


class Rectangle(RandomFigure):
    def __init__(self):
        super().__init__()  # получение конструктора(инициализатора) родительского класса

        try:
            a1 = float(input("Enter side 1: "))
            a2 = float(input("Enter side 2: "))
            self.area = a1*a2
            self.perimetr = 2*a1 + 2*a2

        except ValueError:
            print("You entered not an int!")
            raise NotImplementedError


class Trapetion(RandomFigure):
    def __init__(self):
        super().__init__()  # получение конструктора(инициализатора) родительского класса
        try:
            a = float(input("Enter side 1: "))
            b = float(input("Enter side 2: "))
            c = float(input("Enter side 3: "))
            d = float(input("Enter side 4: "))
            self.perimetr = a + b + c + d
            area = (a+b)/2 * ((c**2 - (((b-a)**2 + c**2 - d**2) / (2*(b-a)))**2)**0.5)
            self.area = area
        except ValueError:
            print("You entered not an int!")
            raise NotImplementedError

        except ZeroDivisionError:
            print("Sorry, cant calculate this during the ZeroDivisionError")
            raise NotImplementedError


class Circle(RandomFigure):
    def __init__(self):
        super().__init__()  # получение конструктора(инициализатора) родительского класса

        try:
            r = float(input("Enter radius: "))
            self.area = pi * r ** 2
            self.perimetr = 2 * pi * r
        except ValueError:
            print("You entered not an num!")
            raise NotImplementedError


if __name__ == "__main__":
    try:
        a = RandomFigure()
        a.task()
    except NotImplementedError:
        print('Some errors')
