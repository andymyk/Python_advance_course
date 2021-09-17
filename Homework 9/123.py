from multiprocessing import Process
from datetime import datetime
#
class A:
    def first(self):
        s = [i for i in range(10 ** 8)]
    spis = []
    def __call__(self):
        for i in range(3):
            start = datetime.now()
            A.first(self)
            finish = datetime.now()
            res = finish - start

            print(f'Child: {res}')

class B:
    def first(self):
        s = [i for i in range(10 ** 8)]
    spis = []
    def __call__(self):
        for i in range(3):
            start = datetime.now()
            B.first(self)
            finish = datetime.now()
            res = finish - start
            print(f'Main: {res}')


if __name__ == '__main__':
    a = A()
    b = B()

    p1 = Process(target=a)
    p1.start()
    p1.join()
    b()
