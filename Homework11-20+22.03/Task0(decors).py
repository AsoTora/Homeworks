# Задача 0
from functools import wraps
import time


class Decorators():
    def decor0(self, func):
        """ декоратор 0, позволяющий вместе с результатом функции возвращать время ее работы """
        def wrapper(*arg):
            t1 = time.clock()
            res = func(*arg)
            t2 = time.clock()
            print('%0.3fms' % ((t2 - t1) * 1000.0))
            return res
        return wrapper

    def decor1(self, f):
        """ декоратор 1, позволяющий вместе с результатом функции возвращать время ее работы """

        @wraps(f)
        def wrapp(*args, **kwargs):
            time_start = round(time.time(), 5)
            result = f(*args, **kwargs)
            time_end = round(time.time(), 5)
            print("Time for func {} is {}".format(f.__name__, time_end - time_start))
            print("The", f.__name__, "result is: ", result)
            return result
        return wrapp

    def decor2(self, f):
        """ декоратор, позволяющий записывать время работы функции,
         имя функции и переданные ей параметры в текстовый файл """

        def wrapp(*args, **kwargs):
            time_start = round(time.time(), 5)
            result = f(*args, **kwargs)
            time_end = round(time.time(), 5)

            with open("decor_data.txt", "w") as fl:
                fl.write(" Func name is: {}\n Work time is: {}\n Args, kwargs are: {}\n The result: {}".format(
                    f.__name__, time_end - time_start, str(*args) + ", " + str(kwargs), result))
                return result
        return wrapp

    # TODO
    def decor3(self, f):
        """декоратор, проверяющий типы, переданных декорируемой функции, аргументов"""

        @wraps(f)
        def wrapp(*args, **kwargs):
            result = f(*args, **kwargs)
            print("Type of args, kwargs for func {}: {}, keys:{}, values:{}".format(f.__name__, type(*args))) ###))
            return result
        return wrapp

    def decor4(self, f):
        """декоратор, который кэширует результат работы функции,
        тем самым обеспечивает единственный вызов функции"""

        f.v = None
        if f.v is None:
            @wraps(f)
            def wrapp(*args, **kwargs):
                print(f.__name__ + " исполняется")
                f.v = f(*args, **kwargs)
                print(f.__name__ + " была исполнена")
                return f.v
            return wrapp 
        else:
            return print('It\'s already finished')


if __name__ == '__main__':
    decor = Decorators()

    @decor.decor1
    @decor.decor2
    @decor.decor3
    @decor.decor4
    def eratosp(n):
        not_prime = {j for i in range(2, n) for j in range(i*2, n, i)}
        return {i for i in range(2, n) if i not in not_prime}

    eratosp(100)
