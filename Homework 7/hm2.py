import random


class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        return str(self.matr)

    def __add__(self, other):
        result = [[self.matr[i][j] + other[i][j] for j in range
        (len(self.matr[0]))] for i in range(len(self.matr))]
        return result

    def __getitem__(self, item):
        return self.matr[item]



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


