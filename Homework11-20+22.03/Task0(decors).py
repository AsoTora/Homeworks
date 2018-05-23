from functools import wraps
import time


class Decorators(object):
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

    def decor3(self, f):
        """декоратор, проверяющий типы, переданных декорируемой функции, аргументов"""

        @wraps(f)
        def wrapp(*args, **kwargs):
            result = f(*args, **kwargs)
            print(*args)
            print('''Type of args, values for func {} are args: {},
                  values:{}'''.format(f.__name__, type(*args), [type(v) for v in kwargs.values()]))
            return result
        return wrapp

    def decor4(self, f):
        """декоратор, который кэширует результат работы функции,
        тем самым обеспечивает единственный вызов функции"""

        @wraps(f)
        def wrapp(*args, **kwargs):

            if wrapp.value is False:
                print(f.__name__ + " исполняется")
                f(*args, **kwargs)
                print(f.__name__ + " была исполнена")
                wrapp.value = True
                return wrapp.value
            return print('It\'s already finished')

        wrapp.value = False
        return wrapp


decor = Decorators()


@decor.decor1
@decor.decor2
@decor.decor3
@decor.decor4
def eratosph(n, k=None):
    not_prime = {j for i in range(2, n) for j in range(i*2, n, i)}
    return {i for i in range(2, n) if i not in not_prime}


if __name__ == '__main__':
    a1 = eratosph
    a1(100, k=200)
    a1(30, k='aaa')

