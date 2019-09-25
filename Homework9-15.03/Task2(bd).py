""" 
Задача 2
Реализовать программу с базой учащихся группы (данные хранятся в файле).
Записи по учащемуся: имя, фамилия, пол, возраст.
Программа должна предусматривать поиск по одному или нескольким полям базы.
Результат выводить в удобочитаемом виде с порядковым номером записи.
Скрипт программы должен принимать параметр, который определяет формат хранения и реализации БД:
в текстовом файле с определенной структурой; в файле json.
"""
import json
# import pdb
# pdb.set_trace()


class TXT(object):
    def __init__(self, filename=None):
        if not filename:  # if filename is None
            filename = input('Enter filename: ')
        try:  # необязательная проверка расширения файла
            if filename.split('.')[-1] != 'txt':
                print('Not a .txt file!')
                raise NotImplementedError
        except IndexError:
            print('Wrong filename')
            raise NotImplementedError

        self.filename = filename

    def search(self, param=None):
        """Поиск подмножества через issubset"""
        if not param:  # if param is None
            try:
                inp = str(input("Search param here: ")).lower().split(',')  # Andrew,18
                self.inp = set(inp)
            except ValueError:
                raise NotImplementedError
        self.inp = set(param.lower().split(','))
        print('Searching for:', self.inp)

        with open(self.filename) as f:
            for line in f.readlines():
                student = set(line.lower().split())
                if self.inp.issubset(student):
                    return print("Student info: {}".format(line))
        return print('No such student')


class JSON(object):
    def __init__(self):
        filepath = '/home/aso/studystuff/python130218/Homework9-15.03/students.json'
        filename, filext = os.path.splitext(filepath)

        if filext != '.json':  # необязательная проверка расширения файла
            print('Not a .json file!')
            raise NotImplementedError

        self.filename = str(filepath.split('/')[-1])  # последний эл-т в split'e
        self.filepath = filepath

        with open(self.filename) as f:
            data = json.load(f)
            self.data = data

    def search(self, someinput=None):
        """Поиск по сравнению множеств"""
        if not someinput:  # if someinput is None
            someinput = input('Search for; ')  # age=18,gender=m
        try:
            searchdata = {}  # a dict of the form {'name':'...', 'lastname':'...'}
            for i in someinput.split(','):
                k, v = i.split('=')
                searchdata[k] = v
        except ValueError:
            print("Missing some args")
            raise NotImplementedError

        for student in self.data:  # main func logic
            if set(searchdata.values()) <= set(self.data[student].values()):
                return print('Info: ', self.data[student])
        return print('No such student')


if __name__ == '__main__':
    try:
        a = TXT('studentsdata.txt')
        a.search('Andrew,18')
        a.search('56,Mark')
        print('***' * 5)
        b = JSON()
        b.search('age=18,gender=m')
        b.search('name=Mark,age=56')
        b.search('age=41')
    except NotImplementedError as e:
        print(e)
