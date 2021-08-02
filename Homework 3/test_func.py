from hm1 import func, fib
import pytest


@pytest.mark.parametrize('a, expected', [
    (3, 1),
    (5, 3),
    (6, 20)
])
def test_fib(a, expected):
    assert fib(a) == expected

ы
@pytest.mark.parametrize('a, exp_raises', [
    ('a', TypeError),
    (0, RecursionError),
])
def test_fib_raise(a, exp_raises):
    with pytest.raises(exp_raises):
        fib(a)


@pytest.mark.parametrize('a,b,c, expected_sum', [
    (1, 2, 3, 5),
    (2, 4, 2, 5)
])
def test_func(a, b, c, expected_sum):
    assert func(a, b, c) == expected_sum
