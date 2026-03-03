'''
Docstring for oop.mangling
class Example:
    def __init__(self):
        self._internal = 'I can be accessed from outside the class, but should not'
        self.__private = 'You cannot access me directly from outside the class'

obj = Example()

print(obj._internal) # I can be accessed from outside the class, but should not
print(obj.__private)  # AttributeError: 'Example' object has no attribute '__private'
'''
class Example:
    def __init__(self, internal, private):
        self._internal = internal
        self.__private = private
        
        