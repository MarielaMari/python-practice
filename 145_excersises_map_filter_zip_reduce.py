# 1 Capitalize all of the pet names and print the list

from functools import reduce
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(item):
    return item.upper()


print()
print(list(map(capitalize, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
print()
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 1, 2]
my_numbers.sort()


print(tuple(zip(my_strings, my_numbers)))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def over_fifty(items):
    return items > 50


print()
print(list(filter(over_fifty, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def accumulator(acc, item):
    return acc + item


print('---Reduce() ---')
print(reduce(accumulator, my_numbers, 0))
print(reduce(accumulator, scores, 0))
