from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def speak(self):
        pass

class Sparrow(Bird):
    def speak(self):
        print("I'm sparrow")

class Penguin(Bird):
    def speak(self):
        print("I'm penguin")


def make_to_speak(bird : Bird):
    bird.speak()

s = Sparrow()
p = Penguin()

lst_bird = [s,p]

for bird in lst_bird:
    make_to_speak(bird)