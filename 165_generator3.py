#To create a generator:

def gen_fun(num):
    for i in range(num):
        yield i #make sure you pause the function; so, later you can use it with for example a for loop

for item in gen_fun(10):