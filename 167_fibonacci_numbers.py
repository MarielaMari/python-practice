# Possible INTERVIEW QUESTION:
# Fibonacci sequence introduced by the Italian mathematician
# Starts with 0 and 1, and every next number is the sum of the previous two: 0, 1, 1, 2, 3, 5, 8, 13, 21, etc.

def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(21): # 21 to be able to get F20 because it starts from 0
    print(x)
