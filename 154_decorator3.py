# Decorator Pattern - a Higher Order Function

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('****************')
        func(*args, **kwargs)
        print('****************')
    return wrap_func


@my_decorator  # it allows to add extra functionality! Enhances the function
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


hello('hiii')
