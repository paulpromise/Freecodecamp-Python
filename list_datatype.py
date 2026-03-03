cities = ['Los Angeles', "London", "Tokyo"]
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers.extend(even_numbers)
print(numbers)

numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(30)
print(numbers)
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)
print(numbers)

numbers = [19, 2, 35, 1, 67, 41]

numbers.sort()
print(numbers)

numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

my_list = [1, 4, 2, 2, 7 ,23, 4, 3, 2]

print(my_list.count(1))