"""
Написать декоратор, который будет печатать на экран время работы функции (пользуемся datetime).
"""
import time


def time_f(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        finish = time.time()
        print(finish - start)
    return inner

@time_f
def test(n):
    time.sleep(1)
    if n == 1:
        return 1
    return test((n - 1) * n)

@time_f
def test_2():
    time.sleep(1)
    print('www')

print(test(1))
test_2()