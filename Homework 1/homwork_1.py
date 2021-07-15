"""
Написать программу, которая запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом
и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
ранее сумме и после этого завершить программу.
"""

suma = list()

def main():
    some_text = input('Enter numbers separated by a space: ').split()
    some_func(some_text)

def some_func(some_text):
    total = 0
    count = 0
    for i in some_text:
        if i.isdigit():
            total += int(i)
        else:
            count += 1
    return check(total, count)


def check(total, count):
    suma.append(total)
    if count > 0:
        return print(f'The sum of entered numbers: {sum(suma)}')
    else:
        return print(f'The sum of entered numbers: {sum(suma)}'), main()


if __name__ == "__main__":
    main()
