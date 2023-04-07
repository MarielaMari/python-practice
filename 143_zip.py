# zip() works like a zipper... we need 2 codes to zip them together
# Can be used in a database, from one part we can grab the names, from other part we can grab the phone numbers, etc.. and zip them togehter
# note: we are not modifying anything, just zipping them together

my_list = [1, 2, 3]
your_list = [10, 20, 30]


def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


print(list(zip(my_list, your_list)))
print(my_list)
