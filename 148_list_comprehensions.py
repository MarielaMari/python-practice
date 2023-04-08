# List Comprehensions is Unique for PYTHON! Syntax: my_list = [param for param in iterable]
# They save space but might not be very readable for other developers!

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# with list comprehensions looks like this:
# my_list = [param for param in iterable]

my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num*2 for num in range(0, 100)]
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]
print('---Here is my_list printed with List comprehensions:', my_list)
print('---Here is my_list2 using range(0, 100) printed with List comprehensions:', my_list2)
print('---Here is my_list3, where each num is *2 in range(0, 100) with List comprehensions:', my_list3)
print('---Here is my_list4, where we keep the SQUARED POSITIVE num IN RANGE(0, 100) with List comprehensions:', my_list4)
