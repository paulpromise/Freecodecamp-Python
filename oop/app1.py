'''class Car:
    def __init__(self, brand,color):
        self.brand = brand
        self.color = color
        
car1 = Car('Toyota', 'red')

print("Car 1 Brand: ", car1.brand)
'''

class Walet:
    def __init__(self, balance):
        self.__balance = balance
    
    def __validate(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")
    
    def deposit(self, amount):
        self.__validate(amount)
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__validate(amount)
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        
    def get_balance(self):
        return self.__balance


account = Walet(0)
account.deposit(100)
print(account.get_balance())
account.withdraw(150)
print(account.get_balance())