"""Напишите программу, содержащую описание стека и моделирующую работу стека, реализовав все указанные здесь методы.
Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. 
После выполнения каждой команды программа должна вывести одну строчку. """

# я так понял, через классы

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,n): # Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.
        self.stack.append(n)
        print("ok")

    def pop(self): # Удалить из стека последний элемент. Программа должна вывести его значение. 
        if len(self.stack) == 0:
            raise Exception("nothing to pop")
        return self.stack.pop(len(self.stack)-1)

    def back(self):
    	return self.stack[-1] # Программа должна вывести значение последнего элемента, не удаляя его из стека.

    def size(self): # Программа должна вывести количество элементов в стеке. 
        return len(self.stack)

    def clear(self): #  Программа должна очистить стек и вывести ok. 
    	print("clear")
    	return self.stack.clear()

    def exit(self): # Программа должна вывести bye и завершить работу.
    	print("bye")
    	return False


s = Stack()

s.push(3)
s.push(14)
print(s.size())
s.clear()
s.push(1)
print(s.back())
s.push(2)
print(s.back())
print(s.pop())
print(s.size())
print(s.pop())
print(s.size())
s.exit()


