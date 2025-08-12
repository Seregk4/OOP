from abc import ABC, abstractmethod


class Flyable():
    def fly(self):
        print("I'm flying!")

class Swimmable():
    def swim(self):
        print("I'm swimming!")

class Duck(Flyable, Swimmable):
    def make_sound(self):
        print("Quack!")


duck1 = Duck()

duck1.fly()
duck1.swim()
duck1.make_sound()


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    
    def speak(self):
        print("Woof!")
    
    def move(self):
        print("Dog run")

class Bird(Animal, Flyable):
    
    def speak(self):
        print("Tweet!")
    
    def move(self):
        self.fly()
    
    def fly(self):
        print("Bird fly")

class Fish(Animal, Swimmable):
    
    def speak(self):
        print("...")
    
    def move(self):
        self.swim()
    
    def swim(self):
        print("Fish swim")

dog = Dog()
bird = Bird()
fish = Fish()

lst = [dog,bird, fish]

for animal in lst:
    animal.speak()
    animal.move()