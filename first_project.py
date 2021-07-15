import string
import json
import re
import random
import os



def main():
    menu()


def menu():
    print(f'''
Привет! Что вы хотите сделать?
1. Зарегистрировать нового пользователя
2. Просмотреть список пользователей
3. Импорт пользователей из файла
4. Выход''')
    print()
    choose = int(input('Выберите пункт: '))
    if choose == 1:
        return register()
    if choose == 2:
        return database()
    if choose == 3:
        return import_user()
    if choose == 4:
        print('Вы вышли из программы')
        exit()
    else:
        print('Не правильный выбор!')
        exit()


def register():
    user = get_name()
    phone_number = get_phone_number()
    email = get_email()
    password = get_password()
    full_user = {
        "name": user,
        "phone_number": phone_number,
        "email": email,
        "password": password,
    }
    return add_user(full_user)


def add_user(full_user):
    with open("test.json") as f:
        spisok = json.load(f)
    spisok.append(full_user)

    with open("test.json", "w") as f:
        data = json.dumps(spisok, indent=4)
        f.write(data)

    return menu()


def get_name():
    name = input('Введите ваше имя: ')
    if len(name) < 2:
        print('Слишком короткое имя. Повторите ввод.')
        return get_name()
    data = string.punctuation + string.digits
    for i in name:
        if i in data:
            print('У имени не может быть цифр или спец символов')
            return get_name()
    return name.title()


def get_phone_number():
    try:
        num = int(input("Введите номер телефона: "))
    except ValueError:
        print('В номере могут быть только цифри! Повторите ввод')
        return get_phone_number()
    phone = str(num)
    if len(phone) == 12 and phone.startswith('380'):
        return valid_phone_number(phone)
    elif len(phone) == 9:
        phone = '380' + phone[-9:]
        return valid_phone_number(phone)
    else:
        print('Невалидный номер. Повторите ввод')
        return get_phone_number()


def valid_phone_number(phone):
    with open("test.json") as f:
        spisok = json.load(f)
    for i in spisok:
        if i["phone_number"] == phone:
            print('Пользователь с таким номером телефона уже существует!')
            return menu()
    return phone


def get_email():
    email = input("Введите email: ")
    if len(email) < 6:
        print('Слишком короткий емейл. Повторите ввод')
        return get_email()
    if email.count("@") != 1:
        print("Неверный формат email.")
        return get_email()
    domain = email.split("@")[1]
    local = email.split("@")[0]
    for i in local:
        if i in string.punctuation:
            print('Неверный формат email')
            return get_email()
    if len(local) > 64:
        print('Слишком длинный емейл. Повторите ввод')
        return get_email()
    for i in domain:
        if i == '.':
            continue
        if i in string.punctuation:
            print("Неверный формат email.")
            return get_email()
    if len(domain.split(".")) < 2:
        print("Неверный формат email.")
        return get_email()
    return email


def get_password():
    pas = input("Введите пароль: ")

    if not password_valid(pas):
        return get_password()

    confirmed = input("Подтвердите пароль: ")
    if pas != confirmed:
        print("Пароли не совпадают.")
        return get_password()
    else:
        return pas


def password_valid(pas):
    if len(pas) < 8:
        print("Пароль должен быть минимум 8 знаков")
        return False
    if len(pas) < 8:
        print("Пароль должен быть минимум 8 знаков")
        return False
    elif re.search('[0-9]', pas) is None:
        print("У вас нет цифры")
        return False
    elif re.search('[A-Z]', pas) is None:
        print("У вас нет большой буквы")
        return False
    elif re.search('[a-z]', pas) is None:
        print("У вас нет маленькой буквы")
        return False
    elif re.search('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', pas) is None:
        print("У вас нет спецсимвола")
        return False
    return True

def import_user():
    p = os.path.abspath('test.json')
    return p


def database():
    with open("test.json") as f:
        data = json.load(f)
    count = len(data)
    print('''
1. Просмотреть количество зарегистрированных пользователей
2. Просмотреть всех зарегистрированных пользователей
3. Вывести подробную информацию о пользователе
4. Выход
''')
    choose = int(input('Что вы хотите сделать? '))
    if choose == 1:
        print(f'Всего зарегестрировано {count} пользователей'.format(count=count))
        s = input('Хотите сделать что то еще? Y or N ')
        if s.lower() == 'y':
            return database()
        else:
            exit()
    if choose == 2:
        for i in data:
            print(i['name'])
        print()
        s = input('Хотите сделать что то еще? Y or N ')
        if s.lower() == 'y':
            return database()
        else:
            exit()
    if choose == 3:
        user = input('О каком пользователе хотите вывести информацию? ')
        for i in data:
            if i["name"] == user:
                v = list(i.values())
                return new_database(v, i["phone_number"])
    if choose == 4:
        return exit()
    else:
        print('Не правильный выбор!')
        return database()


def new_database(v, phone):
    print(*v, sep='\n')
    print('''
1. Сбросить пароль (генерируется новый случайный пароль)
2. Удалить пользователя (необходимо подтвердить удаление)''')
    z = input('Что вы хотите сделать? ')
    with open("test.json") as f:
        spisok = json.load(f)
    if z == '1':
        for i in spisok:
            if i['phone_number'] == str(phone):
                i['password'] = pas_gen()
                print('Пароль сброшен! Новый пароль:', i['password'])
        with open("test.json", "w") as f:
            data = json.dumps(spisok, indent=4)
            f.write(data)
    if z == '2':
        zz = input('Вы уверены? Y / N ')
        if zz.lower() == 'y':
            for i in spisok:
                if i['phone_number'] == str(phone):
                    spisok.remove(i)

            with open("test.json", "w") as f:
                data = json.dumps(spisok, indent=4)
            f.write(data)
        else:
            database()

def pas_gen():
    data = string.digits + string.ascii_letters + string.punctuation
    while True:
        new_pass = ''
        for i in range(10):
            sym = random.choice(data)
            new_pass += sym
        for i in new_pass:
            if i.isdigit():
                continue
            if i.islower():
                continue
            if i.isupper():
                continue
            if i in string.punctuation:
                return new_pass


if __name__ == "__main__":
    main()
