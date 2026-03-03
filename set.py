my_empty_set  = {}
my_new_empty_set = set()


print(type(my_empty_set))
print(type(my_new_empty_set))

my_set = {1, 2, 3, 4, 5} 
my_set.add(7)
print(my_set)
my_set.remove(2)
print(my_set)
my_set.discard(0)
print(my_set)

my_set.clear()
print(my_set)

my_set1 = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set1))
print(your_set.issuperset(my_set1))

print(my_set1 ^ your_set)