# RE https://regex101.com/codegen?language=python
# In regex101 use the CODE GENERATOR and copy the code you need: r"([a-zA-Z}).([a])"

import re

# from Code Generator in redex101.com, the r stands for a row string
pattern = re.compile(r"([a-zA-Z}).([a])")
string = 'seach inside of this text, please!'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
# print(a)
# print(b)
# print(c)
# print(d)
print(a.group())
print(a.group(1))
