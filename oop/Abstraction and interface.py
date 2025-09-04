from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def start_engine(self):
        print("Двигатель запустился")

    def stop_engine(self):
        print("Двигатель остановился")

    def move(self):
        print("Автомобиль начал движение")


class Ship(Transport):
    def start_engine(self):
        print("Двигатель запустился")

    def stop_engine(self):
        print("Двигатель остановился")

    def move(self):
        print("Корабль начал движение")


car = Car()
ship = Ship()

lst = [car, ship]

for transpot in lst:
    transpot.start_engine()
    transpot.stop_engine()
    transpot.move()