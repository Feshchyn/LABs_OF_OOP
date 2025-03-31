from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self._name = name  
    
    @abstractmethod
    def make_sound(self):
        pass  
    
    def get_name(self):
        return self._name  


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed  
    
    def make_sound(self):
        return f"{self._name} (Dog) says: Woof!"
    
    def get_breed(self):
        return self.__breed  


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.__color = color  
    
    def make_sound(self):
        return f"{self._name} (Cat) says: Meow!"
    
    def get_color(self):
        return self.__color  


animals = [Dog("Rex", "Labrador"), Cat("Whiskers", "Black"), Dog("Buddy", "Beagle")]


for animal in animals:
    print(animal.make_sound())
