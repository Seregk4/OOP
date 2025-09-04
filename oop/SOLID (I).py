from abc import ABC, abstractmethod


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Runable(ABC):
    @abstractmethod
    def run(self):
        pass

class Swimable(ABC):
    @abstractmethod
    def swim(self):
        pass

class Lion(Runable):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"lion {self.name}")



lion1 = Lion("Symba")

lion1.run()