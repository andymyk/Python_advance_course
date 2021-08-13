import random


class Car:
    is_police = False
    def __init__(self, max_speed, color, name,is_police=False):
        self.speed = max_speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        return f'Машина марки {self.name} поехала'

    def stop(self):
        return f'Машина марки {self.name} остановилась'

    def turn(self, direction):
        return f'Машина марки {self.name} повернула {direction}'

    def show_speed(self):
        speed = random.randint(10,100)
        return f'Текущяя скорость автомобиля: {speed} км\ч'

    def check_car(self):
        if self.is_police == True:
            return 'Это полицейская машина'
        return 'Это не полицейская машина'

class TownCar(Car):
    def show_speed(self):
        speed = random.randint(10,100)
        if speed > 60:
            return f'Вы превысыли скорость! {speed} км\ч'
        return f'Текущяя скорость автомобиля: {speed} км\ч'


class WorkCar(Car):
    def show_speed(self):
        speed = random.randint(10,100)
        if speed > 40:
            return f'Вы превысыли скорость! {speed} км\ч'
        return f'Текущяя скорость автомобиля: {speed} км\ч'


class PoliceCar(Car):
    def check_car(self):
        self.is_police = True
        if self.is_police == True:
            return 'Это полицейская машина'
        return 'Это не полицейская машина'

a = WorkCar(max_speed=120, color='Red', name='Volvo')
b = PoliceCar(max_speed=100, color='Blue', name='Kia')
print(b.go())
print(a.go())
print(b.stop())
print(a.stop())
print(b.show_speed())
print(a.show_speed())
print(b.check_car())
print(a.check_car())