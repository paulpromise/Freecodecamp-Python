# Week1
Python Variables;
Variables are used to store data values. In Python, you don't need to declare the type of variable explicitly. You can create a variable and assign a value to it using the equals sign (=).
example:
```python
x = 5
y = "Hello, World!"
print(x)
print(y)
```

# Python Data Types;
Python has several built-in data types, including:
- int: Integer numbers (e.g., 1, 2, 3) ie whole numbers.
- float: Floating-point numbers (e.g., 1.5, 2.3) ie decimal numbers.
- str: Strings (e.g., "Hello", 'World') ie character sequences.
- list: Ordered collection of items (e.g., [1, 2, 3])
- tuple: Immutable ordered collection of items (e.g., (1, 2, 3))
- dict: Key-value pairs (e.g., {"name": "Alice", "age": 25})
- bool: Boolean values (True or False)

# String Indexing
indexing in python in the process if working with individual characters in string.
for example
my_str = 'Hello world'

print(len(my_str)) # it will give length of string
print(my_str[0]) # it will give first character 'H'
print(my_str[8]) # it will give character at index 8 'r'
print(my_str[-1]) # it will give last character 'd'
print(my_str[-3]) # it will give third last character 'r'

# String Concatenation
String concatenation is the process of joining two or more strings together.
for example
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result) # it will print "Hello World"

# formatting in string
String formatting is the process of inserting values (variables) into a string.
for example
name = "Alice"
age = 25
formatted_str = f"My name is {name} and I am {age} years old."
print(formatted_str) # it will print "My name is Alice and I am 25 years old."

# string slicing
String slicing is the process of extracting a portion of a string using indexing.  
for example
my_str = "Hello, World!"
slice1 = my_str[0:5]  # it will give 'Hello'
slice2 = my_str[7:]   # it will give 'World!'
slice3 = my_str[:5]   # it will give 'Hello'
slice4 = my_str[::2]  # it will give 'Hlo ol!' ie the step methond
slice5 = my_str[::-1] # it will give '!dlroW ,olleH' ie reverse string

# String Methods
Python provides several built-in string methods to manipulate strings. Some common string methods include:
- lower(): Converts a string to lowercase.
- upper(): Converts a string to uppercase.
- capitalize(): Capitalizes the first character of a string.
- strip(): Removes leading and trailing whitespace.
- replace(old, new): Replaces occurrences of a substring with a new substring.
- split(separator): Splits a string into a list of substrings based on a separator.
- join(iterable): Joins a list of strings into a single string with a specified separator.
- strtartswith(prefix): Checks if the string starts with the specified prefix.
- endswith(suffix): Checks if the string ends with the specified suffix.
- find(substring): Returns the lowest index of the substring if found in the string.
- count(substring): Returns the number of occurrences of the substring in the string.
- isupper(): Checks if all characters in the string are uppercase.
- title(): Converts the first character of each word to uppercase.
for example
my_str = "  Hello, World!  "
print(my_str.lower())        # it will print "  hello, world!  "
print(my_str.upper())        # it will print "  HELLO, WORLD!  "
print(my_str.strip())        # it will print "Hello, World!"
print(my_str.replace("World", "Python")) # it will print "  Hello, Python!  "
print(my_str.split(","))     # it will print ['  Hello', ' World!  ']
print(" ".join(["Hello", "World"])) # it will print "Hello World"

# Arithmetic Operators
Arithmetic operators are used to perform mathematical operations on numbers. The common arithmetic operators in Python include:
- Addition (+): Adds two numbers.
- Subtraction (-): Subtracts one number from another.
- Multiplication (*): Multiplies two numbers.
- Division (/): Divides one number by another (returns a float).
- Floor Division (//): Divides one number by another and returns the largest integer less than

# interger Methods
Python provides several built-in methods to work with integers. Some common integer methods include:
- abs(): Returns the absolute value of an integer.
- pow(base, exp): Returns the value of base raised to the power of exp.
- divmod(a, b): Returns a tuple containing the quotient and remainder of dividing a by b.
- round(num, ndigits): Rounds a floating-point number to the specified number of decimal places.
- int(x): Converts a value x to an integer.
- bin(x): Converts an integer x to its binary representation as a string.
- hex(x): Converts an integer x to its hexadecimal representation as a string.
- oct(x): Converts an integer x to its octal representation as a string.
for example
num = -10
print(abs(num))          # it will print 10
print(pow(2, 3))        # it will print 8
print(divmod(10, 3))    # it will print (3, 1)
print(round(3.14159, 2)) # it will print 3.14
print(int(3.7))         # it will print 3
print(bin(10))          # it will print '0b1010' or equal to the result.
- Modulus (%): Returns the remainder of dividing one number by another.
- Exponentiation (**): Raises one number to the power of another.
for example
a = 10
b = 3
print(a + b)  # it will print 13
print(a - b)  # it will print 7
print(a * b)  # it will print 30
print(a / b)  # it will print 3.3333333333333335
print(a // b) # it will print 3
print(a % b)  # it will print 1
print(a ** b) # it will print 1000

# Augmented Assignment Operators
Augmented assignment operators are used to perform an operation and assign the result to a variable in a single step. The common augmented assignment operators in Python include:
- += : Adds a value to a variable and assigns the result to the variable.
- -= : Subtracts a value from a variable
- *= : Multiplies a variable by a value and assigns the result to the variable.
- /= : Divides a variable by a value and assigns the result to the variable.
- //= : Performs floor division on a variable by a value and assigns the result to the variable.
- %= : Calculates the modulus of a variable by a value and assigns the result to the variable.
- **= : Raises a variable to the power of a value and assigns the result to the variable.
for example
x = 10
x += 5  # equivalent to x = x + 5
print(x)  # it will print 15
x -= 3  # equivalent to x = x - 3
print(x)  # it will print 12
x *= 2  # equivalent to x = x * 2
print(x)  # it will print 24
x /= 4  # equivalent to x = x / 4
print(x)  # it will print 6.0
x //= 2  # equivalent to x = x // 2
print(x)  # it will print 3.0
x %= 2  # equivalent to x = x % 2
print(x)  # it will print 1.0
x **= 3  # equivalent to x = x ** 3
print(x)  # it will print 1.0

# List in Python
A list is a collection of items that are ordered and changeable. Lists are defined using square brackets [] and can contain items of different data types.
for example
my_list = [1, 2, 3, "Hello", 4.5]
print(my_list)  # it will print [1, 2, 3, 'Hello', 4.5]
print(my_list[0])  # it will print 1
print(my_list[3])  # it will print 'Hello'
my_list[1] = 10  # changing the value at index 1
print(my_list)  # it will print [1, 10, 3, 'Hello', 4.5]
my_list.append("World")  # adding an item to the end of the list
print(my_list)  # it will print [1, 10, 3, 'Hello', 4.5, 'World']
my_list.remove(3)  # removing an item from the list
print(my_list)  # it will print [1, 10, 'Hello', 4.5, 'World']

# List Methods
Python provides several built-in list methods to manipulate lists. Some common list methods include:
- append(item): Adds an item to the end of the list.
- insert(index, item): Inserts an item at a specified index.
- remove(item): Removes the first occurrence of an item from the list.
- pop(index): Removes and returns the item at the specified index (default is the last item).
- clear(): Removes all items from the list.
- index(item): Returns the index of the first occurrence of an item.
- count(item): Returns the number of occurrences of an item in the list.
- sort(): Sorts the items of the list in ascending order.
- reverse(): Reverses the order of the items in the list.
- extend(iterable): Extends the list by appending items from an iterable (e.g., another list).
- copy(): Returns a shallow copy of the list.
- sorted(): Returns a new sorted list from the items of the original list.

for example
my_list = [3, 1, 4, 2]
my_list.append(5)
print(my_list)  # it will print [3, 1, 4, 2, 5]
my_list.insert(1, 10)
print(my_list)  # it will print [3, 10, 1, 4, 2, 5]
my_list.remove(4)
print(my_list)  # it will print [3, 10, 1, 2, 5]
popped_item = my_list.pop()
print(popped_item)  # it will print 5
print(my_list)  # it will print [3, 10, 1, 2]
my_list.sort()
print(my_list)  # it will print [1, 2, 3, 10]
my_list.reverse()
print(my_list)  # it will print [10, 3, 2, 1]
my_list.extend([6, 7, 8])
print(my_list)  # it will print [10, 3, 2, 1, 6, 7, 8]  
copied_list = my_list.copy()
print(copied_list)  # it will print [10, 3, 2, 1, 6, 7, 8]  
sorted_list = sorted(my_list)
print(sorted_list)  # it will print [1, 2, 3, 6, 7, 8, 10]

# Tuple in Python
A tuple is a collection of items that are ordered and immutable (cannot be changed). Tuples are defined using parentheses () and can contain items of different data types.
for example
my_tuple = (1, 2, 3, "Hello", 4.5)
print(my_tuple)  # it will print (1, 2, 3, 'Hello', 4.5)
print(my_tuple[0])  # it will print 1
print(my_tuple[3])  # it will print 'Hello'

my_tuple[1] = 10  # This will raise a TypeError because tuples are immutable
print(my_tuple)  # it will print (1, 2, 3, 'Hello', 4.5)

# Tuple Methods
Python provides a few built-in tuple methods to work with tuples. The common tuple methods include:
- count(item): Returns the number of occurrences of an item in the tuple.
- index(item): Returns the index of the first occurrence of an item in the tuple.
- sorted(): Returns a new sorted list from the items of the tuple.
for example
my_tuple = (1, 2, 3, 2, 4)
print(my_tuple.count(2))  # it will print 2
print(my_tuple.index(3))  # it will print 2

# Looping through a Tuple
You can loop through the items of a tuple using a for loop.
for example
my_tuple = (1, 2, 3, "Hello", 4.5)
for item in my_tuple:
    print(item)

# List Comprehension
List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list or range) and optionally filtering items based on a condition.
for example

Creating a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # it will print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]   

# List Comprehension Using functions
You can also use functions within list comprehensions to manipulate the items as you create the new list.
- The map() function applies a given function to each item in an iterable (like a list) and returns a map object (which can be converted to a list).
for example
# Using map() to create a list of squares
def square(x):
    return x**2
squares_map = list(map(square, range(10)))
print(squares_map)  # it will print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# using the filter() function to filter items in an iterable based on a condition.
- The filter() function applies a given function to each item in an iterable and returns a filter object containing only the items for which the function returns True.
for example
# Using filter() to create a list of even numbers
def is_even(x):
    return x % 2 == 0
even_numbers = list(filter(is_even, range(10)))
print(even_numbers)  # it will print [0, 2, 4, 6, 8]

# lambda functions
Lambda functions are small anonymous functions defined using the lambda keyword. They can take any number of arguments but can only have a single expression. Lambda functions are often used in conjunction with functions like map() and filter().
for example
# Using a lambda function with map() to create a list of squares
squares_lambda = list(map(lambda x: x**2, range(10)))
print(squares_lambda)  # it will print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dictionary in Python
A dictionary is a collection of key-value pairs that are unordered, changeable, and indexed. Dictionaries are defined using curly braces {} and each key is separated from its value by a colon (:).

for example
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)  # it will print {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict["name"])  # it will print 'Alice'
my_dict["age"] = 26  # changing the value associated with the key "age"
print(my_dict)  # it will print {'name': 'Alice', 'age': 26, 'city': 'New York'}
my_dict["country"] = "USA"  # adding a new key-value pair
print(my_dict)  # it will print {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}
del my_dict["city"]  # removing a key-value pair
print(my_dict)  # it will print {'name': 'Alice', 'age': 26, 'country': 'USA'}

# Dictionary Methods
Python provides several built-in dictionary methods to manipulate dictionaries. Some common dictionary methods include:
- keys(): Returns a view object containing the keys of the dictionary.
- values(): Returns a view object containing the values of the dictionary.
- items(): Returns a view object containing the key-value pairs of the dictionary as tuples.
- get(key, default): Returns the value associated with the specified key. If the key is not found, it returns the default value (or None if not specified).
- pop(key, default): Removes the specified key and returns its value. If the key is not found, it returns the default value (or raises a KeyError if not specified).
- update(other_dict): Updates the dictionary with key-value pairs from another dictionary.
- clear(): Removes all key-value pairs from the dictionary.
for example
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict.keys())    # it will print dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # it will print dict_values(['Alice', 25, 'New York'])
print(my_dict.items())   # it will print dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# SET
A set is a collection of unique items that are unordered and unindexed. Sets are defined using curly braces {} or the set() function.
creating an empty set with empty curly braces {} will create an empty dictionary, not a set. To create an empty set, you should use the set() function.

example:
my_set = {1, 2, 3, 4, 5}
print(my_set)  # it will print {1, 2, 3, 4, 5}
my_empty_set = set()  # Correct way to create an empty set
print(my_empty_set)  # it will print set()

# Set Methods
Python provides several built-in set methods to manipulate sets. Some common set methods include:
- add(item): Adds an item to the set.
- remove(item): Removes an item from the set. Raises a KeyError if the item is not found.
- discard(item): Removes an item from the set if it exists. Does not raise  an error if the item is not found.
- pop(): Removes and returns an arbitrary item from the set. Raises a KeyError if the set is empty.
- clear(): Removes all items from the set.
- union(other_set): Returns a new set that is the union of the current set and another set.
- intersection(other_set): Returns a new set that is the intersection of the current set and another set.
- difference(other_set): Returns a new set that contains items in the current set but not in another set.
- symmetric_difference(other_set): Returns a new set that contains items in either the current set or another set but not in both.
- issubset(other_set): Checks if the current set is a subset of another set.
- issuperset(other_set): Checks if the current set is a superset of another set

for example
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # it will print {1, 2, 3, 4}
my_set.remove(2)
print(my_set)  # it will print {1, 3, 4}
my_set.discard(5)  # No error even though 5 is not in the set
print(my_set)  # it will print {1, 3, 4}
popped_item = my_set.pop()
print(popped_item)  # it will print an arbitrary item from the set
print(my_set)  # it will print the remaining items in the set
my_set.clear()
print(my_set)  # it will print set()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))               # it will print {1, 2, 3, 4, 5}
print(set1.intersection(set2))        # it will print {3}
print(set1.difference(set2))          # it will print {1, 2}
print(set1.symmetric_difference(set2)) # it will print {1, 2, 4, 5}

# Set Operations
Sets support various mathematical operations such as union, intersection, difference, and symmetric difference using operators.
for example
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Union: it will print {1, 2, 3, 4, 5}
print(set1 & set2)  # Intersection: it will print {3}
print(set1 - set2)  # Difference: it will print {1, 2}
print(set1 ^ set2)  # Symmetric Difference: it will print {1, 2, 4, 5}

# Module in Python
A module is a file containing Python code that defines functions, classes, and variables. Modules allow you to organize your code into separate files and reuse code across different programs. You can create your own modules or use built-in modules provided by Python.
To use a module, you need to import it using the import statement.
for example
# Importing the built-in math module
import math 
print(math.sqrt(16))  # it will print 4.0
print(math.pi)        # it will print 3.141592653589793

# Importing specific functions from a module
from math import factorial, pow
print(factorial(5))  # it will print 120
print(pow(2, 3))     # it will print 8.0

# importing a module with an alias
import math as m
print(m.sqrt(25))  # it will print 5.0

# Creating your own module
You can create your own module by saving your Python code in a file with a .py extension. For example, you can create a file named my_module.py with the following content:
```python
def greet(name):
    return f"Hello, {name}!"
```
You can then import and use your custom module in another Python file:
```python
import my_module
print(my_module.greet("Alice"))  # it will print "Hello, Alice!"
``` 
# Importing Specific Functions from a Module
You can import specific functions, classes, or variables from a module using the from keyword. This allows you to use the imported items directly without needing to prefix them with the module name.
for example
from math import sqrt, pi
print(sqrt(49))  # it will print 7.0
print(pi)        # it will print 3.141592653589793

# Importing All Items from a Module
You can import all items from a module using the asterisk (*) wildcard. However, this practice is generally discouraged as it can lead to namespace pollution and make the code less readable.
for example
from math import *
print(sqrt(64))  # it will print 8.0
print(cos(pi))   # it will print -1.0

# Python Standard Library
The Python Standard Library is a collection of modules and packages that come bundled with Python. It provides a wide range of functionalities, including file I/O, data manipulation, networking, and more. Some commonly used modules from the standard library include:
- os: Provides functions for interacting with the operating system.
- sys: Provides access to system-specific parameters and functions.
- datetime: Provides classes for manipulating dates and times.
- random: Provides functions for generating random numbers.
- json: Provides functions for working with JSON data.
- re: Provides functions for working with regular expressions.
- math: Provides mathematical functions and constants.
- collections: Provides specialized container datatypes like namedtuple, deque, Counter, etc.
- itertools: Provides functions for creating iterators for efficient looping.
- functools: Provides higher-order functions for functional programming.

for example
import os
print(os.getcwd())  # it will print the current working directory
import datetime
now = datetime.datetime.now()
print(now)  # it will print the current date and time
import random
print(random.randint(1, 10))  # it will print a random integer between 1 and 10
import json
data = {"name": "Alice", "age": 25}
json_data = json.dumps(data)
print(json_data)  # it will print '{"name": "Alice", "age": 25}'
import re
pattern = r'\d+'
text = "There are 3 apples and 5 oranges."
matches = re.findall(pattern, text)
print(matches)  # it will print ['3', '5']


# Exception handling
Exception handling is a mechanism in Python that allows you to handle errors gracefully without crashing the program. You can use the try, except, else, and finally blocks to manage exceptions.
- try: The code that may raise an exception is placed inside the try block.
- except: The code to handle the exception is placed inside the except block.
- else: The code inside the else block is executed if no exceptions are raised in the try
- finally: The code inside the finally block is executed regardless of whether an exception was raised or not.
for example
example:

try:
    num1 = int(input("Enter a number: ")) 
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print("Division was successful.")
finally:
    print("Execution completed.")

# Another example 
try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print('Division successful:', x)
finally:
    print('This block always runs.')

# catch multiple exceptions
try:
    number = int('abc')
    result = 10 / number
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")

# catching exeptions as alias
try:
    number = int('abc')
except ValueError as e:
    print('Error occurred:', e)

# This  will help you to return the actual error message or object for logging or debugging purposes.
#  Raise Statement 
The raise statement is used to manually raise an exception in Python. You can use it to trigger an exception when a certain condition is met.
for example
def divide_numbers(num1, num2):
    if num2 == 0:
        raise ValueError("Denominator cannot be zero.")
    return num1 / num2

example:

def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative

# Class in Python
A class is a blueprint for creating objects in Python. It defines the properties (attributes) and behaviors (methods) of the objects. You can create your own classes using the class keyword.
Attributes are variables that belong to a class, while methods are functions that belong to a class.
Here's the basic syntax of a class:

 
class ClassName:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self):
        # method code here

    def method2(self):
        # method code here

# Attributes and Methods
Attributes are variables that belong to a class, while methods are functions that belong to a class.
- Attributes are defined inside the __init__ method using the self parameter.
- Methods are defined as regular functions inside the class and also use the self parameter to access class attributes and other methods.
for example
class Dog:
    species = "French Bulldog" # Class attribute

    def __init__(self, name):
        self.name = name # Instance attribute

print(Dog.species) # French Bulldog

dog1 = Dog("Jack")
print(dog1.name)    # Jack
print(dog1.species) # French Bulldog

dog2 = Dog("Tom")
print(dog2.name)    # Tom
print(dog2.species) # French Bulldog

# Python Magic Methods
Magic methods, also known as dunder methods (double underscore methods), are special methods in Python that have double underscores at the beginning and end of their names. These methods allow you to define the behavior of your classes for built-in operations such as addition, subtraction, string representation, and more. 
Some common magic methods include:
- __init__(self, ...): Constructor method called when an object is created.
- __str__(self): Returns a string representation of the object.
- __repr__(self): Returns a detailed string representation of the object for debugging.
- __add__(self, other): Defines the behavior of the addition operator (+).
- __sub__(self, other): Defines the behavior of the subtraction operator (-).
- __mul__(self, other): Defines the behavior of the multiplication operator (*).
- __len__(self): Returns the length of the object.

# Handle Object Attributes Dynamically
You can use magic methods to handle object attributes dynamically. this includes getting, setting, and deleting attributes.
- __getattr__(self, name): Called when an attribute is not found in the usual way.
- __setattr__(self, name, value): Called when an attribute is set.
- __delattr__(self, name): Called when an attribute is deleted.
- __dir__(self): Returns a list of attributes and methods of the object.
-__hasattr__(self, name): Called to check if an attribute exists.

for example

getattr(object, attribute_name, default_value)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("John Doe", 30)
print(getattr(person, "name"))  # it will print "John Doe"
print(getattr(person, "age"))   # it will print 30
print(getattr(person, "gender", "Not Specified"))  # it will print "Not Specified"

# OOP (Object-Oriented Programming)
Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code. OOP focuses on encapsulating data and behavior within objects, promoting code reusability, modularity, and maintainability. The four main principles of OOP are:
1. Encapsulation: Bundling data (attributes) and methods (functions) that operate on the data within a single unit (class).
2. Inheritance: Creating new classes (subclasses) that inherit attributes and methods from existing classes (superclasses).
3. Polymorphism: The ability of different classes to be treated as instances of the same class through a common interface.
4. Abstraction: Hiding complex implementation details and exposing only the necessary parts of an object.

