# Lambda functions are ANONYMOUS (dont need to name them); use them once and you are dont with them


from functools import reduce


my_list = [1, 2, 3]

# WITH LAMBDA WE DO NOT NEED TO CREATE A FUNCTION. SYNTAX: lambda param: action(param)

# def multiply_by2(item):
#     return item*2


# IF WANT TO USE LAMBDA FILTER
# def only_odd(item):
#     return item % 2 != 0

# TO USE LAMBDA WITH REDUCE()
# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item


print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc+item, my_list))
print(my_list)
