# Regular expressions are very useful when you are doing validations.
# for example if someone has entered the correct email or password,
# RE are NOT typical for Python, you can use them in ANY language
# RE give us not only TRUE or FALSE but actual expressions- info where it occures in a string- match objects
import re

pattern = re.compile('this')
string = 'search inside of this text, please!'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a)
print(b)
print(c)
print(d)
