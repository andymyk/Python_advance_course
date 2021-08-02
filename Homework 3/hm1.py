def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def func(a, b, c):
    return a + b + c - min(a, b, c)

