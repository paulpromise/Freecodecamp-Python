class Dog:
    species = "French Bulldog" # Class attribute
    
    def __init__(self, name):
        self.name = name # Instance attribute

'''
print(Dog.species)
dog1 = Dog("jack")

print(dog1.name)
print(dog1.species)

dog2 = Dog("Tom")
print(dog2.name)    # Tom
print(dog2.species) # French Bulldog

'''

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        
    def describe(self):
        return f"This car is a {self.color} {self.model}"
        
car1 = Car("red", "Toyota Corolla") 
car1.describe()