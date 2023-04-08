# Decorator - a Higher Order Function

def my_decorator(func):
    def wrap_func():
        print('****************')
        func()
        print('****************')
    return wrap_func


@my_decorator  # it allows to add extra functionality! Enhances the function
def hello():
    print('hellooooooo')


@my_decorator
def buy():
    print('See ya later!')


hello()
buy()
