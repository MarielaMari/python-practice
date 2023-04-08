some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

# Using LIST COMPREHENSION:

# NOT VERY READABLE BUT IT IS SHORT
dupl = list(set([char for char in some_list if some_list.count(char) > 1]))
print('\n ---Duplicates found using list comprehension:', dupl)
