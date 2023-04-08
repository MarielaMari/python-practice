# SET comprehensions are the same as list comprehenstion, just replace [] with {}:

my_set = {char for char in 'hello'}
my_set2 = {num for num in range(0, 100)}
my_set3 = {num*2 for num in range(0, 100)}
my_set4 = {num**2 for num in range(0, 100) if num % 2 == 0}
print('---Here is my_list printed with List comprehensions:', my_set)
print('---Here is my_list2 using range(0, 100) printed with List comprehensions:', my_set2)
print('---Here is my_list3, where each num is *2 in range(0, 100) with List comprehensions:', my_set3)
print('---Here is my_list4, where we keep the SQUARED POSITIVE num IN RANGE(0, 100) with List comprehensions:', my_set4)


# DICTIONARY COMPREHENSIONS:
simple_dict = {
    "a": 1,
    "b": 2
}
# Common in python to replace key with "k" and value with 'v'! First part is the action, second the loop
my_dict = {key: value**2 for key, value in simple_dict.items() if value %
           2 == 0}

print("\n ---Dictionary Comprehensions: \n", my_dict)
