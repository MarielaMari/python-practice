from collections import Counter, defaultdict, OrderedDict

# li = [1, 2, 3, 4, 5, 6, 7, 7]
# sentence= 'blah blah blah thinking about python'

# print(Counter(li))
# print(Counter(sentence))


# dictionary = defaultdict(int, {'a': 1, 'b': 2})
# print(dictionary['c'])

# In general, dictionaries are NOT ordered; the larger a dictionary gets, there is no guarantee things will be printed in order;
# However, if you need things in order, than use OrderedDict()' NOTE: if you switch the order of a and b in one of the dictionaries, you will get FALSE, i.e. the dictionaries are not the same
#NOTE: Recently Python has made Dictionaries ordered by DEFAULT in Python 3.7 and up
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2
print(d2 == d)
