"""
Написать декоратор, который будет печатать на экран время работы функции (пользуемся datetime).
"""
import time


def outer(func): # декоратор для простых функций
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        finish = time.time()
        print(finish - start)
        return res
    return inner


def fact_decorator(func): # декоратор для рекурсии, не работает правильно(
    def inner(n):
        start = time.time()
        res = func(n)
        finish = time.time()
        print(finish - start)
        return res
    return inner


@fact_decorator
def test(n):
    time.sleep(1)
    if n == 1:
        return 1
    return test(n - 1) * n


@outer
def test_2(a, b):
    time.sleep(1)
    return a + b


print(test(3))
print(test_2(4, 4))
