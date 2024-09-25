class List:
    def __init__(self):
        self.list = []

    def addend(self, n):
        self.list.append(n)

    def delete(self, n):
        if int(n) < len(self.list):
            self.list.pop(int(n))
        else:
            print('Выходит за границы, введите правильный индекс')

    def reverse(self, n=int):
        if n == 0:
            self.list.reverse()
        elif n == 1:
            self.list = self.list[::-1]

    def double_list(self, n):
        if int(n) == 0:
            self.list.append([])
        elif int(n) == 1:
            self.list += self.list

    def index_list(self, n=int):
        print(self.list[n])

    def clear(self):
        self.list.clear()

    def print(self):
        print(self.list)

    def safe_list(self):
        return self.list

class Set:
    def __init__(self):
        self.set = set()
        self.set2 = set()

    def create_set_elements(self, list=[]):
        if self.set2 == set():
            for i in range(len(list)):
                self.set2.add(list[i])
        else:
            self.set2 = set()
            for i in range(len(list)):
                self.set2.add(list[i])

    def none_set(self):
        self.set = set()

    def add_elements(self, list=[]):
        for i in range(len(list)):
            self.set.add(list[i])

    def print_set(self, n):
        if n == 0:
            print(self.set)
        elif n == 1:
            print(self.set2)