import random


class Car:
    def __init__(self, max_speed, color, name):
        self.max_speed = max_speed
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
    speed = random.randint(10, 120)
    speed_limit = 60
    def show_speed(self):
        if TownCar.speed > TownCar.speed_limit:
            return f'Вы превысыли скорость! {TownCar.speed} км\ч'
        return f'Текущяя скорость автомобиля: {TownCar.speed} км\ч'


class WorkCar(Car):
    speed = random.randint(10, 100)
    speed_limit = 40
    def show_speed(self):
        if WorkCar.speed > WorkCar.speed_limit:
            return f'Вы превысыли скорость! {WorkCar.speed} км\ч'
        return f'Текущяя скорость автомобиля: {WorkCar.speed} км\ч'


class PoliceCar(Car):
    def __init__(self, max_speed, color, name):
        super().__init__(max_speed, color, name)
        self.is_police = True


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