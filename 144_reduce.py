# reduce() is NOT a built in Python function; so, need to import from functools

# SEE ZTM in UDEMY #144 reduce() It is well explained

from functools import reduce
my_list = [1, 2, 3]


def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):  # reduce has a function, sequence, initial. Function is accumulator. Sequence will be our list. Initial is what the accumulator acc is going to be
    print(acc, item)
    return acc + item


# reduce has a function, sequence, initial
# Note: We do not need the list anymore, because reduce() will do it for us; so it changes from print(list(reduce(accumulator, my_list, 0)))  to this at the front.
print(reduce(accumulator, my_list, 0))
print(my_list)

# OUTPUT IS:
# 01                0 because acc starts at 0, and 1 because item comes from my_list so 0 + 1 = 1
# 12                1 because the result acc + item returns into the acc, and 2 because 1 + 1 = 2
# 33                3 because 1 from sum above is fed into acc and item is 2 so  + 2 = 3
# 6                 6 because, acc fed from above is 3 and item from list is 3; so, 3 + 3 = 6
# [1, 2, 3]
