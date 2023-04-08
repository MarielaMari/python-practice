# Map - very useful, simplifies code; IT IS A HIGHER ORDER FUNCTION (because it accepts another function in its parameter)

my_list = [1, 2, 3]


def multiply_by2(item):
    return item*2


print(list(map(multiply_by2, my_list)))
print(my_list)
