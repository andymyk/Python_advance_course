from datetime import datetime
from threading import Thread
#
def first():
    start = datetime.now()
    s = [i for i in range(10 ** 8)]
    finish = datetime.now()
    res = finish - start
    print(f'Potoki: {res}')


def second():
    s = [i for i in range(10 ** 8)]

def func():
    for i in range(3):
        start = datetime.now()
        second()
        finish = datetime.now()
        res = finish - start
        print(f'Function: {res}')

th = Thread(target=first)
th2 = Thread(target=first)
th3 = Thread(target=first)
th.start()
th2.start()
th3.start()
func()