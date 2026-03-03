from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
# Concrete class that will override the abstract method
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Another concrete class that will override the abstract method

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
class Monkey(Animal):
    def make_sound(self):
        return "Ooh Ooh Aah Aah!"
    
animals = [Dog(), Cat(), Monkey()]
for animal in animals:
    print(animal.make_sound())
    
dog = Animal() 
print(dog.make_sound())  # This will raise an error