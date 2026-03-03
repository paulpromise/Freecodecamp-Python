class Animal:
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        return f"{self.name} makes a sound."
    
    
class Dog(Animal):
    bark = "woof!! woof!! woof!!"
    
    def sound(self):
        base = super().sound()
        return f"{self.name} barks: {self.bark}, {base}"

class Cat:
    def  speak(self):
        return "Meow! Meow! Meow!"
    
class Monkey:
    
    def speak(self):
        return "Ooh ooh aah aah!"
    
class Bird:
    
    def speak(self):
        return "Chirp! Chirp! Chirp!"
    

def animal_sound(animal):
   print(animal.speak())
   
animal_sound(Cat())
animal_sound(Monkey())
animal_sound(Bird())