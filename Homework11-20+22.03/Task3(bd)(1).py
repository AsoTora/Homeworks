"""Задача 3
Реализовать программу с базой учащихся группы (данные хранятся в файле).
Записи по учащемуся должны быть представлены отдельным классом с полями: имя, фамилия, пол, возраст.
Программа должна предусматривать поиск по одному или нескольким полям базы.
Результат выводить в удобочитаемом виде с порядковым номером записи. Скрипт программы должен принимать параметр,
который определяет формат хранения и реализации БД: в текстовом файле с определенной структурой; в файле json.
"""
import json
# import pdb
# pdb.set_trace()


# First method

class BaseFile(object):
    """
    A 'wrapper' class that overload its __new__() method
    to return instances of the specialized sub-classes
    """

    def __new__(cls, filename):
        """
        Called to create a new instance of class cls. __new__() is a static method (special-cased so you need
         not declare it as such) that takes the class of which an instance was requested as its first argument.
        The remaining arguments are those passed to the object constructor expression (the call to the class).
        The return value of __new__() should be the new object instance (usually an instance of cls).
        """

        try:
            cls.file_ext = filename.split('.')[1]  # students.json, studentsdata.txt
        except IndexError:
            raise NotImplementedError('Files should have extension!')

        if cls.file_ext == 'txt':
            return TXTFile(filename)  # создаст экземпляр класса TXTFile, передав ему filename
        elif cls.file_ext == 'json':
            return JSONFile(filename)  # создаст экземпляр класса JSONFile, передав ему filename
        else:
            raise NotImplementedError('Unknown file ext')


class TXTFile(object):
    """.txt files class"""

    def __init__(self, filename):
        self.filename = filename

    def search(self, param=None):
        """
        Поиск подмножества через issubset
        Ввод параметров тут, чтобы не перекрывать создание экземпляров базовым классом
        """

        if not param:
            try:
                inp = str(input("Search param here: ")).lower().split(',')  # Andrew,18
                inp = set(inp)
            except ValueError:
                raise NotImplementedError
        inp = set(param.lower().split(','))
        print('Searching in "{}" for {}:'.format(self.filename, inp))

        with open(self.filename) as f:
            for line in f.readlines():
                student = set(line.lower().split())
                if inp.issubset(student):
                    return print("Student info: {}".format(line))
        return print('No such student')


class JSONFile(object):
    """.json files class"""

    def __init__(self, filename):
        with open(filename) as f:
            data = json.load(f)
            self.data = data  # dicts with students info
        self.filename = filename

    def search(self, inp=None):
        """Поиск по сравнению множеств
        Ввод параметров тут, чтобы не перекрывать создание экземпляров базовым классом
        """

        if not inp:
            inp = input('Search for; ')  # age=18,gender=m

        try:
            search_data = {}
            for i in inp.split(','):
                k, v = i.split('=')
                search_data[k] = v
        except ValueError:
            raise NotImplementedError("Missing some args")
        print('Searching in "{}" for {}:'.format(self.filename, search_data))

        for student in self.data:
            if set(search_data.values()) <= set(self.data[student].values()):
                return print('Info: ', self.data[student])
        return print('No such student')


if __name__ == '__main__':
    try:
        BaseFile('students.json').search('age=18,gender=m')
        print('***' * 5)
        BaseFile('studentsdata.txt').search('Andrew,18')
        BaseFile('somefiletocheck').search()
    except NotImplementedError as e:
        print(e)
