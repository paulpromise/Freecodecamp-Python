# try:
#     name = input("Please Enter your name: ")
#     age = int(input("Please Enter your age: "))
#     print("Your name is {name} and {age}years")
# except TypeError:
#     print("Type error please enter the right input")
# except ValueError:
#     print("Value error! input require interger valuue")
  
  
    
try:
    number = int(input('Enter a number: '))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f'Error occurred: {e}')

