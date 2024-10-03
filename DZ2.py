class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self, distance):
        time = distance / self.speed
        return f"Час для переміщення {time:} годин."



class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def move(self, distance):
        return f"Автомобіль {self.brand} переміщується на {distance} км зі швидкістю {self.speed} км/год. " + super().move(distance)


class Bicycle(Vehicle):
    def __init__(self, speed, type_):
        super().__init__(speed)
        self.type_ = type_

    def move(self, distance):
        return f"Велосипед типу {self.type_} переміщується на {distance} км зі швидкістю {self.speed} км/год. " + super().move(distance)


class Airplane(Vehicle):
    def __init__(self, speed, airline):
        super().__init__(speed)
        self.airline = airline

    def move(self, distance):
        return f"Літак компанії {self.airline} переміщується на {distance} км зі швидкістю {self.speed} км/год. " + super().move(distance)


car = Car(90, '"Tesla"')
bicycle = Bicycle(20, '"Гірський"')
airplane = Airplane(740, '"Emirates"')

distance = 300

print ("-------=====================-------")
print(car.move(distance))                           #не знаю як виправити щоб друкувало нормально час(
print ("-------=====================-------")
print(bicycle.move(distance))
print ("-------=====================-------")
print(airplane.move(distance))
print ("-------=====================-------")
