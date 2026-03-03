# Strings
my_str = 'Hello world'
"""
print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

msg = "it's a sunny day"
print(msg)
"""
# multiline string 

message = '''Hello Pearl, Is a wonderful day and I want to say happy new year'''
#Indexing
my_str = 'Hello world'
print(len(my_str))

print(my_str[0])
print(my_str[4])
print(my_str[-1])

# string concatenation
first_name ="Paul"
last_name = "Promise"

fullname = first_name + " " + last_name

print(fullname)

# foramted string
name = "Alice"
age = 23

formated_string = f"My name is {name}  and I am {age} years old"

print(type(formated_string))

# String slicing
new_str = "Hello World"

print(new_str[::-1])

# String Methods
message = " Hello World   "
print(message.replace('World', "Python"))

my_list = ['hello', 'world']
joined_list = ' '.join(my_list)
print(joined_list)



developer = "Naomi"

result = developer.endswith('N')

print(result)

print(4 + 2.4)