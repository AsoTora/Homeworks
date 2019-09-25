"""
Задача 0
Требуется написать программу для генерации и проверки контрольных сумм у файлов.

Входные данные
Файл-манифест – текстовый файл, в котором содержится информация о контрольных суммах для некоторого набора файлов.
Структура:

<имя_файла_1>:<контрольная_сумма_для_файла_1>
<имя_файла_2>:<контрольная_сумма_для_файла_2>
<имя_файла_3>:<контрольная_сумма_для_файла_3>

Задание
Сама программа должна иметь возможность работы в двух режимах:

Режим 1. Подсчет контрольной суммы для заданного набора файлов и генерация файла-манифеста.
На вход программы в качестве аргументов командной строки подается набор имён файлов.
Для каждого из этих файлов программа должна осуществить подсчёт контрольной суммы и занести информацию
 об имени файла и соответствующей ему контрольной сумме в файл-манифест.

Режим 2. Проверка целостности файлов.
На вход программы в качестве аргумента командной строки подаётся файл-манифест.
Для каждого из файлов, указанных в файле-манифесте, необходимо осуществить подсчёт контрольной суммы,
сравнить с той, что указана в манифесте, выдать в консоль результат о совпадении (ОК) или несовпадении (FAILED) значений

Режим работы программы задается ключом, переданным как аргумент командной строки.
Для первого режима можно использовать ключ --calc, для второго — --check.

Пример запуска:

> checksum.py --calc <имя_файла_1> ... <имя_файла_N>

Вывод:

> checksum for <имя_файла_1> calculated
...
> checksum for <имя_файла_N> calculated

Проверка целостности файлов.
<название_бинарника> --check <имя_файла_манифеста>

Вывод:

> <имя_файла_1> : <OK/FAILED>
...
> <имя_файла_N> : <OK/FAILED>
"""
from hashlib import sha256  # encryption func
import os
import sys  # terminal


class File(object):
    def __init__(self, filename):
        self.name = filename
        self.openfile = open(filename)

    def close(self):
        return self.openfile.close()

    def __str__(self):
        return self.name


class Hash(object):
    def __init__(self, otherfile):
        self.file_to_hash = otherfile.openfile
        self.hash = self.dict_hash(otherfile)

    def create_hash(self):
        hashed = sha256()
        for line in self.file_to_hash:
            hashed.update(line.encode())
        return hashed.hexdigest()

    def dict_hash(self, other):
        hash_dict = other.name + ': ' + self.create_hash()
        return hash_dict

    def __str__(self):
        return str(self.hash)


class Service:
    def __init__(self, hash_dict, db_name):
        self.hashed = hash_dict.hash.split(': ')
        self.database = db_name

    def write(self):
        with open(self.database, 'a+') as f:
            f.write(": ".join(self.hashed) + '\n')
            print("checksum for {} calculated".format(self.hashed[0]))

    def compare(self):
        list_hash = self.hashed
        with open(self.database) as db:
            for line in db:
                key_val = line.split(': ')
                if key_val[0] == list_hash[0]:
                    last_hash = key_val
            try:
                if last_hash[1][:-1] == list_hash[1]:  # Delete '/n'
                    print("{} is OK".format(last_hash[0]))
                else:
                    print("{} is FAILED".format(last_hash[0]))
            except UnboundLocalError:
                print('No match count...')


DATABASE = 'result.txt'
if not os.path.isfile(DATABASE):
    open('result.txt', 'w').close()


def working_with_files(files, func):
    for file in files:
        this_file = File(file)
        hash_of_file = Hash(this_file)
        this_file.close()
        obj = Service(hash_of_file, DATABASE)
        make_mission = getattr(obj, func)
        make_mission()


if __name__ == '__main__':
    Commands = {'--calc': 'write', '--check': 'compare'}
    files = sys.argv[2:]
    func = Commands[sys.argv[1]]
    working_with_files(files, func)
