# Create a squared Lambda list
my_list = [5, 4, 3]

print(list(map(lambda item: item**2, my_list)))

# List Sorting

a = [(12, 24), (0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])  # COMMON WAY TO ADJUST YOUR SORTING!
print(a)

# print(list(filter(lambda item: item)))
