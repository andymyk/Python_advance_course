import random


class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        return str(self.matr)

    def __add__(self, other):
        result = [map(sum, zip(*i)) for i in zip(self.matr, other)]
        return result

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        letter = self.matr[self.index]
        self.index += 1
        return letter




def matrix_create():
    a = []
    b = []
    size = int(input('Привет. Создадим матрицу чисел. Какого размера будет матрица? '))
    for i in range(size):
        for j in range(size):
            b.append(random.randint(1, 100))
        a.append(b)
        b = []
    return a


a = Matrix(matrix_create())
print(a)
b = Matrix(matrix_create())
print(b)

print(a+b)


