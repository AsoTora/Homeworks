"""Задача 3
Реализовать программу с базой учащихся группы (данные хранятся в файле).
Записи по учащемуся должны быть представлены отдельным классом с полями: имя, фамилия, пол, возраст.
Программа должна предусматривать поиск по одному или нескольким полям базы.
Результат выводить в удобочитаемом виде с порядковым номером записи. Скрипт программы должен принимать параметр,
который определяет формат хранения и реализации БД: в текстовом файле с определенной структурой; в файле json.
"""
import json


class BaseFile(object):
    """
    Решение задачи с помощью staticmethods python3
    Скрипт является ригистратором создаваемых подклассов + метод фабрики их экземпляров
    """
    subclasses = {}  # == registered file_types

    @classmethod
    def register_subclass(cls, file_type):
        """При задании нового подкласса для нового расширения файлов
        этот декоратор добавляет его в словарь подклассов.
        Возвращает функцию decorator, которая принимает подкласс в качестве аргумента."""

        def decorator(subclass):
            cls.subclasses[file_type] = subclass
            return subclass
        return decorator

    @classmethod
    def create(cls, file_type, file_name):
        """
        'Фабрика' экземпляров класса. Если при создании указывается известный тип файла(расширение),
        то создается экземпляр такого класса с переданными аргументами
        """
        if file_type not in cls.subclasses:
            raise NotImplementedError('Unknown file extension {}'.format(file_type))
        return cls.subclasses[file_type](file_name)


@BaseFile.register_subclass('txt')
class TXT(BaseFile):

    def __init__(self, file_name):
        try:
            if file_name.split('.')[-1] != 'txt':
                raise NotImplementedError('Not a .txt file!')
        except IndexError:
            raise NotImplementedError('Wrong filename')
        self.file_name = file_name

    def search(self, param=None):
        """Поиск подмножества через issubset"""
        if not param:
            try:
                inp = str(input("Search param here: ")).lower().split(',')  # Andrew,18
                inp = set(inp)
            except ValueError:
                raise NotImplementedError
        inp = set(param.lower().split(','))
        print('Searching in {} for {}:'.format(self.file_name, inp))

        with open(self.file_name) as f:
            for line in f.readlines():
                student = set(line.lower().split())
                if inp.issubset(student):
                    return print("Student info: {}".format(line))
        return print('No such student')


@BaseFile.register_subclass('json')
class JSON(BaseFile):

    def __init__(self, file_name):
        try:
            if file_name.split('.')[-1] != 'json':
                raise NotImplementedError('Not a .json file!')
        except IndexError:
            raise NotImplementedError('Wrong filename')
        self.file_name = file_name

        with open(self.file_name) as f:
            data = json.load(f)
            self.data = data

    def search(self, inp=None):
        """Поиск по сравнению множеств"""

        if not inp:
            inp = input('Search for; ')  # name=Mark,age=56
        try:
            searchdata = {}
            for i in inp.split(','):
                k, v = i.split('=')
                searchdata[k] = v
        except ValueError:
            raise NotImplementedError("Missing some args")
        print('Searching in {} for {}:'.format(self.file_name, searchdata))

        for student in self.data:
            if set(searchdata.values()) <= set(self.data[student].values()):
                return print('Info: ', self.data[student])
        return print('No such student')


if __name__ == '__main__':
    try:
        a = BaseFile.create('txt', 'studentsdata.txt')
        a.search('Andrew,18')
        a.search('56,Mark')
        print('***' * 5)
        b = BaseFile.create('json', 'students.json')
        b.search('name=Mark,age=56')
        b.search('age=41')
        print('***' * 5)
    except NotImplementedError as e:
        print(e)

    try:
        с = BaseFile.create('unknown_ext', 'studentsdata.txt')
        c.search()
    except NotImplementedError as e:
        print(e)

    try:
        d = BaseFile.create('json', 'unknown_file')
        d.search()
    except NotImplementedError as e:
        print(e)
